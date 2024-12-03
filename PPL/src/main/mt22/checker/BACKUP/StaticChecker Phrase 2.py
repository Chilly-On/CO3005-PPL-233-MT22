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
def lookup_Var_Param(name, lst, func):
    for x in lst:
        if type(x) is VarDecl or type(x) is ParamDecl:
            if name == func(x):
                return x
    return None
def lookup_Func(name, lst, func):
    for x in lst:
        if type(x) is FuncDecl:
            if name == func(x):
                return x
    return None
def remv(l: list, name):
    del_list = []
    for x in l:
        if type(x) is name:
            del_list += [x]
    for x in del_list:
        l.remove(x)
    return l

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
    for x in variables:
        print(x)
    raise 2
# IMPORTANT FUNC
def type_compare_expr(l, r):     # expr compare, return the side having errors
    # verify type
    if type(l) is VoidType:     # invalid l
        return 'l'
    elif type(l) is ArrayType:
        return arr_compare(l, r)
    elif type(l) is AutoType:   # l is auto, accept all
        if type(r) is VoidType:     # r cannot void
            return 'r'
        else: return None       # others are OK
    elif AutoType is type(r):   # r is auto, accept all; l only int, float, bool, string
        return None
    elif type(l) is IntegerType or type(l) is FloatType:            # check num
        if type(r) is IntegerType or type(r) is FloatType:    # accept both int and float
            return None
        else:
            return 'r'
    else:                       # l other types: bool, string
        if type(l) is type(r):      # only accept same type
            return None
        else:
            return 'r'
def type_compare_stmt(l, r):     # assign stmt compare, return the side having errors
    # verify type
    if type(l) is VoidType:     # invalid l
        return 'l'
    elif type(l) is ArrayType:
        if arr_compare(l, r) is not None:   # if arr has err, always err r
            return 'r'
    elif type(l) is AutoType:   # l is auto, accept all
        if type(r) is VoidType:     # r cannot void
            return 'r'
    elif type(r) is AutoType:   # r is auto, accept all; only int, float, bool, string
        return None
    elif type(l) is IntegerType or type(l) is FloatType:            # check num
        if type(r) is IntegerType or type(r) is FloatType:    # accept both int and float
            return None
        else:
            return 'r'
    else:                       # other types
        if type(l) is type(r):      # only accept same type
            return None
        else:
            return 'r'
def arr_compare(l, r):
    if type(l) is ArrayType and type(r) is ArrayType:   # if both are array
        if l.dimensions[0] == r.dimensions[0]:          # if same first dimen list
            if len(l.dimensions) > 1 and len(r.dimensions) > 1:     # if have >1 ele
                return arr_compare(l.dimensions[1:], r.dimensions[1:])             # cut head then compare
            else:
                if len(l.dimensions) == 1:  # if only 1 ele, convert to pure ele
                    l = l.typ
                if len(r.dimensions) == 1:  # if only 1 ele, convert to pure ele
                    r = r.typ
                return arr_compare(l, r)
        else:   # wrong dimension, always err the 2nd
            return 'r'
    elif type(l) is ArrayType:  # l has redundant array dimen
        return 'l'
    elif type(r) is ArrayType:  # r has redundant array dimen
        return 'r'
    else:       # both are pure type, compare them
        return type_compare_stmt(l, r)
def extract_array(input, arr):
    if len(input) == 0:      # if input empty
        if len(arr) == 0:       # if arr is also empty
            return
    else:           # still have input
        if input[0] < arr.cell[0]:   # if valid input
            return extract_array(input[1:], arr[1:])
        else:               # invalid input
            return None


def checkDeclare(node, env, typ: VarDecl or ParamDecl or FuncDecl):
    name = node.name
    if typ is VarDecl or typ is ParamDecl:
        for scope in env:       # check each scopes from in to out
            result = lookup_Var_Param(name, scope, lambda x: x.name)
            if result is not None:          # has found declared
                return result
        return None
    else:   # Func
        for scope in env:       # check each scopes from in to out
            result = lookup_Func(name, scope, lambda x: x.name)
            if result is not None:          # has found declared
                return result
        return None

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
        self.Current_Function = None    # to store the current function node
        self.No_Entry_Point = True      # ini true
        self.First_Return = False       # store if a function has checked first return stmt in func scope
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

    def visitId(self, ctx: Id, o):          # visit if the ID has been declared
        result = checkDeclare(ctx, o, VarDecl)
        if result is not None:          # has found declared
            return result.typ               # return its type
        raise Undeclared(Variable(), ctx.name)  # declare unfound

    def visitArrayCell(self, ctx: ArrayCell, o):
        # load decl
        decl = checkDeclare(ctx, o, VarDecl)
        if decl is None:        # if not decl
            raise Undeclared(Function(), ctx.name)

        # check type
        node_type = decl.typ      # take its type
        if type(node_type) is not ArrayType:                     # variable is not array, raise all node
            raise TypeMismatchInExpression(ctx)

        if len(ctx.cell) != len(node_type.dimensions):  # if l n' r diff size
            raise TypeMismatchInStatement(ctx)    # raise err in this node

        # check input is int
        for x in ctx.cell:
            if type(self.visit(x, o)) is not IntegerType:                  # if not int, raise
                raise TypeMismatchInExpression(ctx)         # raise err in this node

        return node_type.typ                # extract array to pure type

    def visitArrayLit(self, ctx: ArrayLit, o):
        first_type = self.visit(ctx.explist[0], o)     # take the first type; maybe an array ele
        if len(ctx.explist) > 1:        # if have more than 1 ele
            for x in ctx.explist[1:]:
                if type(self.visit(x, o)) is not type(first_type):     # if one type has diff type from the first
                    raise IllegalArrayLiteral(x)    # err

        # declare array type
        arr_type = None
        dimen = []
        if type(first_type) is not ArrayType:           # if the type is not array, return it
            arr_type = first_type
            dimen += [len(ctx.explist)]
        else:       # if multi-dimen array, concate them
            arr_type = first_type.typ                   # type is as same as inner; this takes pure array type
            dimen = ([len(ctx.explist)] + first_type.dimensions)    # dimen is cur array len concat with each element's dimen
        return ArrayType(dimen, arr_type) # return type as the first ele; aka convert lit to type

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

            self.Current_Function = outfunc     # store cur func data
            self.First_Return = False
            o = self.visit(outfunc, o)             # visit each node
            self.Current_Function = None        # no longer in func

            node += 1           # adv
        if self.No_Entry_Point == True: raise NoEntryPoint()                # no proper main function
        return

    # GLOBAL AND EXPRESSION
    def visitVarDecl(self, ctx: VarDecl, o):
        # check redeclare variable
        if checkDeclare(ctx, o, VarDecl):
            raise Redeclared(Variable(), ctx.name)

        # check Auto type
        if type(ctx.typ) is AutoType:
            # Invalid auto
            if ctx.init is None:
                raise Invalid(Variable(), ctx.name)
        else:       # other types
            if ctx.init is not None:            # compare type if have ini
                err = type_compare_stmt(self.visit(ctx.typ, o), self.visit(ctx.init, o))
                if err is not None:
                    if err == 'l':
                        raise TypeMismatchInStatement(ctx.typ)
                    elif err == 'r':
                        raise TypeMismatchInStatement(ctx.init)

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
        if checkDeclare(ctx, o, ParamDecl):
            raise Redeclared(Parameter(), ctx.name)

        o[0] += [ctx]       # add var to current scope
        return o

    def visitAssignStmt(self, ctx: AssignStmt, o):
        # check decl:
        l = checkDeclare(ctx.lhs, o, VarDecl)
        if not l:           # if not found
            raise Undeclared(Variable(), ctx.lhs.name)

        # compare type
        if type(l.typ) is not AutoType:     # not auto type
            err = type_compare_stmt(self.visit(ctx.lhs, o), self.visit(ctx.rhs, o)) # check type same with vardecl
            if err is not None:
                if err == 'l':
                    raise TypeMismatchInStatement(ctx.lhs)
                elif err == 'r':
                    raise TypeMismatchInStatement(ctx.rhs)

        return self.visit(ctx.rhs, o)           # return for For stmt

    def visitBinExpr(self, ctx: BinExpr, o):
        # take type of var based on declare
        l = self.visit(ctx.left, o)
        r = self.visit(ctx.right, o)

        err = type_compare_expr(l, r)     # precheck type in case Auto
        if err is not None:
            if err == 'l':
                raise TypeMismatchInStatement(ctx.left)
            elif err == 'r':
                raise TypeMismatchInStatement(ctx.right)
        # AutoType
        if type(l) is AutoType and type(r) is AutoType:   # if both are auto, accept all sign
            return AutoType()

        auto_side = 'x'                # raise flag for side with Auto
        if type(l) is AutoType:
            auto_side = 'l'
        elif type(r) is AutoType:
            auto_side = 'r'

        # check op
        num_op = ['*', '/', '+', '-']       # '%' seperate, must all integer
        logic_op = ['&&', '||']
        eq_op = ['==', '!=']
        compare_op = ['<', '>', '<=', '>=']

        # String check
        if ctx.op == '::':     # if meet concate op
            if auto_side == 'l':        # if l is auto
                if type(r) is StringType:   # if r is correct type
                    return StringType()                             # result string
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx.right) # unmatch
            else:                       # if l is not auto
                if type(l) is StringType:
                    if type(r) is StringType or auto_side == 'r':   # if both are string or r is auto
                        return StringType()                             # result string
                    else: # unmatch
                        raise TypeMismatchInExpression(ctx.right) # unmatch
                else:
                    raise TypeMismatchInExpression(ctx.left)

        # check %
        if ctx.op == '%':     # if meet num op
            if auto_side == 'l':        # if l is auto
                if type(r) is IntegerType:   # if r is correct type
                    return IntegerType()                             # return it
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx.right) # unmatch
            else:                       # if l is not auto
                if type(l) is IntegerType:    # if both are int
                    if type(r) is IntegerType or auto_side == 'r':
                        return IntegerType()
                    else: raise TypeMismatchInExpression(ctx.right) # unmatch
                else:
                    raise TypeMismatchInExpression(ctx.left)

        # check &&, ||
        if ctx.op in logic_op:     # if meet num op
            if auto_side == 'l':        # if l is auto
                if type(r) is BooleanType:   # if r is correct type
                    return BooleanType()                             # result string
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx.right) # unmatch
            else:                       # if l is not auto
                if type(l) is BooleanType:   # if both are int or bool
                    if type(r) is BooleanType or auto_side == 'r':
                        return BooleanType()
                    else:                                       # unmatch
                        raise TypeMismatchInExpression(ctx.right)
                else:                                       # unmatch
                    raise TypeMismatchInExpression(ctx.left)

        # check ==, !=
        if ctx.op in eq_op:     # if meet num op
            if auto_side == 'l':        # if l is auto
                if type(r) is IntegerType or type(r) is BooleanType:   # if r is correct type
                    return BooleanType()                             # result string
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx.right) # unmatch
            else:                       # if l is not auto
                if (type(l) is IntegerType or type(l) is BooleanType):   # if both are int or bool
                    if (type(r) is IntegerType or type(r) is BooleanType):
                        return BooleanType()
                    else:                                       # unmatch
                        raise TypeMismatchInExpression(ctx.right)
                else:                                       # unmatch
                    raise TypeMismatchInExpression(ctx.left)

        # check accept int or float
        if ctx.op in num_op + compare_op:     # if meet num op
            if auto_side == 'l':        # if l is auto
                if type(r) is IntegerType or type(r) is FloatType:   # if r is correct type
                    if ctx.op in num_op:      # if num

                        return r        # type based on non-auto
                    else:               # the bool
                        return BooleanType()
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx.right) # unmatch
            else:
                if (type(l) is IntegerType or type(l) is FloatType):   # if both are num or bool
                    if (type(r) is IntegerType or type(r) is FloatType):
                        if ctx.op in num_op:      # if num
                            if type(l) is IntegerType and type(r) is IntegerType:   # if both side are int, return int
                                return IntegerType()
                            else:
                                return FloatType()                # return float
                        else: return BooleanType()
                    else:                                       # unmatch
                        raise TypeMismatchInExpression(ctx.right)
                else:                                       # unmatch
                    raise TypeMismatchInExpression(ctx.left)
        print_and_stop(["UNKNOWN TYPE"])

    def visitUnExpr(self, ctx: UnExpr, o):      # minus or negation
        exp = self.visit(ctx.val, o)
        if type(exp) is AutoType:       # if auto
            return exp                          # return its type

        # check -
        if ctx.op == '-':     # if meet negative op
            if (type(exp) is IntegerType or type(exp) is FloatType):    # exp must be number
                return exp                          # return its type
            else:
                raise TypeMismatchInExpression(ctx.val)     # err

        # check !
        if ctx.op == '!':     # if meet negative op
            if type(exp) is BooleanType:    # exp must be bool
                return exp                          # return its type
            else:
                raise TypeMismatchInExpression(ctx.val)     # err

        print_and_stop(["UNKNOWN RETURN"])

    # ACTIVE STATEMENTS
    def visitBlockStmt(self, ctx: BlockStmt, o):
        # Visit + Must in loop
        env = [[]] + o  # create new scope
        for stmt in ctx.body:
            if (type(stmt) == BreakStmt or type(stmt) == ContinueStmt   # if break or cont is not in for, while
            and self.Loop_Counter == 0):        # and not indirectly in loop
                raise MustInLoop(stmt)  # err
            o = self.visit(stmt, env)   # visit each statements in body
        return o        # err its environment
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
        return o        # err its environment
    def visitForStmt(self, ctx: ForStmt, o):
        init = self.visit(ctx.init, o)
        cond = self.visit(ctx.cond, o)
        upd = self.visit(ctx.upd, o)

        # check init
        if type(init) is not IntegerType and type(init) is not AutoType:       # if not int
            raise TypeMismatchInStatement(ctx.init)    # err
        # check condition to be boolean
        if type(cond) is not BooleanType and type(cond) is not AutoType:       # if not bool
            raise TypeMismatchInStatement(ctx.cond)    # err
        # check update to be integer
        if type(upd) is not IntegerType and type(upd) is not AutoType:       # if not int
            raise TypeMismatchInStatement(ctx.upd)    # err

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
        if type(cond) is not BooleanType and type(cond) is not AutoType:       # if not bool
            raise TypeMismatchInStatement(ctx.cond)    # err

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
        if type(cond) is not BooleanType and type(cond) is not AutoType:       # if not bool
            raise TypeMismatchInStatement(ctx.cond)    # err

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
        decl = checkDeclare(ctx, o, FuncDecl)
        if decl is None or type(decl) is not FuncDecl:        # if not decl
            raise Undeclared(Function(), ctx.name)

        # check type of parameters:
        para_list = decl.params
        # compare size of l and r
        if len(para_list) != len(ctx.args):  # if l n' r diff size
            raise TypeMismatchInExpression(ctx)    # raise err in this node; CALLFUNC CHANGE TO RAISE STATEMENT
        in_count = 0       # ini its counter to compare each type
        for para in para_list:      # take each para
            l = para.typ            # l is para type
            r = self.visit(ctx.args[in_count], o)  # r is matching input

            err = type_compare_stmt(l, r) # compare as stmt
            if err is not None:
                raise TypeMismatchInExpression(ctx)    # if have any err, always raise this node; CALLFUNC CHANGE TO RAISE STATEMENT
            in_count += 1  # adv
        return self.visit(decl.return_type, o)                 # err type
    def visitCallStmt(self, ctx: CallStmt, o):
        # check decl:
        decl = checkDeclare(ctx, o, FuncDecl)
        if decl is None or type(decl) is not FuncDecl:        # if not decl
            raise Undeclared(Function(), ctx.name)

        # check type of parameters:
        para_list = decl.params
        # compare size of l and r
        if len(para_list) != len(ctx.args):  # if l n' r diff size
            raise TypeMismatchInStatement(ctx)    # raise err in this node; CALLFUNC CHANGE TO RAISE STATEMENT
        in_count = 0       # ini its counter to compare each type
        for para in para_list:      # take each para
            l = para.typ            # l is para type
            r = self.visit(ctx.args[in_count], o)  # r is matching input

            err = type_compare_stmt(l, r) # compare as stmt
            if err is not None:
                raise TypeMismatchInStatement(ctx)    # if have any err, always raise this node; CALLFUNC CHANGE TO RAISE STATEMENT
            in_count += 1  # adv

        return self.visit(decl.return_type, o)                 # err type

    def visitReturnStmt(self, ctx: ReturnStmt, o):
        # check if need to check current return
        if self.First_Return == False or len(o) > 2:             # if has not checked first return o or in stmt
            # check type of r
            l = self.Current_Function.return_type # take cur function as l
            r = VoidType()      # if nothing, return void
            if ctx.expr:        # if have expr
                r = self.visit(ctx.expr, o)   # return its type

            err = type_compare_stmt(l, r)   # compare 2 types, rhs is expr
            if err is not None:
                if err == 'r':      # only raise r
                    if ctx.expr is None:                    # check if have expr, raise that, else, void
                        raise TypeMismatchInStatement(VoidType())
                    else:
                        raise TypeMismatchInStatement(ctx.expr)

        if self.First_Return == False and len(o) == 2:             # if has not checked first return o and not in stmt
            self.First_Return = True            # mark checked
        return o

    # NAIVE STATEMENTS
    def visitBreakStmt(self, ctx: BreakStmt, o): return o    # nothing
    def visitContinueStmt(self, ctx: ContinueStmt, o): return o    # nothing

    # TYPE
    def visitBooleanType(self, ctx: BooleanType, o): return BooleanType()    # the type returns itself; used for declaring
    def visitIntegerType(self, ctx: IntegerType, o): return IntegerType()    # the type returns itself; used for declaring
    def visitFloatType(self, ctx: FloatType, o): return FloatType()    # the type returns itself; used for declaring
    def visitStringType(self, ctx: StringType, o): return StringType()    # the type returns itself; used for declaring
    def visitVoidType(self, ctx: VoidType, o): return VoidType()    # the type returns itself; used for declaring

    def visitAutoType(self, ctx: AutoType, o): return AutoType()
    def visitArrayType(self, ctx: ArrayType, o):  return ctx                # return its node

    # TEXT AND LITERAL
    def visitBooleanLit(self, ctx: BooleanLit, o): return BooleanType()     # element returns its type
    def visitIntegerLit(self, ctx: IntegerLit, o): return IntegerType()     # element returns its type
    def visitFloatLit(self, ctx: FloatLit, o): return FloatType()     # element returns its type
    def visitStringLit(self, ctx: StringLit, o): return StringType()     # element returns its type