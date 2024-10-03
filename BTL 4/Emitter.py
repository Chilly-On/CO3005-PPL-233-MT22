from Utils import *
# from StaticCheck import *
# from StaticError import *
import main.mt22.codegen.CodeGenerator as cgen      # changed to match path
from MachineCode import JasminCode
from AST import *
from CodeGenError import *
from CodeGenerator import reduce


# DEBUG TOOLS
def printO(o):      # print O to debug
    for x in range(len(o)):
        print("Scope ", x)
        for y in o[x]:
            if type(y) == VarDecl:
                print("\tVarDecl: ", y.name, ", ", y.typ)
            elif type(y) == ParamDecl:
                print("\tParamDecl: ", y.name, ", ", y.typ)
            elif type(y) == FuncDecl:
                print("\tFuncDecl: ", y.name, ", ", y.return_type)
            else: print("\tUnknown type: ", y.name)
        print("-----")      # to seperate

def print_and_stop(variables):
    print("----------STOP----------")
    for x in variables:
        print(x)
    raise 2

# ULIITIES
def remvNull(l: list):
    return filter(lambda x: x is not None, l)

@abstractmethod
class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = []
        self.jvm = JasminCode()

    def getJVMType(self, inType):
        typeIn = type(inType)                           # take pure type
        if typeIn is IntegerType or typeIn is cgen.IntBoolType:
            return "I"
        elif typeIn is FloatType or typeIn is cgen.AutoType or typeIn is cgen.IntFloatType:
            return "F"
        elif typeIn is BooleanType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:               # add more layer based on dimension
            arr_dimen_str = ""
            for x in range(len(inType.dimensions)):
                arr_dimen_str += "["
            return arr_dimen_str + self.getJVMType(inType.typ)      # go to pure type
        elif typeIn is cgen.MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is cgen.ClassType:
            return "L" + str(inType.name.name) + ";"

    def getFullType(self, inType):
        typeIn = type(inType)
        if typeIn is IntegerType or typeIn is cgen.IntBoolType:
            return "int"
        elif typeIn is FloatType or typeIn is cgen.AutoType or typeIn is cgen.IntFloatType:
            return "float"
        elif typeIn is BooleanType:
            return "boolean"
        elif typeIn is StringType:
            return "java/lang/String"
        elif typeIn is ArrayType:
            arr_dimen_str = ""
            for x in range(len(inType.dimensions)):
                arr_dimen_str += "["
            return arr_dimen_str + self.getJVMType(inType.typ)      # go to pure type
        elif typeIn is VoidType:
            return "void"

    def emitPUSHICONST(self, in_, frame):
        # in: Int or Sring
        # frame: Frame

        frame.push()
        if type(in_) is int:
            i = in_
            i = ((i + 32768) % 65536) - 32768          # round if num is too high
            if i >= -1 and i <= 5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
        elif type(in_) is bool:         # if is bool
            if in_ == "True":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "False":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)

    def emitPUSHFCONST(self, in_, frame):
        # in_: String
        # frame: Frame

        f = float(in_)
        frame.push()
        rst = "{0:.4f}".format(f)
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDCFloat(str(in_))

    ''' 
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''

    def emitPUSHCONST(self, in_, typ, frame):
        # in_: String
        # typ: Type
        # frame: Frame

        frame.push()
        if type(typ) is IntegerType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is FloatType:
            return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is StringType or type(in_) is cgen.AutoType:
            frame.push()
            return self.jvm.emitLDC(in_)
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    def emitALOAD(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...
        frame.pop()
        if type(in_) is IntegerType or type(in_) is cgen.IntBoolType:
            return self.jvm.emitIALOAD()
        elif type(in_) is FloatType or type(in_) is cgen.AutoType or type(in_) is cgen.IntFloatType:
            return self.jvm.emitFALOAD()
        elif type(in_) is BooleanType:
            return self.jvm.emitBALOAD()
        # elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:
        elif type(in_) is cgen.ClassType or type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitASTORE(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is IntegerType or type(in_) is cgen.IntBoolType:
            return self.jvm.emitIASTORE()
        elif type(in_) is FloatType or type(in_) is cgen.AutoType or type(in_) is cgen.IntFloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is BooleanType:
            return self.jvm.emitBASTORE()
        # elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:
        elif type(in_) is cgen.ClassType or type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))

    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''

    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        # in_: Int
        # varName: String
        # inType: Type
        # fromLabel: Int
        # toLabel: Int
        # frame: Frame
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ... -> ..., value

        frame.push()
        if type(inType) is IntegerType or type(inType) is cgen.IntBoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is FloatType or type(inType) is cgen.AutoType or type(inType) is cgen.IntFloatType:
            return self.jvm.emitFLOAD(index)
        elif type(inType) is BooleanType:
            return self.jvm.emitILOAD(index)
        # elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType:
        elif type(inType) is cgen.ClassType or type(inType) is StringType or type(inType) is ArrayType:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''

    def emitREADVAR2(self, name, typ, frame):
        # name: String
        # typ: Type
        # frame: Frame
        # ... -> ..., value

        # frame.push()
        raise IllegalOperandException(name)

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''

    def emitWRITEVAR(self, name, inType, index, frame):
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ..., value -> ...

        frame.pop()

        if type(inType) is IntegerType or type(inType) is cgen.IntBoolType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is FloatType or type(inType) is cgen.AutoType or type(inType) is cgen.IntFloatType:
            return self.jvm.emitFSTORE(index)
        elif type(inType) is BooleanType:
            return self.jvm.emitISTORE(index)
        # elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType:
        elif type(inType) is cgen.ClassType or type(inType) is StringType or type(inType) is ArrayType:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''

    def emitWRITEVAR2(self, name, typ, frame):
        # name: String
        # typ: Type
        # frame: Frame
        # ..., value -> ...

        # frame.push()
        raise IllegalOperandException(name)

    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    '''

    def emitATTRIBUTE(self, lexeme, in_, isFinal = False, value = None):
        # lexeme: String
        # in_: Type
        # isFinal: Boolean
        # value: String

        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal)

    def emitGETSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETSTATICDefault(self, lexeme, in_, frame):         # create alt default to add class type
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()

        return self.jvm.emitGETSTATIC("MT22Class." + lexeme, self.getJVMType(in_))

    def emitPUTSTATICDefault(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        return self.jvm.emitPUTSTATIC("MT22Class." + lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''

    def emitINVOKESTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''

    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        # lexeme: String
        # in_: Type
        # frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''

    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        paraIn = None
        if in_.partype:         # concate parameter to print
            paraIn = reduce(lambda x, y: x + self.getJVMType(y), in_.partype, "")
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_.rettype), paraIn)

    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''

    def emitNEGOP(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result

        if type(in_) is IntegerType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        # in_: Type
        # frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHICONST(True, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHICONST(False, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitADDOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntegerType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntegerType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntegerType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntegerType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''

    def emitOROP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, frame):
        # op: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        if op == ">":                         # take the true to another branchs
            result.append(self.jvm.emitIFICMPLE(labelF))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(labelF))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(labelF))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(labelF))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(labelF))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(labelF))
        result.append(self.emitPUSHCONST(1, IntegerType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST(0, IntegerType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):         # based on label
        # op: String
        # in_: Type
        # trueLabel: Int
        # falseLabel: Int
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(falseLabel))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(falseLabel))
        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        # lexeme: String
        # in_: Type
        # isStatic: Boolean
        # frame: Frame
        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    '''   generate the end directive for a function.
    '''

    def emitENDMETHOD(self, frame):
        # frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast):
        # ast: Literal
        if type(ast) is IntegerType:
            return (str(ast.value), IntegerType())

    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''
    def emitNEWARRAY(self, _in, frame):
        # ast: ARRAYLIT
        # _in: AST input: ArrayType
        frame.pop()                         # pop stack to get the arr len
        if type(_in) is ArrayType:
            return self.jvm.emitANEWARRAY(self.getFullType(_in))
        else:
            return self.jvm.emitNEWARRAY(self.getFullType(_in))



    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''

    def emitANEWARRAY(self, typ, frame):
        # ast: ARRAYLIT
        # typ: type of arr
        frame.pop()                         # pop stack to get the arr len
        return self.jvm.emitANEWARRAY(self.getFullType(typ))

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''

    def emitIFTRUE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''

    def emitIFFALSE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)

    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''

    def emitDUP(self, frame):
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''

    def emitI2F(self, typ, frame):          # change 2 types each other; input type of rhs
        # frame: Frame
        # typ: Integer or Float
        if type(typ) is IntegerType:
            return self.jvm.emitI2F()
        elif type(typ) is FloatType:
            return self.jvm.emitF2I()


    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        # in_: Type
        # frame: Frame

        # put all return type here; must comment pop so that it should not pop overflow when double return
        if type(in_) is IntegerType or type(in_) is cgen.IntBoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType  or type(in_) is cgen.AutoType or type(in_) is cgen.IntFloatType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is cgen.ClassType or type(in_) is StringType or type(in_) is ArrayType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()

    ''' generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    '''

    def emitLABEL(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    '''

    def emitGOTO(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitGOTO(str(label))

    ''' generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    '''

    def emitPROLOG(self, name, parent):
        # name: String
        # parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER(
            "java/land/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        # num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        # num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        self.buff = filter(lambda x: x != None, self.buff)      # delete all none
        for x in self.buff:     # not NONE in last
            file.write(x)
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''

    def printout(self, in_):
        # in_: String
        self.buff.append(in_)
        print(in_, end = "")      # print the input

    def clearBuff(self):
        self.buff.clear()
