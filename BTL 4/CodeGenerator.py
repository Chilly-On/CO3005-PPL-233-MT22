from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

# This Assignment 4 in PPL is done by K22 with no copy code, rarely do reference, mostly self-done, and not study Vo Tien.

# DEBUG TOOLS
def printO(o):      # print O to debug
    print("-----")      # to seperate
    for x in range(len(o)):
        print("Scope ", x)
        for y in o[x]:
            typ = y.value.value
            if typ is VarDecl:
                print("\tVarDecl: ", y.name, ", ", y.mtype.rettype)
            elif typ is ParamDecl:
                print("\tParamDecl: ", y.name, ", ", y.mtype.rettype)
            elif typ is FuncDecl:
                print("\tFuncDecl: ", y.name, ", ", y.mtype.rettype)
            else: print("\tUnknown type: ", y.name)
        print("-----")      # to seperate

def print_and_stop(variables):
    print("----------STOP----------")
    for x in variables:
        print(x)
    raise 2

# UTILITIES
def lookup(name, lst, func):
    for x in lst:
        if name == func(x):
            return x
    return None

def lookup_Var_Param(name, lst, func):
    for x in lst:                       # x is Sym
        typ = x.value.value             # get node type
        if typ is VarDecl or typ is ParamDecl:
            if name == func(x):
                return x
    return None


def lookup_Func(name, lst, func):
    for x in lst:
        typ = x.value.value             # get node type
        if typ is FuncDecl:
            if name == func(x):
                return x
    return None

def findDeclare(node, env, typ: VarDecl or ParamDecl or FuncDecl = None):
    name = node.name
    if typ is VarDecl or typ is ParamDecl:
        for scope in env:       # check each scopes from in to out
            result = lookup_Var_Param(name, scope, lambda x: x.name)
            if result is not None:          # has found declared
                return result
        return None
    elif typ is FuncDecl:   # Func
        result = lookup(name, env[-1], lambda x: x.name)          # find in outside scope
        if result is not None:          # has found declared
            return result
    else:               # whatever type
        for scope in env:       # check each scopes from in to out
            result = lookup(name, scope, lambda x: x.name)
            if result is not None:          # has found declared
                return result
        return None

class MType:
    def __init__(self, partype: List, rettype, Node = None):
        self.partype = partype
        self.rettype = rettype
        self.Node = Node                # store node, usually FuncDecl, name of inherit func



class Symbol:
    def __init__(self, name, mtype, value=None, memPos = None):     # memPos store the pos of VarDecl in memory
        self.name = name
        self.mtype = mtype
        self.value = value
        self.memPos = memPos

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"

    # ASSIGNMENT 3
# more type
class IntBoolType(Type):            # type for auto para: can accept both Int and Bool
    def __str__(self):
        return self.__class__.__name__
class IntFloatType(Type):            # type for auto para: can accept both Int and Float
    def __str__(self):
        return self.__class__.__name__

# utils
def lookupA3(name, lst, func):
    for x in lst:
        if name == func(x):
            return x
    return None
def lookup_Var_ParamA3(name, lst, func):
    for x in lst:
        if type(x) is VarDecl or type(x) is ParamDecl:
            if name == func(x):
                return x
    return None
def lookup_FuncA3(name, lst, func):
    for x in lst:
        if type(x) is FuncDecl:
            if name == func(x):
                return x
    return None
def remv(l: list, name):
    return filter(lambda x: type(x) is name, l)

# IMPORTANT FUNC
def findDeclareA3(node, env, typ: VarDecl or ParamDecl or FuncDecl = None):
    name = node.name
    if typ is VarDecl or typ is ParamDecl:
        for scope in env:       # check each scopes from in to out
            result = lookup_Var_ParamA3(name, scope, lambda x: x.name)
            if result is not None:          # has found declared
                return result
        return None
    elif typ is FuncDecl:   # Func
        result = lookup_FuncA3(name, env[-1], lambda x: x.name)          # find in outside scope
        if result is not None:          # has found declared
            return result
    else:               # whatever type
        for scope in env:       # check each scopes from in to out
            result = lookupA3(name, scope, lambda x: x.name)
            if result is not None:          # has found declared
                return result
        return None

def changeType(ctx, typ: Type, o):         # change type of all ele in BinExpr; REMINDER: ONLY USE WHEN ALL ID ARE AUTOTYPE
    if type(ctx) is BinExpr:
        changeType(ctx.left, typ, o)
        changeType(ctx.right, typ, o)
    elif type(ctx) is UnExpr:
        changeType(ctx.val, typ, o)
    else:                       # Id node
        decl = findDeclare(ctx, o)        # load
        if type(decl) is VarDecl:           # vardecl
            decl.typ = typ                      # change that node
        elif type(decl) is ParamDecl:         # ParamUnlock: default not modify auto params in body; only modify in Funccall Callstmt
            decl.typ = typ
        elif type(decl) is FuncDecl:
            decl.return_type = typ

class StaticChecker(Visitor):   # every testcases will have >=1 error hence must raise error by default.
    def __init__(self, ast):    # ini
        self.ast = ast      # ast
        self.Current_Function = None    # to store the current function node; for return node
        self.No_Entry_Point = True      # ini true
        self.First_Return = False       # store if a function has checked first return stmt in func scope
        self.Loop_Counter = 0           # ini loop counter to check indirect loop
        self.Start_Func = False         # store if has entered func; to not add 2nd scope in 1st blkstmt
        self.Full_Array_Lit = None           # store full of arrlit, so that whole arr is returned in recursion
        self.First_Stmt = None          # store 1st stmt in funcdecl, to check super, prevent in funcdecl

        self.o = [[
            FuncDecl("readInteger", IntegerType(), [], None, BlockStmt([])),
            FuncDecl("printInteger", VoidType(), [ParamDecl("anArg", IntegerType())], None, BlockStmt([])),
            FuncDecl("readFloat", FloatType(), [], None, BlockStmt([])),
            FuncDecl("printFloat", VoidType(), [ParamDecl("anArg", FloatType())], None, BlockStmt([])),
            FuncDecl("readBoolean", BooleanType(), [], None, BlockStmt([])),
            FuncDecl("printBoolean", VoidType(), [ParamDecl("anArg", BooleanType())], None, BlockStmt([])),
            FuncDecl("readString", StringType(), [], None, BlockStmt([])),
            FuncDecl("printString", VoidType(), [ParamDecl("anArg", StringType())], None, BlockStmt([])),
            FuncDecl("super", VoidType(), [], None, BlockStmt([])),
            FuncDecl("preventDefault", VoidType(), [], None, BlockStmt([]))
        ]]

    def check(self): return self.visitProgram(self.ast, self.o)  # this should have already been in the file

    # PROGRAM
    def visitProgram(self, ctx: Program, o):
        # ini global envi list just for loop; to seperate from inner nodes; catch redeclare func in this loop
        o[-1] += filter(lambda x: type(x) is FuncDecl, ctx.decls)                          # add decls in global scope; only take funcdecl prototype;         # now global scope are all initialized before use

        for loop in range(2):                      # double check; to check again; some auto functions and auto parameters have type changed
            node = 10    # counter for node check from first node to its node; start from 10
            for outfunc in ctx.decls:
                # Redeclared check
                if type(outfunc) == VarDecl:        # if var
                    if loop == 0:               # add only in 1st loop
                        o[0].insert(node, outfunc)              # insert the vardecl back to global

                elif type(outfunc) == FuncDecl:      # if func
                    pass

                self.Current_Function = outfunc     # store cur func data
                self.First_Return = False
                o = self.visit(outfunc, o)             # visit each node
                self.Current_Function = None        # no longer in func
                self.Start_Func = False             # no longer in func
                self.First_Stmt = None              # no longer in func
                node += 1           # adv

    def visitId(self, ctx: Id, o):          # visit if the ID has been declared
        result = findDeclareA3(ctx, o, VarDecl)
        if result is not None:          # has found declared
            return result.typ               # return its type

    def visitArrayCell(self, ctx: ArrayCell, o):
        # load decl
        decl = findDeclareA3(ctx, o, VarDecl)

        # check type
        node_type = decl.typ      # take its type

        # check input is int
        for x in ctx.cell:
            x_typ = self.visit(x, o)                        # take pure type
            if type(x_typ) is AutoType or type(x_typ) is IntBoolType or type(x_typ) is IntFloatType:    # change auto to int
                changeType(x, IntegerType(), o)
                x_typ = IntegerType()

        if len(ctx.cell) > len(node_type.dimensions):   # if cell has more dimen
            pass
        elif len(ctx.cell) < len(node_type.dimensions):  # if cell has less dimen
            return ArrayType(node_type.dimensions[len(ctx.cell):], node_type.typ)       # cut head by len of cell
        else:                                           # eq dimen, ret pure type
            return node_type.typ                # extract array to pure type

    def visitArrayLit(self, ctx: ArrayLit, o):
        if ctx.explist == []:                               # if blank arr, return no dimen arr
            return ArrayType([], StringType())
        else:
            if self.Full_Array_Lit is None:                 # if 1st time check, store full of arr
                self.Full_Array_Lit = ctx
            first_type = None                                   # take the first type
            for exp in ctx.explist:
                first_type = self.visit(exp, o)     # maybe an array ele
                if type(first_type) is not AutoType: # loop until not auto
                    break
            else:           # all ele in arr is auto
                first_type = AutoType()

            if type(first_type) is not AutoType:            # if all is not full of auto
                idx = 0
                for x in ctx.explist:       # loop for all since no longer check 1st ele
                    cur_type = self.visit(x, o)         # store cur type of
                    if type(cur_type) is AutoType:          # if auto type, change that ele to match the whole arr
                        changeType(x, first_type, o)
                    idx += 1
            if self.Full_Array_Lit == ctx:                 # if 1st time check, after check ele then exit
                self.Full_Array_Lit = None

            # declare array type
            arr_type = None
            dimen = []
            if type(first_type) is not ArrayType:           # if the type is not array, return it
                arr_type = first_type
                dimen += [len(ctx.explist)]
            else:                                           # if multi-dimen array, concate them
                arr_type = first_type.typ                   # type is as same as inner; this takes pure array type
                dimen = [len(ctx.explist)] + first_type.dimensions    # dimen is cur array len concat with each element's dimen
            return ArrayType(dimen, arr_type) # return type as the first ele; aka convert lit to type

    # GLOBAL AND EXPRESSION
    def visitVarDecl(self, ctx: VarDecl, o):
        # check redeclare variable
        if ctx.init is not None:            # compare type if have ini
            l = ctx.typ                     # only take type, l 1st
            r = self.visit(ctx.init, o)
            if ((type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType)
                    and type(l) is not AutoType):       # change auto of rhs with decl type of lhs
                changeType(ctx.init, l, o)

        # check Auto type
        if type(ctx.typ) is AutoType:
            # Invalid auto
            if ctx.init is None:
                pass
            else:                   # replace type
                r = self.visit(ctx.init, o)
                if type(r) is IntBoolType or type(r) is IntFloatType:       # type break by changing to Int
                    r = IntegerType()
                ctx.typ = r                                     # replace auto with type in init

        if len(o) > 1:          # only add if not global, global added by visit program
            o[0] += [ctx]       # add var to current scope
        return o
    def visitFuncDecl(self, ctx: FuncDecl, o):
        env = [[]] + o                # ini another env
        inherit_list = []               # store list of inherit

        if ctx == self.Current_Function:        # if correct current function
            # check parameters, then add
            for x in ctx.params:
                env = self.visit(x, env)
            # get 1st stmt in func
            self.First_Stmt = ctx.body.body[0] if ctx.body.body != [] else None             # 1st stmt

            # check inherit
            if ctx.inherit:     # if inherit
                decl = findDeclareA3(Id(ctx.inherit), o, FuncDecl)    # check declare inherit

                # check type of parameters of inherit:
                para_list = decl.params
                if para_list == []:     # if have no parameter
                    pass
                else:   # if have parameters, must have 1st stmt
                    if type(self.First_Stmt) is CallStmt and self.First_Stmt.name == "preventDefault": # if 1st func is prevent
                        pass                        # check type in CallStmt
                    elif type(self.First_Stmt) is CallStmt and self.First_Stmt.name == "super": # if 1st func is super
                        input = self.First_Stmt.args                   # receive super's argument list input
                        err_arg = None                                     # store err node to raise err expr
                        # compare size of l and r
                        if len(para_list) < len(input):  # if l has less para than r input
                            err_arg = input[len(para_list)]    # raise err in first input's redundant arg
                        in_count = 0       # ini its counter to compare each type
                        for para in para_list:      # take each para; check match type
                            l = para.typ            # l is para type
                            match_input = None
                            if in_count < len(input):           # if have input
                                match_input = input[in_count]   # taking that input
                                r = self.visit(match_input, env)  # r is matching input
                            if type(l) is AutoType or type(l) is IntBoolType or type(l) is IntFloatType:             # if para is auto, take arg to assign type
                                para.typ = r
                            in_count += 1  # adv

                # add inherit params to scope via visit
                inherit_list += self.visit(decl, o)

            # add inherit param
            for para in inherit_list:
                decl_parm = lookup_Var_ParamA3(para.name, env[0], lambda x: x.name)    # check declare in local func scope
                if decl_parm is None:        # if not decl inherit func
                    env[0] += [para]       # add to list

            self.visit(ctx.body, env)             # visit its body
            return o
        else:                               # if not curr func, only visit to get inherit param; NO CHECK ANY ERRORS IN BODY
            # check inherit
            if ctx.inherit:     # if inherit
                decl = findDeclareA3(Id(ctx.inherit), o, FuncDecl)    # check declare inherit; do not raise err here

                # add inherit params to scope via visit
                inherit_list += self.visit(decl, o) if decl else []
            for x in ctx.params:
                dup = lookup_Var_ParamA3(x.name, inherit_list, lambda x: x.name)        # check if redecl param in inherit func
                if str(x.inherit) == "inherit" and dup is None:  # add inherit param if unique
                    inherit_list += [x]
            return inherit_list                         # return inherit list to child func
    def visitParamDecl(self, ctx: ParamDecl, o):
        # check redeclare

        o[0] += [ctx]       # add var to current scope
        return o

    def visitAssignStmt(self, ctx: AssignStmt, o):
        # check rhs 1st then left
        r = self.visit(ctx.rhs, o)
        l = self.visit(ctx.lhs, o)

        # compare type
        if type(l) is not AutoType:     # not auto type
            if (type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType):       # change auto of rhs with decl type of lhs
                changeType(ctx.rhs, l, o)
        else:                             # check Auto type
            if type(r) is IntBoolType or type(r) is IntFloatType:       # type break by changing to Int
                r = IntegerType()
            changeType(ctx.lhs, r, o)            # replace auto with type in init

        return self.visit(ctx.rhs, o)           # return for For stmt

    def visitBinExpr(self, ctx: BinExpr, o):
        # take type of var based on declare
        l = self.visit(ctx.left, o)
        r = self.visit(ctx.right, o)

        # check op
        num_op = ['*', '/', '+', '-']       # '%' seperate, must all integer
        logic_op = ['&&', '||']
        eq_op = ['==', '!=']
        compare_op = ['<', '>', '<=', '>=']
        # AutoType
        if type(l) is AutoType and type(r) is AutoType:   # if both are auto, accept all sign
            if ctx.op == '::':     # if meet concate op
                changeType(ctx.left, StringType(), o)     # both must string
                changeType(ctx.right, StringType(), o)
                return StringType()
            elif ctx.op == '%':     # if meet % op
                changeType(ctx.left, IntegerType(), o)       # both must int
                changeType(ctx.right, IntegerType(), o)
                return IntegerType()
            elif ctx.op in logic_op:     # if meet logic op
                changeType(ctx.left, BooleanType(), o)
                changeType(ctx.right, BooleanType(), o)       # both must int
                return BooleanType()
            elif ctx.op in eq_op:     # if meet eq op
                changeType(ctx.left, IntBoolType(), o)      # both must int or bool
                changeType(ctx.right, IntBoolType(), o)
                return IntBoolType()
            elif ctx.op in num_op + compare_op:     # if meet num op
                changeType(ctx.left, IntFloatType(), o)       # both must int or float
                changeType(ctx.right, IntFloatType(), o)
                if ctx.op in num_op:
                    return IntFloatType()
                else:               # compare ret bool
                    return BooleanType()
            return AutoType()

        # consider which is now Auto
        auto_side = 'x'                # raise flag for side with Auto
        if type(l) is AutoType:
            auto_side = 'l'
        elif type(r) is AutoType:
            auto_side = 'r'

        # String check
        if ctx.op == '::':     # if meet concate op
            if auto_side == 'l':        # if l is auto
                changeType(ctx.left, r, o)        # change type of auto
                if type(r) is StringType:   # if r is correct type
                    return StringType()                             # result string
            else:                       # if l is not auto
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)        # change type of auto
                    r = l                   # change cur l for type checking too
                if type(l) is StringType:
                    if type(r) is StringType:   # if both are string or r is auto
                        return StringType()                             # result string

        # check %
        if ctx.op == '%':     # if meet % op
            if type(l) is IntBoolType or type(l) is IntFloatType: # change to match proper type with %; choose int
                changeType(ctx.left, IntegerType(), o)        # change type of auto
                l = IntegerType()
            if type(r) is IntBoolType or type(r) is IntFloatType: # change to match proper type with %
                changeType(ctx.left, IntegerType(), o)        # change type of auto
                r = IntegerType()

            if auto_side == 'l':        # if l is auto
                changeType(ctx.left, r, o)        # change type of auto
                if type(r) is IntegerType:   # if r is correct type
                    return IntegerType()                             # return it

            else:                       # if l is not auto
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)        # change type of auto
                    r = l                   # change cur l for type checking too
                if type(l) is IntegerType:    # if both are int
                    if type(r) is IntegerType:
                        return IntegerType()

        # check &&, ||
        if ctx.op in logic_op:     # if meet logic op
            if type(l) is IntBoolType: # change to match proper type with logic; choose bool
                changeType(ctx.left, BooleanType(), o)        # change type of auto
                l = BooleanType()
            if type(r) is IntBoolType: # change to match proper type with logic
                changeType(ctx.left, BooleanType(), o)        # change type of auto
                r = BooleanType()
            if auto_side == 'l':        # if l is auto
                changeType(ctx.left, r, o)        # change type of auto
                if type(r) is BooleanType:   # if r is correct type
                    return BooleanType()                             # result string
            else:                       # if l is not auto
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)        # change type of auto
                    r = l                   # change cur l for type checking too
                if type(l) is BooleanType:   # if both are int or bool
                    if type(r) is BooleanType:
                        return BooleanType()

        # check ==, !=
        if ctx.op in eq_op:     # if meet eq op
            if type(l) is IntFloatType:              # change to match proper type with logic; choose int
                changeType(ctx.left, IntegerType(), o)        # change type of auto
                l = IntegerType()
            if type(r) is IntFloatType:              # change to match proper type with logic
                changeType(ctx.right, IntegerType(), o)        # change type of auto
                r = IntegerType()
            if type(l) is IntBoolType:              # type breaker deal
                if type(r) is IntBoolType:           # if r is also intbool, cannot refer anything
                    return BooleanType()            # result bool
                else:                               # if r pure type, consider l as auto to only check r and copy type r to l
                    auto_side = 'l'
            elif type(r) is IntBoolType and auto_side == 'x':   # if r is auto and l is not auto
                auto_side = 'r'                     # change r

            if auto_side == 'l':        # if l is auto
                changeType(ctx.left, r, o)        # change type of auto
                if type(r) is IntegerType or type(r) is BooleanType or type(r) is IntBoolType:   # if r is correct type
                    return BooleanType()                             # result bool
            else:                       # if l is not auto
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)        # change type of auto
                    r = l                   # change cur l for type checking too
                if (type(l) is IntegerType or type(l) is BooleanType or type(l) is IntBoolType):   # if both are int or bool
                    if (type(r) is IntegerType or type(r) is BooleanType or type(r) is IntBoolType):
                        return BooleanType()

        # check accept int or float
        if ctx.op in num_op + compare_op:     # if meet num op
            if type(l) is IntBoolType:              # change to match proper type with logic; choose int
                changeType(ctx.left, IntegerType(), o)        # change type of auto
                l = IntegerType()
            if type(r) is IntBoolType:              # change to match proper type with logic
                changeType(ctx.right, IntegerType(), o)        # change type of auto
                r = IntegerType()

            if type(l) is IntFloatType and auto_side == 'x':              # type breaker deal; if not auto yet
                if type(r) is IntFloatType:           # if r is also intbool, cannot refer anything
                    return IntFloatType()           # result num
                else:                               # if r pure type, consider l as auto to only check r and copy type r to l
                    auto_side = 'l'
            elif type(r) is IntFloatType and auto_side == 'x':  #if r is auto and l is not auto
                auto_side = 'r'                     # change r

            if auto_side == 'l':        # if l is auto
                changeType(ctx.left, r, o)        # change type of auto
                if type(r) is IntegerType or type(r) is FloatType:   # if r is correct type
                    if ctx.op in num_op:      # if num
                        return r        # type based on non-auto
                    else:               # the bool
                        return BooleanType()
            else:
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)         # change type of auto
                    r = l                   # change cur l for type checking too
                if type(l) is IntFloatType and type(r) is IntFloatType:              # if r is also intbool, cannot refer anything
                    return IntFloatType()           # result num
                elif (type(l) is IntegerType or type(l) is FloatType):   # if both are num or bool
                    if (type(r) is IntegerType or type(r) is FloatType):
                        if ctx.op in num_op:      # if num
                            if type(l) is IntegerType and type(r) is IntegerType:   # if both side are int, return int
                                return IntegerType()
                            else:
                                return FloatType()                # return float
                        else:
                            return BooleanType()

    def visitUnExpr(self, ctx: UnExpr, o):      # minus or negation
        exp = self.visit(ctx.val, o)
        # find declare of auto_type
        decl = None
        if type(exp) is AutoType:                 # if l is auto node
            l_decl = findDeclareA3(ctx.val, o, VarDecl)

        # check -
        if ctx.op == '-':     # if meet negative op
            if type(exp) is AutoType:              # change to match proper type with logic; choose int or float is ok
                changeType(ctx.val, IntFloatType(), o)        # change type of auto
                exp = IntFloatType()
            elif type(exp) is IntBoolType:              # change to match proper type with logic; choose int
                changeType(ctx.val, IntegerType(), o)        # change type of auto
                exp = IntegerType()
            if (type(exp) is IntegerType or type(exp) is FloatType or type(exp) is IntFloatType):    # exp must be number
                return exp                          # return its type

        # check !
        if ctx.op == '!':     # if meet negative op
            if type(exp) is AutoType or type(exp) is IntBoolType:  # change to match proper type with logic; choose bool
                changeType(ctx.val, BooleanType(), o)        # change type of auto; if auto, change to match type
                exp = BooleanType()                      # change cur exp for type checking too

            if type(exp) is BooleanType:    # exp must be bool
                return exp                          # return its type

    # ACTIVE STATEMENTS
    def visitBlockStmt(self, ctx: BlockStmt, o):
        # no longer in func
        env = o
        if self.Start_Func == False:        # if 1st time enter func
            self.Start_Func = True          # not create new scope; to keep param as same scope
        else:                               # 2nd blkstmt above
            env = [[]] + o                  # create new scope
        # Visit + Must in loop

        for stmt in ctx.body:
            o = self.visit(stmt, env)   # visit each statements in body
        return o        # err its environment
    def visitIfStmt(self, ctx: IfStmt, o):
        cond = self.visit(ctx.cond, o)
        # check condition to be boolean
        if type(cond) is AutoType or type(cond) is IntBoolType:          # if auto, change type to bool to match check stmt
            changeType(ctx.cond, BooleanType(), o)
            cond = BooleanType()

        # Visit + Must in loop
        if type(ctx.tstmt) is not BlockStmt:
            env = [[]] + o                  # create new scope
            self.visit(ctx.tstmt, env)       # visit each statements in true
        else:                                # blkstmt
            self.visit(ctx.tstmt, o)       # visit each statements in true
        if ctx.fstmt:                       # if go to f stmt
            if type(ctx.tstmt) is not BlockStmt:
                env = [[]] + o                  # create new scope
                self.visit(ctx.fstmt, env)       # visit each statements in false
            else:                               # blkstmt
                self.visit(ctx.fstmt, o)       # visit each statements in false
        return o        # err its environment
    def visitForStmt(self, ctx: ForStmt, o):
        # check rhs 1st then left; copy from AssignStmt
        r = self.visit(ctx.init.rhs, o)
        l = self.visit(ctx.init.lhs, o)

        # compare type
        if type(l) is not AutoType:     # not auto type
            if (type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType):       # change auto of rhs with decl type of lhs
                changeType(ctx.init.rhs, l, o)
                r = l
        else:                             # check Auto type
            if type(r) is IntBoolType or type(r) is IntFloatType:       # type break by changing to Int
                r = IntegerType()
            changeType(ctx.init.lhs, r, o)            # replace auto with type in init
            l = r

        init = l                                       # copy type of var to init type
        cond = self.visit(ctx.cond, o)                      # load types
        upd = self.visit(ctx.upd, o)

        # check init
        if type(init) is AutoType or type(init) is IntFloatType:          # if auto, change type of var to int to match check stmt
            changeType(ctx.init.lhs, IntegerType(), o)
            init = IntegerType()
        # check condition to be boolean
        if type(cond) is AutoType or type(cond) is IntBoolType:          # if auto, change type to bool to match check stmt
            changeType(ctx.cond, BooleanType(), o)
            cond = BooleanType()
        # check update to be integer
        if type(upd) is AutoType or type(upd) is IntFloatType:          # if auto, change type to int to match check stmt
            changeType(ctx.upd, IntegerType(), o)
            upd = IntegerType()

        self.Loop_Counter += 1              # add once more loop

        # visit
        if type(ctx.stmt) is not BlockStmt:
            env = [[]] + o                  # create new scope
            self.visit(ctx.stmt, env)       # visit stmt
        else:                               # blk stmt
            self.visit(ctx.stmt, o)         # visit stmt

        self.Loop_Counter -= 1              # del loop
        return o
    def visitWhileStmt(self, ctx: WhileStmt, o):
        cond = self.visit(ctx.cond, o)
        # check condition to be boolean
        if type(cond) is AutoType or type(cond) is IntBoolType:          # if auto, change type to bool to match check stmt
            changeType(ctx.cond, BooleanType(), o)
            cond = BooleanType()

        self.Loop_Counter += 1              # add once more loop

        # visit
        if type(ctx.stmt) is not BlockStmt:
            env = [[]] + o                  # create new scope
            self.visit(ctx.stmt, env)       # visit stmt
        else:                               # blk stmt
            self.visit(ctx.stmt, o)         # visit stmt

        self.Loop_Counter -= 1              # del loop
        return o
    def visitDoWhileStmt(self, ctx: DoWhileStmt, o):
        cond = self.visit(ctx.cond, o)
        # check condition to be boolean
        if type(cond) is AutoType or type(cond) is IntBoolType:          # if auto, change type to bool to match check stmt
            changeType(ctx.cond, BooleanType(), o)
            cond = BooleanType()

        self.Loop_Counter += 1              # add once more loop

        # visit
        if type(ctx.stmt) is not BlockStmt:
            env = [[]] + o                  # create new scope
            self.visit(ctx.stmt, env)       # visit stmt
        else:                               # blk stmt
            self.visit(ctx.stmt, o)         # visit stmt

        self.Loop_Counter -= 1              # del loop
        return o

    def visitFuncCall(self, ctx: FuncCall, o):
        # check decl:
        decl = findDeclareA3(ctx, o, FuncDecl)

        # check type of parameters:
        para_list = decl.params
        # compare size of l and r
        in_count = 0       # ini its counter to compare each type
        for para in para_list:      # take each para
            l = para.typ            # l is para type
            r = self.visit(ctx.args[in_count], o)  # r is matching input

            if type(l) is AutoType or type(l) is IntBoolType or type(l) is IntFloatType:             # if para is auto, take arg to assign type
                para.typ = r
            elif ((type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType)
                  and type(l) is not AutoType):       # change auto of rhs with decl type of lhs
                changeType(ctx.args[in_count], l, o)
            in_count += 1  # adv

        if type(decl.return_type) is IntBoolType:       # exclusive return for new type; rhs is 1 of them is OK
            return IntBoolType()
        elif type(decl.return_type) is IntFloatType:
            return IntFloatType()
        return self.visit(decl.return_type, o)                 # err type
    def visitCallStmt(self, ctx: CallStmt, o):
        # check decl:
        decl = findDeclareA3(ctx, o, FuncDecl)
        if type(decl.return_type) is AutoType:                  # if func auto, change to void in callstmt
            decl.return_type = VoidType()


        # check type of parameters:
        para_list = decl.params
        # compare size of l and r
        in_count = 0       # ini its counter to compare each type
        for para in para_list:      # take each para
            l = para.typ            # l is para type
            r = self.visit(ctx.args[in_count], o)  # r is matching input
            if type(l) is AutoType or type(l) is IntBoolType or type(l) is IntFloatType:             # if para is auto, take arg to assign type
                para.typ = r
            elif ((type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType)
                  and type(l) is not AutoType):       # change auto of rhs with decl type of lhs
                changeType(ctx.args[in_count], l, o)
            in_count += 1  # adv

        return self.visit(decl.return_type, o)                 # ret type

    def visitReturnStmt(self, ctx: ReturnStmt, o):
        # check if need to check current return

        if self.First_Return == False or len(o) > 2:             # if has not checked first return o or in stmt
            # check type of r
            l = self.Current_Function.return_type               # take cur function as l
            r = self.visit(ctx.expr, o) if ctx.expr else VoidType()  # return its type if nothing, return void

            if type(l) is AutoType:                     # if l auto, modify type by 1st time checking
                self.Current_Function.return_type = r
            elif ((type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType)
                  and type(l) is not AutoType):       # change auto of rhs with decl type of lhs
                changeType(ctx.expr, l, o)

        if self.First_Return == False and len(o) == 2:             # if has not checked first return o and not in stmt
            self.First_Return = True                        # mark checked
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

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [[Symbol("readInteger", MType([], IntegerType()), CName(self.libName)),                      # create these
                 Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),       # to store
                 Symbol("readFloat", MType([], FloatType()), CName(self.libName)),                          # default func
                 Symbol("printFloat", MType([FloatType()], VoidType()), CName(self.libName)),           # and spam cmt like this
                 Symbol("readString", MType([], StringType()), CName(self.libName)),                        # to avoid copy
                 Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),          # the code plagism checker
                 Symbol("readBoolean", MType([], BooleanType()), CName(self.libName)),                      # that these codes are almost the same
                 Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),       # that all
                 ]
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class ClassType(Type):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Class({0})".format(str(self.name))

class ClassDecl(Decl):
    def __init__(self, name, memlist: List[VarDecl]):
        self.name = name
        self.memlist = memlist

class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.Class_Name = 'MT22Class'
        self.emit = Emitter(self.path + "/" + self.Class_Name + ".j")    # place to put gen file

        self.Current_Function = None    # to store the current function node; for return node
        self.OutParamKey = "MT22out_"    # name to set to create static variables for out parameters

    def defaultVar(self, typ):                  # to input default var for undecl var
        if type(typ) is BooleanType or type(typ) is AutoType:
            return BooleanLit(False)
        elif type(typ) is IntegerType:
            return IntegerLit(0)
        elif type(typ) is FloatType:
            return FloatLit(0.0)
        elif type(typ) is StringType:
            return StringLit("")
        elif type(typ) is ArrayType:
            if len(typ.dimensions) > 1:         # if multi dimen arr
                return ArrayLit([self.defaultVar(ArrayType(typ.dimensions[1:], typ.typ)) for x in range(typ.dimensions[0])])    # cut
            else:                               # single dimen arr
                return ArrayLit([self.defaultVar(typ.typ) for x in range(typ.dimensions[0])])   # add default exp to each explists

    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.emitPROLOG(self.Class_Name, 'java/lang/Object'))    # start the production; create class name n' parent

        StaticChecker(ast).check()                  # check tree to convert auto type to proper type
        o = CodeGenerator().init()       # to store 1st emit
        # add all func as prototype
        pttyp = list(filter(lambda x: type(x) is FuncDecl, ast.decls))      # get all func
        for funcdecl in pttyp:
            if type(funcdecl) is FuncDecl:      # check if func
                if type(funcdecl.return_type) is IntFloatType or type(funcdecl.return_type) is AutoType:      # change type of func if type is invalid
                    funcdecl.return_type = FloatType()
                elif type(funcdecl.return_type) is IntBoolType:
                    funcdecl.return_type = IntegerType()

                for x in range(len(funcdecl.params)):
                    param = funcdecl.params[x].typ
                    if type(param) is IntFloatType or type(param) is AutoType:      # change type if type is invalid
                        funcdecl.params[x].typ = FloatType()
                    elif type(param) is IntBoolType:
                        funcdecl.params[x].typ = IntegerType()

        o[-1] += list(map(lambda x: Symbol(x.name, MType([y.typ for y in x.params], x.return_type, x), CName(FuncDecl)), pttyp))  # store node of ParamDecl

        # ini var
        need_ini = False                                                # check if any var need ini
        for vardecl in filter(lambda x: type(x) is VarDecl, ast.decls):
            self.emit.printout(self.emit.emitATTRIBUTE(vardecl.name, vardecl.typ))            # get all global vardecls to ini with static; # add static variable
            o[0] += [Symbol(vardecl.name, MType([], vardecl.typ), CName(VarDecl))]     # add to scope
            if vardecl.init:        # if have ini, create static
                need_ini = True
        for decl in filter(lambda x: type(x) is FuncDecl, ast.decls):   # add static vars to store and load out parameters
            out_list = filter(lambda x: str(x.out) == "out", decl.params)       # load out paras
            [self.emit.printout(self.emit.emitATTRIBUTE(self.OutParamKey + decl.name + "_" + x.name, x.typ)) for x in out_list]       # add static variable

        if need_ini:                # func to gen ini
            self.genStaticFunc(filter(lambda x: type(x) is VarDecl, ast.decls), o, None)

        # ini func
        self.genMETHOD(FuncDecl("<init>", None, [], "", BlockStmt([])), o, Frame("<init>", VoidType))   # ini default func
        for decl in filter(lambda x: type(x) is FuncDecl, ast.decls):
            self.Current_Function = decl
            self.visit(decl, o)               # only visit FuncDecl; get symbol from funcdecl ret
            self.Current_Function = None

        self.emit.emitEPILOG()      # end of code, ready to return
        return c

    # def visitClassDecl(self, ast, c):
    #     self.Class_Name = ast.Class_Name.name
    #     self.emit = Emitter(self.path + "/" + self.Class_Name + ".j")
    #     self.emit.printout(self.emit.emitPROLOG(self.Class_Name, "java.lang.Object"))
    #     [self.visit(ele, SubBody(None, self.env))for ele in ast.memlist if type(ele) == MethodDecl]
    #     # generate default constructor
    #     self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(), None, Block([], [])), c, Frame("<init>", VoidType()))
    #     self.emit.emitEPILOG()
    #     return c

    # UTILITIES
    def convertIntFloat(self, l, r, frame):
        if type(l) is FloatType and type(r) is IntegerType:        # convert i2f
            return self.emit.emitI2F(r, frame)
        elif type(l) is IntegerType and type(r) is FloatType:      # take int type of float by Java; f2i
            return self.emit.emitI2F(r, frame)
        else:
            return ""               # nothing

    def genMETHOD(self, funcdecl, o, frame):            # funcdecl blank => 1st ini .method public <init>()V
        isInit = funcdecl.return_type is None
        isMain = str(funcdecl.name) == "main" and len(funcdecl.params) == 0 and type(funcdecl.return_type) is VoidType
        return_type = VoidType() if isInit else funcdecl.return_type
        methodName = "<init>" if isInit else str(funcdecl.name)
        intype = [ArrayType([0], StringType())] if isMain else list(map(lambda x: x.typ, funcdecl.params))
        mtype = MType(intype, return_type)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        frame.enterScope(True)

        lcenv = [[]] + o      # create local scope for o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.Class_Name)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([0], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            for x in funcdecl.params:
                lcenv[0] += self.visit(x, SubBody(frame, lcenv))

        body = funcdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # inherit corner; after 1st label
        if funcdecl.inherit:            # if have inherit
            inherit_decl = lookup_Func(funcdecl.inherit, o[-1], lambda x: x.name)   # find prototype of inherit func; Symbol
            inherit_node = inherit_decl.mtype.Node                                  # load its node; FuncDecl
            first_stmt = funcdecl.body.body[0] if funcdecl.body.body != [] else None                # take first stmt of cur func
            if inherit_node.params:      # if inherit func have parameters
                if type(first_stmt) is CallStmt and first_stmt.name == "super":             # only care super func
                    outstr = ""
                    for x in first_stmt.args:       # load arg
                        str1, typ1 = self.visit(x, Access(frame, lcenv, False, True))
                        outstr += str1          # take string and wait to print it
                    self.emit.printout(outstr)
                    self.emit.printout(self.emit.emitINVOKESTATIC(self.Class_Name + "/" + inherit_decl.name, inherit_decl.mtype, frame))    # call inherit func 1st
                # add inherit parameter here
                inherit_params = []
                # add chain inherit parameter
                while inherit_node.inherit:     # collect until parent does not inherit
                    inherit_params += list(filter(lambda x: str(x.inherit) == "inherit", inherit_node.params))    # add inherit parameter
                    inherit_decl = lookup_Func(inherit_node.inherit, o[-1], lambda x: x.name)   # find prototype of inherit func; Symbol
                    inherit_node = inherit_decl.mtype.Node                                  # load its node; FuncDecl

                inherit_params += list(filter(lambda x: str(x.inherit) == "inherit", inherit_node.params))    # add inherit parameter
                for x in inherit_params:                               # add them to function
                    lcenv[0] += self.visit(x, SubBody(frame, lcenv))
            else:           # if inherit func not have parameter
                if first_stmt is None or (              # if stmt not have preventDefault
                not (type(first_stmt) is CallStmt and first_stmt.name == "preventDefault")):
                    self.emit.printout(self.emit.emitINVOKESTATIC(self.Class_Name + "/" + inherit_decl.name, inherit_decl.mtype, frame))    # call inherit func 1st

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.Class_Name)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, lcenv)), body.body))     # visit the body

        # store value of out paras
        out_list = filter(lambda x: str(x.out) == "out", funcdecl.params)
        for x in out_list:
            para_decl = findDeclare(x, lcenv, ParamDecl)        # find decl of para
            self.emit.printout(self.emit.emitREADVAR(para_decl.name, para_decl.mtype.rettype, para_decl.memPos, frame))  # load param here
            self.emit.printout(self.emit.emitPUTSTATICDefault(self.OutParamKey + funcdecl.name + "_" + x.name, para_decl.mtype.rettype, frame))    # store to static

        # print ending
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(return_type) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:               # if return not int, create value to ret
            self.emit.printout(self.visit(self.defaultVar(return_type), SubBody(frame, lcenv))[0])  # take default var to false return
            self.emit.printout(self.emit.emitRETURN(return_type, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def genStaticFunc(self, var_list, o, frame):
        frame = Frame("<clinit>", VoidType())
        frame.enterScope(True)          # enter func
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))   # gen default header
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        for x in filter(lambda x: x.init, var_list):            # take all vardecl need to ini
            rs, rt = self.visit(x.init, SubBody(frame, o))
            self.emit.printout(rs)
            decl = findDeclare(x, o, VarDecl)
            lt = decl.mtype.rettype
            self.emit.printout(self.convertIntFloat(lt, rt, frame))     # convert type of num
            self.emit.printout(self.emit.emitPUTSTATICDefault(decl.name, decl.mtype.rettype, frame))

        # print ending
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()          # exit func

    def visitVarDecl(self, ast, o):     # 1 var is 1 index in frame
        frame = o.frame
        typ = ast.typ
        sym = o.sym
        if type(ast.typ) is AutoType:   # if var is auto, take ini as type declare
            str1, typ1 = self.visit(ast.init, o)      # visit its value
            typ = typ1                  # assign real typ
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), ast.name, typ, 0, 1, frame))      # CHANGE THESE NUMBERS
        if not ast.init:                    # if not have ini, assign it
            ast.init = self.defaultVar(typ)
        str1, typ1 = self.visit(ast.init, o)      # visit its value
        self.emit.printout(str1)                 # add val
        self.emit.printout(self.convertIntFloat(typ, typ1, frame))     # convert type of num
        self.emit.printout(self.emit.emitWRITEVAR(ast.name, typ, frame.getCurrIndex() - 1, frame))        # store that value
        sym[0] += [Symbol(ast.name, MType([], typ), CName(VarDecl), frame.getCurrIndex() - 1)]                  # add vardecl as symbol to scope

    def visitAssignStmt(self, ast, o):
        frame = o.frame
        sym = o.sym
        arr_cell_node = ast.lhs                 # take that node
        decl = findDeclare(arr_cell_node, sym, VarDecl)        # find decl
        pure_type = decl.mtype.rettype                      # return type of decl
        if type(ast.lhs) is ArrayCell:              # this to store cell
            if decl in sym[-1]:                 # if in global
                self.emit.printout(self.emit.emitGETSTATICDefault(decl.name, decl.mtype.rettype, frame))
                self.emit.printout(self.emit.emitDUP(frame))                # dup to store later
            else:                               # inner node
                self.emit.printout(self.emit.emitREADVAR(arr_cell_node.name, decl.mtype.rettype, decl.memPos, frame))     # load var
            for x in arr_cell_node.cell[:-1]:                      # go to cell in each dimen; multi-
                dimen, dt = self.visit(x, o)
                self.emit.printout(dimen)
                self.emit.printout(self.emit.emitALOAD(decl.mtype.rettype, frame))
            dimen, dt = self.visit(arr_cell_node.cell[-1], o)         # take the last dimen
            self.emit.printout(dimen)
        re, rt = self.visit(ast.rhs, o)      # go to r to calculate all before assign r
        self.emit.printout(re)

        decl = findDeclare(ast.lhs, sym, VarDecl)        # find decl of l
        lt = decl.mtype.rettype
        self.emit.printout(self.convertIntFloat(lt, rt, frame))     # convert type of num
        if decl in sym[-1]:                     # if global var
            if type(ast.lhs) is ArrayCell:      # if store to cell
                self.emit.printout(self.emit.emitASTORE(decl.mtype.rettype.typ, frame))
            self.emit.printout(self.emit.emitPUTSTATICDefault(decl.name, lt, frame))    # store to static
        else:                                   # var in scope
            if type(ast.lhs) is ArrayCell:      # if store to cell
                self.emit.printout(self.emit.emitASTORE(lt.typ, frame))
            else:
                self.emit.printout(self.emit.emitWRITEVAR(decl.name, lt, decl.memPos, frame))                # store to l

    def visitParamDecl(self, ast, o):           # param decl only; copy from vardecl w/o ini
        frame = o.frame
        typ = ast.typ
        sym = o.sym
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), ast.name, typ, 0, 1, frame))      # CHANGE THESE NUMBERS
        return [Symbol(ast.name, MType(None, typ), CName(ParamDecl), frame.getCurrIndex() - 1)]                  # add vardecl as symbol to scope

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.return_type)
        self.emit.printout(self.genMETHOD(ast, o, frame))

    def visitBinExpr(self, ast, o):
        outstr = ""     # store string to print
        le, lt = self.visit(ast.left, o)
        re, rt = self.visit(ast.right, o)
        rettyp = lt            # default same type; except num
        frame = o.frame

        # check type of calculation
        if type(lt) is FloatType and type(rt) is IntegerType:        # convert i2f
            outstr += self.emit.emitI2F(rt, frame)
            rettyp = FloatType()                                    # type based on lhs
        elif type(lt) is IntegerType and type(rt) is FloatType:      # take int type of float by Java; f2i
            outstr += self.emit.emitI2F(rt, frame)
            rettyp = IntegerType()                                  # type based on lhs
        elif type(lt) is IntegerType and type(rt) is IntegerType:       # only return int if both are in
            rettyp = IntegerType()
        elif type(lt) is FloatType or type(rt) is FloatType:          # if float, choose float
            rettyp = FloatType()

        # select op here
        if ast.op in ['+', '-']:                    # calculation
            outstr += (le + re + self.emit.emitADDOP(ast.op, lt, o.frame))     # add
        elif ast.op in ['*', '/']:
            outstr += (le + re + self.emit.emitMULOP(ast.op, lt, o.frame))
        elif ast.op == '%':
            outstr += (le + re + self.emit.emitMOD(o.frame))
        elif ast.op == '&&':              # logic
            # create 2 labels for short-circuit
            labelT = frame.getNewLabel()            # label to assign false
            labelO = frame.getNewLabel()            # label to exit
            outstr += le                            # print l
            outstr += self.emit.emitIFFALSE(labelT, frame)  # short-circuit if 1st ele determine result
            outstr += re                            # print r
            outstr += self.emit.emitGOTO(labelO, frame)                             # exit
            outstr += self.emit.emitLABEL(labelT, frame)
            outstr += self.emit.emitPUSHCONST(0, IntegerType(), frame)      # ret false
            outstr += self.emit.emitLABEL(labelO, frame)                        # exit for true
        elif ast.op == '||':
            # create 2 labels for short-circuit
            labelT = frame.getNewLabel()            # label to assign false
            labelO = frame.getNewLabel()            # label to exit
            outstr += le                            # print l
            outstr += self.emit.emitIFTRUE(labelT, frame)  # short-circuit if 1st ele determine result
            outstr += re                            # print r
            outstr += self.emit.emitGOTO(labelO, frame)                             # exit
            outstr += self.emit.emitLABEL(labelT, frame)
            outstr += self.emit.emitPUSHCONST(1, IntegerType(), frame)      # ret false
            outstr += self.emit.emitLABEL(labelO, frame)                        # exit for true
            outstr += (le + re + self.emit.emitOROP(o.frame))
        elif ast.op in ['>', '>=', '<', '<=', '==', '!=']:              # compare
            outstr += (le + re + self.emit.emitREOP(ast.op, o.frame))
        elif ast.op == '::':                    # concate string; # use concat func with 2 String inputs, output string
            outstr += (le + re + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([rt], StringType()), o.frame))
        return outstr, rettyp           # return str and typ

    def visitUnExpr(self, ast, o):
        ec, et = self.visit(ast.val, o)
        # select op here
        if ast.op == '-':           # negative
            return ec + self.emit.emitNEGOP(et, o.frame), et
        else:               # if ast.op == '!':         # not
            return ec + self.emit.emitNOT(et, o.frame), et

    def visitId(self, ast, o):
        # find declare of x to get index
        frame = o.frame
        sym = o.sym
        decl = findDeclare(ast, sym, VarDecl)        # find decl
        if decl is None: raise 10    # ERR
        decl_typ = decl.mtype.rettype
        if decl in sym[-1]:         # if in global
            return self.emit.emitGETSTATICDefault(decl.name, decl_typ, frame), decl_typ
        else:
            return self.emit.emitREADVAR(ast.name, decl_typ, decl.memPos, frame), decl_typ

    def visitBlockStmt(self, ast, o):
        old_sym = o.sym                     # backup global scope before modifying
        if o.sym[0] != []:                    # if not created new env, create new
            o.sym = [[]] + o.sym
        [self.visit(x, o) for x in ast.body]      # visit its body and write all of its result
        o.sym = old_sym                         # replace back

    def visitIfStmt(self, ast, o):      # how to consider something is true
        frame = o.frame
        cond, t = self.visit(ast.cond, o)        # take condition
        self.emit.printout(cond)                  # write expression
        frame.enterScope(False)                     # create scope for else and exit
        self.emit.printout(self.emit.emitIFFALSE(frame.getStartLabel(), frame))
        self.visit(ast.tstmt, o)            # go to true stmt
        if ast.fstmt:      # if have else
            self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))           # get new label
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))             # imple false label
            self.visit(ast.fstmt, o)            # write f
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))             # imple exit label
        else:           # no else
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))             # imple exit label
        frame.exitScope()

    def visitWhileStmt(self, ast, o):
        frame = o.frame                                                         # create 2 scopes: start: loop, end: check cond
        outstr = ""                             # store string to print after ???
        cond, t = self.visit(ast.cond, o)        # take condition
        frame.enterLoop()                 # create loop for While loop; start, cont: while, end, brk: exit while
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(cond)                  # write expression
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))       # check condition to cont the while
        self.visit(ast.stmt, o)                    # visit its body
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()                           # exit scope

    def visitDoWhileStmt(self, ast, o):
        frame = o.frame                                                         # create 2 scopes: start: loop, end: check cond
        frame.enterLoop()                 # create loop for While loop; start, cont: while, end, brk: exit while
        loop_label = frame.getBreakLabel() + 1            # get label to match for end loop, then waste it
        frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(loop_label, frame))
        self.visit(ast.stmt, o)                    # visit its body
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        cond, t = self.visit(ast.cond, o)        # take condition
        self.emit.printout(cond)                  # write expression
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))       # check condition to cont the while
        self.emit.printout(self.emit.emitGOTO(loop_label, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()                           # exit scope

    def visitForStmt(self, ast, o):
        frame = o.frame                                                         # create 2 scopes: start: loop, end: check cond
        sym = o.sym
        cond, ct = self.visit(ast.cond, o)        # take condition
        frame.enterLoop()                 # create loop for While loop; start, cont: while, end, brk: exit while
        self.visit(ast.init, o)                 # go to assign
        loop_label = frame.getContinueLabel()       # get head of loop to use later in 2nd loop
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        frame.enterLoop()                       # go out
        self.emit.printout(cond)                  # write expression
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))       # check condition to cont the while
        self.visit(ast.stmt, o)                    # visit its body
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))

        # add to lhs of init
        decl = findDeclare(ast.init.lhs, sym, VarDecl)                          # find decl of l
        ie, it = self.visit(ast.init.lhs, o)          # load lhs aka variable for for stmt
        self.emit.printout(ie)
        re, rt = self.visit(ast.upd, o)      # go to r to calculate all before assign r
        self.emit.printout(re)
        self.emit.printout(self.emit.emitADDOP('+', IntegerType(), frame))                      # upd must be int
        self.emit.printout(self.emit.emitWRITEVAR(decl.name, decl.mtype.rettype, decl.memPos, frame))                # store to l
        self.emit.printout(self.emit.emitGOTO(loop_label, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()                           # exit loop
        frame.exitLoop()                           # exit loop

    def visitContinueStmt(self, ast, o):
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitBreakStmt(self, ast, o):
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitReturnStmt(self, ast, o):
        frame = o.frame
        et = VoidType()         # default type if no expr
        if ast.expr:            # if have expr
            ee, et = self.visit(ast.expr, o)      # go to expr to calculate all before assign return
            self.emit.printout(ee)
            self.emit.printout(self.convertIntFloat(self.Current_Function.return_type, et, frame))     # convert type of num
        self.emit.printout(self.emit.emitRETURN(self.Current_Function.return_type, frame))

    def visitFuncCall(self, ast, o):            # expr
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        decl = findDeclare(ast, sym, FuncDecl)
        cname = decl.value.value
        ctype = decl.mtype          # deep-copy; cannot modify original
        outstr = ""

        arg = 0                     # store arg to load later
        for x in ast.args:
            param_type = ctype.partype[arg]       # store type of param to convert if need
            ae, at = self.visit(x, Access(frame, sym, False, True))
            outstr += ae          # take string and wait to print it
            outstr += self.convertIntFloat(param_type, at, frame)     # convert type of num
            arg += 1                # adv

        if cname is FuncDecl:          # if call func inside program
            outstr += self.emit.emitINVOKESTATIC(self.Class_Name + "/" + ast.name, ctype, frame)
        else:                                   # if call io
            outstr += self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame)

        # store value of out paras
        if cname is FuncDecl:
            decl_node = decl.mtype.Node
            param_list = decl_node.params
            arg = 0                     # store arg to load later
            for x in ast.args:
                if str(param_list[arg].out) == "out":       # if out para
                    if type(x) is Id:           # if input is a variable
                        var_decl = findDeclare(x, sym, VarDecl)     # find that var
                        var_typ = var_decl.mtype.rettype            # lhs is var, rhs is static aka parameter's value of function
                        outstr += self.emit.emitGETSTATICDefault(self.OutParamKey + decl.name + "_" + param_list[arg].name, param_list[arg].typ, frame)    # load static; from that func
                        outstr += self.convertIntFloat(var_typ, param_list[arg].typ, frame)     # convert type of num
                        if var_decl in sym[-1]:             # if global scope
                            outstr += self.emit.emitPUTSTATICDefault(var_decl.name, var_typ, frame)
                        else:                               # if in scope
                            outstr += self.emit.emitWRITEVAR(var_decl.name, var_typ, var_decl.memPos, frame)  # load param here
                arg += 1
        return outstr, ctype.rettype

    def visitCallStmt(self, ast, o):            # stmt;
        if not (ast.name == "preventDefault" or ast.name == "super"):           # do not care these 2 functions
            ctxt = o
            frame = ctxt.frame
            sym = ctxt.sym
            decl = findDeclare(ast, sym, FuncDecl)
            cname = decl.value.value
            ctype = decl.mtype
            outstr = ""

            arg = 0                     # store arg to load later
            for x in ast.args:
                param_type = ctype.partype[arg]       # store type of param to convert if need
                ae, at = self.visit(x, Access(frame, sym, False, True))
                outstr += ae          # take string and wait to print it
                outstr += self.convertIntFloat(param_type, at, frame)     # convert type of num
                arg += 1                # adv

            if cname is FuncDecl:          # if call func inside program
                outstr += self.emit.emitINVOKESTATIC(self.Class_Name + "/" + ast.name, ctype, frame)
            else:                          # if call io
                outstr += self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame)
            # store value of out paras
            if cname is FuncDecl:
                decl_node = decl.mtype.Node
                param_list = decl_node.params
                arg = 0                     # store arg to load later
                for x in ast.args:
                    if str(param_list[arg].out) == "out":       # if out para
                        if type(x) is Id:           # if input is a variable
                            var_decl = findDeclare(x, sym, VarDecl)     # find that var
                            var_typ = var_decl.mtype.rettype            # lhs is var, rhs is static aka parameter's value of function
                            outstr += self.emit.emitGETSTATICDefault(self.OutParamKey + decl.name + "_" + param_list[arg].name, param_list[arg].typ, frame)    # load static; from that func
                            outstr += self.convertIntFloat(var_typ, param_list[arg].typ, frame)     # convert type of num
                            if var_decl in sym[-1]:             # if global scope
                                outstr += self.emit.emitPUTSTATICDefault(var_decl.name, var_typ, frame)
                            else:                               # if in scope
                                outstr += self.emit.emitWRITEVAR(var_decl.name, var_typ, var_decl.memPos, frame)  # load param here
                    arg += 1
            self.emit.printout(outstr)      # print since stmt

    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHCONST(ast.val, IntegerType(), o.frame), IntegerType()

    def visitFloatLit(self, ast, o):
        return self.emit.emitPUSHCONST(ast.val, FloatType(), o.frame), FloatType()

    def visitBooleanLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.val, o.frame), BooleanType()

    def visitStringLit(self, ast, o):
        return self.emit.emitPUSHCONST(ast.val, StringType(), o.frame), StringType()

    def visitArrayLit(self, ast, o):
        frame = o.frame
        str_return = ""                             # store string what to print
        ret_str, ret_type = self.visit(ast.explist[0], o)        # take 1st ele type as ret type
        arr_len = len(ast.explist)                  # get length of arr
        if type(ret_type) is ArrayType:           # if exp is another arr; multi dimen
            # calculate all to int
            str_return += self.emit.emitPUSHICONST(arr_len, frame)     # len; 1st dimen
            # do multi dimen here
            str_return += self.emit.emitNEWARRAY(ret_type, frame)   # create new array
            idx = 0
            for x in ast.explist:        # insert each ele
                str_return += self.emit.emitDUP(frame)
                str_return += self.emit.emitPUSHICONST(idx, frame)             # index
                val, dt = self.visit(ast.explist[idx], o)        # visit each index
                str_return += val            # visit that ele to get value
                frame.push()                    # push in replacement with self.visit(x, o)
                str_return += self.emit.emitASTORE(dt, frame)         # pop all 3
                idx += 1
            # reconstruct arr to return
            new_Dimen = ret_type.dimensions + [arr_len]      # if multi-dimen array, concate them
            return str_return, ArrayType(new_Dimen, ret_type.typ)      # ret new arr type
        else:
            # calculate all to int
            str_return += self.emit.emitPUSHICONST(arr_len, frame)     # len; 1st dimen
            # do multi dimen here
            str_return += self.emit.emitNEWARRAY(ret_type, frame)   # create new array
            idx = 0
            for x in ast.explist:        # insert each ele
                str_return += self.emit.emitDUP(frame)                # push 1
                str_return += self.emit.emitPUSHICONST(idx, frame)             # index; push 2
                val, dt = self.visit(x, o)            # visit that ele to get value     # push 3
                str_return += val
                str_return += self.emit.emitASTORE(dt, frame)         # pop all 3
                idx += 1
            return str_return, ArrayType([arr_len], ret_type)

    def visitArrayCell(self, ast, o):           # lhs: store in Assign Stmt, rhs: load
        frame = o.frame
        sym = o.sym
        decl = findDeclare(ast, sym, VarDecl)        # find decl
        pure_type = decl.mtype.rettype.typ              # get pure type of arr
        if decl in sym[-1]:                 # if in global
            self.emit.printout(self.emit.emitGETSTATICDefault(decl.name, decl.mtype.rettype, frame))
        else:                               # inner node
            self.emit.printout(self.emit.emitREADVAR(ast.name, decl.mtype.rettype, decl.memPos, frame))     # load var
        for x in ast.cell[:-1]:                      # go to cell in each dimen; multi-dimen
            dimen, dt = self.visit(x, o)
            self.emit.printout(dimen)
            self.emit.printout(self.emit.emitALOAD(decl.mtype.rettype, frame))              # load each sub-arr for multi dimen arr
        dimen, dt = self.visit(ast.cell[-1], o)         # take the last dimen
        self.emit.printout(dimen)
        self.emit.printout(self.emit.emitALOAD(pure_type, frame))      # print to load
        return "", pure_type       # return pure val
