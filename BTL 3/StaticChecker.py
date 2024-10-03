from Visitor import Visitor
from StaticError import *
from AST import *
from Utils import *

import collections.abc
# This Assignment 3 in PPL is done by K22 with no copy code, rarely do reference, mostly self-done, and not study Vo Tien.

# more type
class IntBoolType(Type):            # type for auto para: can accept both Int and Bool
    def __str__(self):
        return self.__class__.__name__
class IntFloatType(Type):            # type for auto para: can accept both Int and Float
    def __str__(self):
        return self.__class__.__name__

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
    return filter(lambda x: type(x) is name, l)

# DEBUG TOOLS
def printO(o):      # print O to debug
    print("-----")      # to seperate
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
# IMPORTANT FUNC
def type_compare_return(l, r):     # check in return stmt, return the side having errors
    # verify type
    if type(l) is VoidType:     # exception: both Void are allowed in return stmt
        if type(r) is VoidType:     # or l auto r void
            return None
        else:
            return 'r'       # others are OK
    elif type(l) is AutoType:   # l is auto, accept all
        return None       # others are OK
    elif type(r) is AutoType:   # r is auto, accept all
        return None
    elif type(l) is IntBoolType:    # only for func call and ret stmt
        if type(r) is IntegerType or type(r) is BooleanType:
            return None
        else:                       # r diff type
            return 'r'
    elif type(l) is IntFloatType:    # only for func call and ret stmt
        if type(r) is IntegerType or type(r) is FloatType:
            return None
        else:                       # r diff type
            return 'r'
    elif type(r) is IntBoolType:    # only for func call and ret stmt
        if type(l) is IntegerType or type(l) is BooleanType:
            return None
        else:                       # r diff type
            return 'l'
    elif type(r) is IntFloatType:    # only for func call and ret stmt
        if type(l) is IntegerType or type(l) is FloatType:
            return None
        else:                       # r diff type
            return 'l'
    elif type(l) is ArrayType:
        if arr_compare(l, r) is not None:   # if arr has err, always err r
            return 'r'
    elif type(l) is FloatType:      # check num; only int, float, bool, string
        if type(r) is IntegerType or type(r) is FloatType:    # accept both int and float
            return None
        else:
            return 'r'
    else:                       # other types
        if type(l) is type(r):      # only accept same type
            return None
        else:
            return 'r'
def type_compare_stmt(l, r):     # assign stmt compare, return the side having errors
    # verify type
    if type(l) is VoidType:     # invalid l
        return 'l'
    elif type(l) is AutoType:   # l is auto, accept all
        if type(r) is VoidType:     # r cannot void
            return 'r'
        else:
            return None       # others are OK
    elif type(r) is AutoType:   # r is auto, accept all
        return None
    elif type(l) is IntBoolType:    # only for func call and ret stmt
        if type(r) is IntegerType or type(r) is BooleanType:
            return None
        else:                       # r diff type
            return 'r'
    elif type(l) is IntFloatType:    # only for func call and ret stmt
        if type(r) is IntegerType or type(r) is FloatType:
            return None
        else:                       # r diff type
            return 'r'
    elif type(r) is IntBoolType:    # only for func call and ret stmt
        if type(l) is IntegerType or type(l) is BooleanType:
            return None
        else:                       # r diff type
            return 'l'
    elif type(r) is IntFloatType:    # only for func call and ret stmt
        if type(l) is IntegerType or type(l) is FloatType:
            return None
        else:                       # r diff type
            return 'l'
    elif type(l) is ArrayType:
        if arr_compare(l, r) is not None:   # if arr has err, always err r
            return 'r'
    elif type(l) is FloatType:      # check num; only int, float, bool, string
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
        if l.dimensions == []:          # if l is null arr
            return 'l'
        elif r.dimensions == []:          # if r is null arr
            return 'r'
        elif l.dimensions[0] == r.dimensions[0]:          # if same first dimen list
            if len(l.dimensions) > 1 and len(r.dimensions) > 1:     # if have >1 ele
                # REWORK THIS TO CHANGE L, R TO ARRAY TYPE
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

def findDeclare(node, env, typ: VarDecl or ParamDecl or FuncDecl = None):
    name = node.name
    if typ is VarDecl or typ is ParamDecl:
        for scope in env:       # check each scopes from in to out
            result = lookup_Var_Param(name, scope, lambda x: x.name)
            if result is not None:          # has found declared
                return result
        return None
    elif typ is FuncDecl:   # Func
        result = lookup_Func(name, env[-1], lambda x: x.name)          # find in outside scope
        if result is not None:          # has found declared
            return result
    else:               # whatever type
        for scope in env:       # check each scopes from in to out
            result = lookup(name, scope, lambda x: x.name)
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
                    for x in range(node):
                        compare_node = o[0][x]
                        if compare_node.name == outfunc.name:  # if found same name
                            raise Redeclared(Variable(), compare_node.name)    # err
                    if loop == 0:               # add only in 1st loop
                        o[0].insert(node, outfunc)              # insert the vardecl back to global

                elif type(outfunc) == FuncDecl:      # if func
                    for x in range(node):                  # if func
                        compare_node = o[0][x]
                        if compare_node.name == outfunc.name:  # if found same name
                            raise Redeclared(Function(), compare_node.name)    # err

                if loop == 1:                          # only check in 2nd loop, when all type are inferred
                    # No Entry Point
                    if (type(outfunc) == FuncDecl       # if a function
                            and outfunc.name == "main"          # name main
                            and outfunc.params == []          # no paras
                            and (type(outfunc.return_type) == VoidType or type(outfunc.return_type) == AutoType) # and return Type; visit all and no return stmt to replace type
                    ):
                        if outfunc.inherit is not None:     # if have inherit
                            decl = findDeclare(Id(outfunc.inherit), o, FuncDecl)    # check declare inherit
                            inherit_list = self.visit(decl, o)
                            if inherit_list == []:              # if have no inherit param
                                self.No_Entry_Point = False     # accept this main funcs
                        else:
                            self.No_Entry_Point = False     # since found the main function

                self.Current_Function = outfunc     # store cur func data
                self.First_Return = False
                o = self.visit(outfunc, o)             # visit each node
                self.Current_Function = None        # no longer in func
                self.Start_Func = False             # no longer in func
                self.First_Stmt = None              # no longer in func
                node += 1           # adv
        # done all check
        if self.No_Entry_Point == True: raise NoEntryPoint()                # no proper main function
        #return None     # success w/o errors

    def visitId(self, ctx: Id, o):          # visit if the ID has been declared
        result = findDeclare(ctx, o, VarDecl)
        if result is not None:          # has found declared
            return result.typ               # return its type
        raise Undeclared(Identifier(), ctx.name)  # declare unfound

    def visitArrayCell(self, ctx: ArrayCell, o):
        # load decl
        decl = findDeclare(ctx, o, VarDecl)
        if decl is None:        # if not decl
            raise Undeclared(Identifier(), ctx.name)

        # check type
        node_type = decl.typ      # take its type
        if type(node_type) is not ArrayType:                     # variable is not array, raise all node
            raise TypeMismatchInExpression(ctx)

        # check input is int
        for x in ctx.cell:
            x_typ = self.visit(x, o)                        # take pure type
            if type(x_typ) is AutoType or type(x_typ) is IntBoolType or type(x_typ) is IntFloatType:    # change auto to int
                changeType(x, IntegerType(), o)
                x_typ = IntegerType()
            elif type(x_typ) is not IntegerType:                  # if not int, raise
                raise TypeMismatchInExpression(ctx)         # raise err in this argument; consider as a funcall with RHS is int

        if len(ctx.cell) > len(node_type.dimensions):   # if cell has more dimen
            raise TypeMismatchInExpression(ctx)         # raise err in this node
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
                    if type_compare_stmt(first_type, cur_type):         # mainly check auto
                        raise IllegalArrayLiteral(self.Full_Array_Lit)
                    if type(cur_type) is AutoType or type(cur_type) is IntBoolType or type(cur_type) is IntFloatType:          # if auto type, change that ele to match the whole arr
                        changeType(x, first_type, o)
                    elif type(cur_type) is type(first_type):     # if one type has diff type from the first; MUST MATCH FULL TYPE
                        raise IllegalArrayLiteral(self.Full_Array_Lit)    # raise err for the whole arr
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
        if len(o) > 1:      # if not in global; skip global since already ini
            if lookup_Var_Param(ctx.name, o[0], lambda x: x.name):
                raise Redeclared(Variable(), ctx.name)

        if ctx.init is not None:            # compare type if have ini
            l = ctx.typ                     # only take type, l 1st
            r = self.visit(ctx.init, o)
            err = type_compare_stmt(l, r)   # compare lhs with rhs
            if err is not None:
                raise TypeMismatchInVarDecl(ctx)
            if ((type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType)
                    and type(l) is not AutoType):       # change auto of rhs with decl type of lhs
                changeType(ctx.init, l, o)

        # check Auto type
        if type(ctx.typ) is AutoType:
            # Invalid auto
            if ctx.init is None:
                raise Invalid(Variable(), ctx.name)
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
                decl = findDeclare(Id(ctx.inherit), o, FuncDecl)    # check declare inherit
                if decl is None:        # if not decl inherit func
                    raise Undeclared(Function(), ctx.inherit)

                # add inherit params to scope via visit
                inherit_list += self.visit(decl, o)

                # add inherit param before checking 1st stmt; DO NOT CHANGE POS
                for para in inherit_list:
                    decl_parm = lookup_Var_Param(para.name, env[0], lambda x: x.name)    # check declare in local func scope
                    if decl_parm is None:        # if not decl inherit func
                        env[0] += [para]       # add to list
                    else:                   # redeclared inherit para
                        raise Invalid(Parameter(), para.name)

                # check type of parameters of inherit:
                para_list = decl.params
                if para_list == []:     # if have no parameter
                    if (type(self.First_Stmt) is CallStmt and self.First_Stmt.name == "preventDefault" # if 1st func is prevent
                            and self.First_Stmt.args):
                        raise TypeMismatchInExpression(self.First_Stmt.args[0])
                    elif (type(self.First_Stmt) is CallStmt and self.First_Stmt.name == "super"
                          and self.First_Stmt.args): # if 1st func is super with args, raise like super
                        raise TypeMismatchInExpression(self.First_Stmt.args[0])
                else:   # if have parameters, must have 1st stmt
                    if self.First_Stmt is None:       # if not have 1st stmt
                        raise InvalidStatementInFunction(ctx.name)      # raise err
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
                            else:                   # input < para; overflow
                                raise TypeMismatchInExpression(None)        # raise none
                            err = type_compare_stmt(l, r)       # compare as stmt
                            if err is not None:
                                raise TypeMismatchInExpression(match_input)        # if have any err, always raise current unmatched node
                            if type(l) is AutoType or type(l) is IntBoolType or type(l) is IntFloatType:             # if para is auto, take arg to assign type
                                para.typ = r
                            in_count += 1  # adv
                        # raise err if have
                        if err_arg is not None:
                            raise TypeMismatchInExpression(err_arg)

                    else:   # if 1st func is not super or prevent
                        raise InvalidStatementInFunction(ctx.name)      # raise its name

            else:       # if not inherit, check 1st stmt must not super or prevent
                if (type(self.First_Stmt) is CallStmt
                        and (self.First_Stmt.name == "super" or self.First_Stmt.name == "preventDefault")
                ): # if 1st func is super or prevent, invalid
                    raise InvalidStatementInFunction(ctx.name)

            self.visit(ctx.body, env)             # visit its body
            return o
        else:                               # if not curr func, only visit to get inherit param; NO CHECK ANY ERRORS IN BODY
            for x in ctx.params:
                dup = lookup_Var_Param(x.name, inherit_list, lambda x: x.name)        # check if redecl param in inherit func
                if str(x.inherit) == "inherit" and dup is None:  # add inherit param if unique
                    inherit_list += [x]

            # check inherit later
            if ctx.inherit:     # if inherit
                decl = findDeclare(Id(ctx.inherit), o, FuncDecl)    # check declare inherit; do not raise err if not found

                # add inherit params to scope via visit
                inherit_list_above = self.visit(decl, o) if decl else []            # take param from grandparent func
                for x in inherit_list_above:                        # only add if not already in cur func
                    dup = lookup_Var_Param(x.name, inherit_list, lambda x: x.name)  # check if redecl param in inherit func
                    if dup is None:                                 # add inherit param if unique
                        inherit_list += [x]

            return inherit_list                         # return inherit list to child func
    def visitParamDecl(self, ctx: ParamDecl, o):
        # check redeclare
        if lookup_Var_Param(ctx.name, o[0], lambda x: x.name):
            raise Redeclared(Parameter(), ctx.name)

        o[0] += [ctx]       # add var to current scope
        return o

    def visitAssignStmt(self, ctx: AssignStmt, o):
        # check rhs 1st then left
        r = self.visit(ctx.rhs, o)
        l = self.visit(ctx.lhs, o)

        # compare type
        if type(l) is not AutoType:     # not auto type
            err = type_compare_stmt(l, r) # check type same with vardecl
            if err is not None:
                raise TypeMismatchInStatement(ctx)
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
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx) # unmatch
            else:                       # if l is not auto
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)        # change type of auto
                    r = l                   # change cur l for type checking too
                if type(l) is StringType:
                    if type(r) is StringType:   # if both are string or r is auto
                        return StringType()                             # result string
                    else: # unmatch
                        raise TypeMismatchInExpression(ctx) # unmatch
                else:
                    raise TypeMismatchInExpression(ctx)

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
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx) # unmatch
            else:                       # if l is not auto
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)        # change type of auto
                    r = l                   # change cur l for type checking too
                if type(l) is IntegerType:    # if both are int
                    if type(r) is IntegerType:
                        return IntegerType()
                    else: raise TypeMismatchInExpression(ctx) # unmatch
                else:
                    raise TypeMismatchInExpression(ctx)

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
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx) # unmatch
            else:                       # if l is not auto
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)        # change type of auto
                    r = l                   # change cur l for type checking too
                if type(l) is BooleanType:   # if both are int or bool
                    if type(r) is BooleanType:
                        return BooleanType()
                    else:                                       # unmatch
                        raise TypeMismatchInExpression(ctx)
                else:                                       # unmatch
                    raise TypeMismatchInExpression(ctx)

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
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx) # unmatch
            else:                       # if l is not auto
                if auto_side == 'r':     # if r auto, change to match type
                    changeType(ctx.right, l, o)        # change type of auto
                    r = l                   # change cur l for type checking too
                if (type(l) is IntegerType or type(l) is BooleanType or type(l) is IntBoolType):   # if both are int or bool
                    if (type(r) is IntegerType or type(r) is BooleanType or type(r) is IntBoolType):
                        return BooleanType()
                    else:                                       # unmatch
                        raise TypeMismatchInExpression(ctx)
                else:                                       # unmatch
                    raise TypeMismatchInExpression(ctx)

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
                else:                   # unmatch
                    raise TypeMismatchInExpression(ctx) # unmatch
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
                    else:                                       # unmatch
                        raise TypeMismatchInExpression(ctx)
                else:                                       # unmatch
                    raise TypeMismatchInExpression(ctx)
        print_and_stop(["UNKNOWN TYPE"])

    def visitUnExpr(self, ctx: UnExpr, o):      # minus or negation
        exp = self.visit(ctx.val, o)
        # find declare of auto_type
        decl = None
        if type(exp) is AutoType:                 # if l is auto node
            l_decl = findDeclare(ctx.val, o, VarDecl)

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
            else:
                raise TypeMismatchInExpression(ctx)     # err

        # check !
        if ctx.op == '!':     # if meet negative op
            if type(exp) is AutoType or type(exp) is IntBoolType:  # change to match proper type with logic; choose bool
                changeType(ctx.val, BooleanType(), o)        # change type of auto; if auto, change to match type
                exp = BooleanType()                      # change cur exp for type checking too

            if type(exp) is BooleanType:    # exp must be bool
                return exp                          # return its type
            else:
                raise TypeMismatchInExpression(ctx)     # err

        print_and_stop(["UNKNOWN RETURN"])

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
            if ((type(stmt) == BreakStmt or type(stmt) == ContinueStmt)   # if break or cont is not in for, while
                    and self.Loop_Counter == 0):        # and not indirectly in loop
                raise MustInLoop(stmt)  # err
            o = self.visit(stmt, env)   # visit each statements in body
        return o        # err its environment
    def visitIfStmt(self, ctx: IfStmt, o):
        cond = self.visit(ctx.cond, o)
        # check condition to be boolean
        if type(cond) is AutoType or type(cond) is IntBoolType:          # if auto, change type to bool to match check stmt
            changeType(ctx.cond, BooleanType(), o)
            cond = BooleanType()
        elif type_compare_stmt(BooleanType(), cond):       # if not bool
            raise TypeMismatchInStatement(ctx)    # err

        # Visit + Must in loop
        if ((type(ctx.tstmt) == BreakStmt or type(ctx.tstmt) == ContinueStmt)   # if break or cont is not in for, while
                and self.Loop_Counter == 0):        # and not indirectly in loop
            raise MustInLoop(ctx.tstmt)  # err for true stmt
        if type(ctx.tstmt) is not BlockStmt:
            env = [[]] + o                  # create new scope
            self.visit(ctx.tstmt, env)       # visit each statements in true
        else:                                # blkstmt
            self.visit(ctx.tstmt, o)       # visit each statements in true
        if ctx.fstmt:                       # if go to f stmt
            if ((type(ctx.fstmt) == BreakStmt or type(ctx.fstmt) == ContinueStmt)   # if break or cont is not in for, while
                    and self.Loop_Counter == 0):        # and not indirectly in loop
                raise MustInLoop(ctx.fstmt)  # err for false stmt
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
            err = type_compare_stmt(l, r) # check type same with vardecl
            if err is not None:
                raise TypeMismatchInStatement(ctx)
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
        elif type_compare_stmt(IntegerType(), init):       # if not changed to int
            raise TypeMismatchInStatement(ctx)    # err
        # check condition to be boolean
        if type(cond) is AutoType or type(cond) is IntBoolType:          # if auto, change type to bool to match check stmt
            changeType(ctx.cond, BooleanType(), o)
            cond = BooleanType()
        if type_compare_stmt(BooleanType(), cond):       # if not bool
            raise TypeMismatchInStatement(ctx)    # err
        # check update to be integer
        if type(upd) is AutoType or type(upd) is IntFloatType:          # if auto, change type to int to match check stmt
            changeType(ctx.upd, IntegerType(), o)
            upd = IntegerType()
        if type_compare_stmt(IntegerType(), upd):       # if not changed to int
            raise TypeMismatchInStatement(ctx)    # err

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
        elif type_compare_stmt(BooleanType(), cond):       # if not bool
            raise TypeMismatchInStatement(ctx)    # err

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
        elif type_compare_stmt(BooleanType(), cond):       # if not bool
            raise TypeMismatchInStatement(ctx)    # err

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
        decl = findDeclare(ctx, o, FuncDecl)
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

            if type(l) is AutoType or type(l) is IntBoolType or type(l) is IntFloatType:             # if para is auto, take arg to assign type
                para.typ = r
            elif ((type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType)
                  and type(l) is not AutoType):       # change auto of rhs with decl type of lhs
                changeType(ctx.args[in_count], l, o)          # allow change parameter in funccall
            in_count += 1  # adv

        if type(decl.return_type) is IntBoolType:       # exclusive return for new type; rhs is 1 of them is OK
            return IntBoolType()
        elif type(decl.return_type) is IntFloatType:
            return IntFloatType()
        return self.visit(decl.return_type, o)                 # err type
    def visitCallStmt(self, ctx: CallStmt, o):
        # check super, prevent call func
        if ctx.name == "super" or ctx.name == "preventDefault":     # if func is super or prevent
            if ctx == self.First_Stmt:                          # if 1st stmt
                return                                          # skip
            else:                                               # if in middle, raise invalid stmt
                raise InvalidStatementInFunction(self.Current_Function.name)

        # check decl:
        decl = findDeclare(ctx, o, FuncDecl)
        if decl is None or type(decl) is not FuncDecl:        # if not decl
            raise Undeclared(Function(), ctx.name)
        if type(decl.return_type) is AutoType:                  # if func auto, change to void in callstmt
            decl.return_type = VoidType()


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
            if type(l) is AutoType or type(l) is IntBoolType or type(l) is IntFloatType:             # if para is auto, take arg to assign type
                para.typ = r
            elif ((type(r) is AutoType or type(r) is IntBoolType or type(r) is IntFloatType)
                  and type(l) is not AutoType):       # change auto of rhs with decl type of lhs
                changeType(ctx.args[in_count], l, o)          # allow change parameter in funccall
            in_count += 1  # adv

        return self.visit(decl.return_type, o)                 # ret type

    def visitReturnStmt(self, ctx: ReturnStmt, o):
        # check if need to check current return

        if self.First_Return == False or len(o) > 2:             # if has not checked first return o or in stmt
            # check type of r
            l = self.Current_Function.return_type               # take cur function as l
            r = self.visit(ctx.expr, o) if ctx.expr else VoidType()  # return its type if nothing, return void

            err = type_compare_return(l, r)   # compare 2 types, rhs is expr
            if err is not None:             # if err, always raise r in return
                raise TypeMismatchInStatement(ctx)
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