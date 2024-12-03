from Visitor import Visitor
from StaticError import *
from AST import *
from Utils import *

from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser

import collections.abc

# utils
def lookup(name, lst, func):
    for x in lst:
        if name == func(x):
            return x
    return None
def remv(l: list, name):
    for x in l:
        if type(x) is name:
            l.remove(x)
    return l

def printO(o):      # print O to debug
    for x in range(len(o)):
        print("Scope ", x)
        for y in o[x]:
            if type(y) == VarDecl:
                print("\tVarDecl: ", y.name)
            elif type(y) == ParamDecl:
                print("\tParamDecl: ", y.name)
            elif type(y) == FuncDecl:
                print("\tFuncDecl: ", y.name)
            else: print("\tUnknown type: ", y.name)
        print("-----")      # to seperate
def print_and_stop(variables: List):
    for x in variables:
        print(x)
    raise 2
# IMPORTANT FUNC
def typeCompare(lhs, rhs):
    # verify type; may go to another class in Phrase 2
    if type(lhs) is VoidType:
        raise TypeMismatchInStatement(lhs)
    if type(lhs) is ArrayType:
        raise TypeMismatchInStatement(lhs)

def checkDeclare(node, env):
    name = node.name
    for scope in env:       # check each scopes from in to out
        result = lookup(name, scope, lambda x: x.name)
        if result is not None:          # has found declared
            return True
    return False

class OutFuncEnviIni(Visitor):
    def __init__(self):    # ini
        pass

    def check(self): return self.visitProgram(self.ast)  # to run to find o; 2 layer o

    # PROGRAM
    def visitProgram(self, ctx: Program, o):
        o = [[]]        # ini 2D o
        for outfunc in ctx.decls:
            o = self.visit(outfunc, o)        # replace o with visit each VarDecl nodes with o
        return o                # return result

    def visitVarDecl(self, ctx: VarDecl, o):
        o[0] += [ctx]           # add var nodes itself to global scope
        return o                # return result

    def visitFuncDecl(self, ctx: FuncDecl, o):
        o[0] += [ctx]           # add func nodes itself to global scope
        return o                # return result

class StaticChecker(Visitor):   # every testcases will have >=1 error hence must raise error by default.
    def __init__(self, ast):    # ini
        self.ast = ast      # ast
        self.No_Entry_Point = True      # ini true
        self.Loop_Counter = 0           # ini loop counter to check indirect loop


        self.o = [[
            FuncDecl("readInteger", VoidType(), [], None, BlockStmt([])),
            FuncDecl("printInteger", VoidType(), [ParamDecl("anArg", IntegerType())], None, BlockStmt([])),
            FuncDecl("readFloat", VoidType(), [], None, BlockStmt([])),
            FuncDecl("writeFloat", VoidType(), [ParamDecl("anArg", FloatType())], None, BlockStmt([])),
            FuncDecl("readBoolean", VoidType(), [], None, BlockStmt([])),
            FuncDecl("printBoolean", VoidType(), [ParamDecl("anArg", BooleanType())], None, BlockStmt([])),
            FuncDecl("readString", VoidType(), [], None, BlockStmt([])),
            FuncDecl("printString", VoidType(), [ParamDecl("anArg", StringType())], None, BlockStmt([])),
            FuncDecl("super", VoidType(), [ParamDecl("anArg", AtomicType())], None, BlockStmt([])),
            FuncDecl("preventDefault", VoidType(), [], None, BlockStmt([]))
        ]
        ]

    def check(self): return self.visitProgram(self.ast, self.o)  # this should have already been in the file

    # TYPE
    def visitBooleanType(self, ctx: BooleanType, o): return BooleanType()    # the type returns itself; used for declaring
    def visitIntegerType(self, ctx: IntegerType, o): return IntegerType()    # the type returns itself; used for declaring
    def visitFloatType(self, ctx: FloatType, o): return FloatType()    # the type returns itself; used for declaring
    def visitStringType(self, ctx: StringType, o): return StringType()    # the type returns itself; used for declaring
    def visitVoidType(self, ctx: VoidType, o): return VoidType()    # the type returns itself; used for declaring



    def visitAutoType(self, ctx: AutoType, o): return AutoType()
    def visitArrayType(self, ctx: ArrayType, o):  return o          # WIP

    # TEXT AND LITERAL
    def visitBooleanLit(self, ctx: BooleanLit, o): return BooleanType()     # element returns its type
    def visitIntegerLit(self, ctx: IntegerLit, o): return IntegerType()     # element returns its type
    def visitFloatLit(self, ctx: FloatLit, o): return FloatType()     # element returns its type
    def visitStringLit(self, ctx: StringLit, o): return StringType()     # element returns its type

    def visitId(self, ctx: Id, o):          # visit if the ID has been declared
        for env in o:             # check each scope from in to out
            result = lookup(ctx.name, env, lambda x: x.name)
            if result is not None:          # has found declared
                return o
        raise Undeclared(Variable(), ctx.name)  # declare unfound

    def visitArrayCell(self, ctx: ArrayCell, o):
        return o
    def visitArrayLit(self, ctx: ArrayLit, o):
        #if ctx.explist.__len__() > 1:
        first_type = type(ctx.explist[0])     # take the first type
        for x in ctx.explist[1:]:
            if type(x) is not first_type:     # if one type has diff type from the first
                raise IllegalArrayLiteral(x)    # err
        return o          # WIP

    # PROGRAM
    def visitProgram(self, ctx: Program, o):
        global_o = OutFuncEnviIni().visit(ctx, o)      # ini global envi list just for loop; to seperate from inner nodes

        # Redeclared
        node = 0    # counter for node check from first node to its node
        for outfunc in ctx.decls:
            if type(outfunc) == VarDecl:        # if var
                for x in range(node):
                    compare_node = global_o[0][x]
                    if compare_node.name == outfunc.name and type(compare_node) == VarDecl:  # if found same name and type
                        raise Redeclared(Variable(), compare_node.name)    # err
            elif type(outfunc) == FuncDecl:      # if func
                for x in range(node):                  # if func
                    compare_node = global_o[0][x]
                    if compare_node.name == outfunc.name and type(compare_node) == FuncDecl:  # if found same name and type
                        raise Redeclared(Function(), compare_node.name)    # err
            # No Entry Point
            if (type(outfunc) == FuncDecl       # if a function
                    and outfunc.name == "main"          # name main
                    and outfunc.params == []          # no paras
                    and outfunc.return_type == VoidType() # and return Type
                    and outfunc.inherit == None         # no inherit
            ):
                self.No_Entry_Point = False     # since found the main function
            o = self.visit(outfunc, o)             # visit each node
            node += 1           # adv
        if self.No_Entry_Point == True: raise NoEntryPoint()                # no proper main function
        return

    # GLOBAL AND EXPRESSION
    def visitVarDecl(self, ctx: VarDecl, o):
        # check redeclare variable
        if checkDeclare(ctx, o):
            raise Redeclared(Variable(), ctx.name)

        # check Auto type
        if ctx.typ == AutoType:
            # Invalid auto
            if ctx.init is None:
                raise Invalid(Variable(), ctx.name)

        o[0] += [ctx]       # add var to current scope
        return o
    def visitFuncDecl(self, ctx: FuncDecl, o):
        # check redeclare function
        for x in o[-1]:         # check global scope
            if x.name == ctx.name:
                raise Redeclared(Function(), ctx.name)

        # check parameters
        for x in ctx.params:
            o = self.visit(x, o)

        o[0] += [ctx]                       # add func name to global for recursion

        self.visit(ctx.body, o)            # visit its body

        remv(o[-1], ParamDecl)
        return o
    def visitParamDecl(self, ctx: ParamDecl, o):
        # check redeclare
        if checkDeclare(ctx, o):
            raise Redeclared(Parameter(), ctx.name)

        o[0] += [ctx]       # add var to current scope
        return o

    def visitAssignStmt(self, ctx: AssignStmt, o):
        # check decl:
        if not checkDeclare(ctx.lhs, o):
            raise Undeclared(Variable(), ctx.lhs.name)

        # compare type
        typeCompare(ctx.lhs, ctx.rhs)
        if type(ctx.rhs) == IntegerLit:
            return IntegerType()
        return ctx.rhs      # only return type of the lhs for For. CHECK TYPE IN DECLARE

    def visitBinExpr(self, ctx: BinExpr, o):    return o
    def visitUnExpr(self, ctx: UnExpr, o):  return o

    # ACTIVE STATEMENTS
    def visitBlockStmt(self, ctx: BlockStmt, o):
        # Visit + Must in loop
        env = [[]] + o  # create new scope
        for stmt in ctx.body:
            if (type(stmt) == BreakStmt or type(stmt) == ContinueStmt   # if break or cont is not in for, while
                    and self.Loop_Counter == 0):        # and not indirectly in loop
                raise MustInLoop(stmt)  # err
            o = self.visit(stmt, env)   # visit each statements in body
        return o        # ret its environment
    def visitIfStmt(self, ctx: IfStmt, o):
        cond = self.visit(ctx.cond, o)
        # check condition to be boolean
        if type(cond) is not BooleanType:       # if not bool
            raise TypeMismatchInExpression(ctx.cond)    # err

        # Visit + Must in loop
        if ((type(ctx.tstmt) == BreakStmt or type(ctx.tstmt) == ContinueStmt)   # if break or cont is not in for, while
                and self.Loop_Counter == 0):        # and not indirectly in loop
            raise MustInLoop(ctx.tstmt)  # err for true stmt
        env = [[]] + o  # create new scope
        o = self.visit(ctx.tstmt, env)   # visit each statements in true
        if ctx.fstmt:
            if (type(ctx.fstmt) == BreakStmt or type(ctx.fstmt) == ContinueStmt   # if break or cont is not in for, while
                    and self.Loop_Counter == 0):        # and not indirectly in loop
                raise MustInLoop(ctx.fstmt)  # err for false stmt
            env = [[]] + o  # create new scope
            o = self.visit(ctx.fstmt, env)   # visit each statements in false
        return o        # ret its environment
    def visitForStmt(self, ctx: ForStmt, o):
        init = self.visit(ctx.init, o)
        cond = self.visit(ctx.cond, o)
        upd = self.visit(ctx.upd, o)

        # check init to be integer
        if type(init) is not IntegerType:       # if not int
            raise TypeMismatchInExpression(ctx.init)    # err
        # check condition to be boolean
        if type(cond) is not BooleanType:       # if not bool
            raise TypeMismatchInExpression(ctx.cond)    # err
        # check update to be integer
        if type(upd) is not IntegerType:       # if not int
            raise TypeMismatchInExpression(ctx.upd)    # err

        self.Loop_Counter += 1              # add once more loop

        # visit
        if type(ctx.stmt) is not BlockStmt:
            env = [[]] + o                  # create new scope
            self.visit(ctx.stmt, env)       # visit stmt
        else: self.visit(ctx.stmt, o)       # visit stmt

        self.Loop_Counter -= 1              # del loop
        return o
    def visitWhileStmt(self, ctx: WhileStmt, o):
        cond = self.visit(ctx.cond, o)
        # check condition to be boolean
        if type(cond) is not BooleanType:       # if not bool
            raise TypeMismatchInExpression(ctx.cond)    # err

        self.Loop_Counter += 1              # add once more loop

        # visit
        if type(ctx.stmt) is not BlockStmt:
            env = [[]] + o                  # create new scope
            self.visit(ctx.stmt, env)       # visit stmt
        else: self.visit(ctx.stmt, o)       # visit stmt

        self.Loop_Counter -= 1              # del loop
        return o

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o):
        cond = self.visit(ctx.cond, o)
        # check condition to be boolean
        if type(cond) is not BooleanType:       # if not bool
            raise TypeMismatchInExpression(ctx.cond)    # err

        self.Loop_Counter += 1              # add once more loop
        # visit
        if type(ctx.stmt) is not BlockStmt:
            env = [[]] + o                  # create new scope
            self.visit(ctx.stmt, env)       # visit stmt
        else: self.visit(ctx.stmt, o)       # visit stmt

        self.Loop_Counter -= 1              # del loop
        return o

    def visitFuncCall(self, ctx: FuncCall, o):
        # check decl:
        if not checkDeclare(ctx, o):
            raise Undeclared(Function(), ctx.name)
        return o # nothing
    def visitCallStmt(self, ctx: CallStmt, o):
        # check decl:
        if not checkDeclare(ctx, o):
            raise Undeclared(Function(), ctx.name)
        return o # nothing
    # NAIVE STATEMENTS
    def visitBreakStmt(self, ctx: BreakStmt, o): return o    # nothing
    def visitContinueStmt(self, ctx: ContinueStmt, o): return o    # nothing
    def visitReturnStmt(self, ctx: ReturnStmt, o):
        printO(o)       # may use return as a stop in code
        raise 2
        return o # nothing