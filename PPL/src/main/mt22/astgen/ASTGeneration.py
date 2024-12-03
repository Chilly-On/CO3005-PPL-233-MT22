from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *           # copy the AST.py to the same folder astgen

class ASTGeneration(MT22Visitor):
    # program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        if ctx.outfunc():
            return Program(self.visit(ctx.outfunc()))
        else: return Program([])

    def visitOutfunc(self, ctx:MT22Parser.OutfuncContext):
        if ctx.vardclr():
            return self.visit(ctx.vardclr()) + (self.visit(ctx.outfunc()) if ctx.outfunc() else [])
        if ctx.assnstmt():
            return [self.visit(ctx.assnstmt())] + (self.visit(ctx.outfunc()) if ctx.outfunc() else [])
        else:       # stmt
            return [self.visit(ctx.funcdclr())] + (self.visit(ctx.outfunc()) if ctx.outfunc() else [])

    # stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        stmt = self.visit(ctx.stmt())
        if not type(stmt) == list:  # if return other functions as single ele array
            if ctx.stmtlist():      # if have more stmts
                return [stmt] + self.visit(ctx.stmtlist())
            else: return [stmt]     # the only one aka last stmt
        else:   # if return other functions as multi var array like vardclr, adapt it
            if ctx.stmtlist():      # if have more stmts
                return stmt + self.visit(ctx.stmtlist())        # stmt is already list
            else: return stmt     # the only one aka last stmt

    # stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.open_stmt(): return self.visit(ctx.open_stmt())
        else: return self.visit(ctx.closed_stmt())

    # Open_stmt.
    def visitOpen_stmt(self, ctx:MT22Parser.Open_stmtContext):
        if ctx.WHILE():     # while stmt part
            stmt = self.visit(ctx.open_stmt())
            if type(stmt) == list:         # if return array, take the first one
                stmt = stmt[0]
            return WhileStmt(self.visit(ctx.exp()), stmt)
        elif ctx.for_openstmt():        # go to for stmt
            return self.visit(ctx.for_openstmt())
        else:               # if stmt part
            if not ctx.ELSE(): # single if part
                stmt = self.visit(ctx.stmt())
                if type(stmt) == list:         # if return array, take the first one
                    stmt = stmt[0]
                return IfStmt(self.visit(ctx.exp()), stmt)
            else:
                stmt0 = self.visit(ctx.closed_stmt())
                if type(stmt0) == list:         # if return array, take the first one
                    stmt0 = stmt0[0]
                stmt1 = self.visit(ctx.open_stmt())
                if type(stmt1) == list:
                    stmt1 = stmt1[0]
                return IfStmt(self.visit(ctx.exp()), stmt0, stmt1)


    # Closed_stmt.
    def visitClosed_stmt(self, ctx:MT22Parser.Closed_stmtContext):
        if ctx.WHILE():     # while stmt part
            stmt = self.visit(ctx.closed_stmt(0))
            if type(stmt) == list:         # if return array, take the first one
                stmt = stmt[0]
            return WhileStmt(self.visit(ctx.exp()), stmt)
        elif ctx.for_closedstmt():        # go to for stmt
            return self.visit(ctx.for_closedstmt())
        elif ctx.IF():      # if stmt part
            stmt0 = self.visit(ctx.closed_stmt(0))
            if type(stmt0) == list:         # if return array, take the first one
                stmt0 = stmt0[0]
            stmt1 = self.visit(ctx.closed_stmt(1))
            if type(stmt1) == list:
                stmt1 = stmt1[0]     # 1 stmt
            return IfStmt(self.visit(ctx.exp()), stmt0, stmt1)
        else: return self.visit(ctx.basic_stmt())       # basic stmt

    # basic stmt.
    def visitBasic_stmt(self, ctx:MT22Parser.Basic_stmtContext):
        # STMT RETURN ARRAY ELEMENT     FOCUS TO CHANGE IT INTO NON-ARRAY
        if ctx.vardclr(): return self.visit(ctx.vardclr())

        # STMT W/O RETURN ARRAY ELEMENT
        if ctx.assnstmt(): return self.visit(ctx.assnstmt())
        if ctx.dowhstmt(): return self.visit(ctx.dowhstmt())
        if ctx.brkstmt(): return self.visit(ctx.brkstmt())
        if ctx.contstmt(): return self.visit(ctx.contstmt())
        if ctx.rtnstmt(): return self.visit(ctx.rtnstmt())
        if ctx.callstmt(): return self.visit(ctx.callstmt())
        if ctx.vardclr(): return self.visit(ctx.vardclr())
        if ctx.blkstmt(): return self.visit(ctx.blkstmt())

    # ty_pe.
    def visitTy_pe(self, ctx: MT22Parser.Ty_peContext):
        if ctx.BOOL():
            return BooleanType()
        if ctx.INT():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.AUTO():
            return AutoType()
        if ctx.arrtype():
            return self.visit(ctx.arrtype())

    # atmtype.
    def visitAtmtype(self, ctx:MT22Parser.AtmtypeContext):
        if ctx.BOOL():
            return BooleanType()
        if ctx.INT():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()

    # functype.
    def visitFunctype(self, ctx:MT22Parser.FunctypeContext):
        if ctx.BOOL():
            return BooleanType()
        if ctx.INT():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.AUTO():
            return AutoType()
        if ctx.VOID():
            return VoidType()
        if ctx.arrtype():
            return self.visit(ctx.arrtype())

    # idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):    # if have more id, add them too
        return [ctx.ID().getText()] + (self.visit(ctx.idlist()) if ctx.idlist() else []) # else only one

    # arrtype.
    def visitArrtype(self, ctx:MT22Parser.ArrtypeContext):
        return ArrayType(self.visit(ctx.dimen()), self.visit(ctx.atmtype()))


    # dimen.
    def visitDimen(self, ctx:MT22Parser.DimenContext):
        if ctx.COMMA():     # if have more
            return [int(ctx.INTNUM().getText())] + self.visit(ctx.dimen())
        return [int(ctx.INTNUM().getText())]    # reach end


    # arridx.
    def visitArridx(self, ctx:MT22Parser.ArridxContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.explist()))

    # arrele.
    def visitArrele(self, ctx:MT22Parser.ArreleContext):
        return ArrayLit(self.visit(ctx.explistskipable()))

    # explistskipable.
    def visitExplistskipable(self, ctx:MT22Parser.ExplistskipableContext):
        if ctx.explist():
            return self.visit(ctx.explist())
        else: return []    # else: return nothing


    # explistnonnull.
    def visitExplist(self, ctx:MT22Parser.ExplistContext):
        if ctx.COMMA():        # if have more exp, add them too
            return [self.visit(ctx.exp())] + self.visit(ctx.explist())
        else: return [self.visit(ctx.exp())]    # only one

    # vardclr.
    def visitVardclr(self, ctx:MT22Parser.VardclrContext):
        if ctx.varnoini(): # simple ini var; x is for all id in var
            return self.visit(ctx.varnoini()) # value assign;
        else:               # varini
            idlist, explist, ty_pe = self.visit(ctx.varini())       # take final ele from recur at array
            return [VarDecl(idlist[i], ty_pe, explist[i]) for i in range(len(idlist))]

    # vardclr.
    def visitVarnoini(self, ctx:MT22Parser.VarnoiniContext):
        if ctx.COLON():      # if get final assign, return an array ID, type, exp
            return [VarDecl(n, self.visit(ctx.ty_pe())) for n in self.visit(ctx.idlist())]
        else:
            return self.visit(ctx.varnoini()) + [VarDecl(n, self.visit(ctx.ty_pe())) for n in self.visit(ctx.idlist())]

    # varini.
    def visitVarini(self, ctx:MT22Parser.VariniContext):
        if ctx.COLON():      # if get final assign, return an array ID, type, exp
            return [ctx.ID().getText()], [self.visit(ctx.exp())], self.visit(ctx.ty_pe())
        else:
            idlist, explist, ty_pe = self.visit(ctx.varini())       # take final ele from recur at array
            return [ctx.ID().getText()] + idlist, explist + [self.visit(ctx.exp())], ty_pe

    # funcdclr.
    def visitFuncdclr(self, ctx:MT22Parser.FuncdclrContext):
        ID, functype, paramlist, inheritID = self.visit(ctx.funcproto())     # get info from proto
        blkstmt = self.visit(ctx.blkstmt())
        if inheritID:
            return FuncDecl(ID, functype, paramlist, inheritID, blkstmt)
        else:
            return FuncDecl(ID, functype, paramlist,None, blkstmt)

    # funcproto.
    def visitFuncproto(self, ctx:MT22Parser.FuncprotoContext):
        if ctx.paramlist():
            if ctx.INHERIT():   # if func has INHERIT, change all var inherit to True
                return ctx.ID(0).getText(), self.visit(ctx.functype()), self.visit(ctx.paramlist()), ctx.ID(1).getText()
            else: return ctx.ID(0).getText(), self.visit(ctx.functype()), self.visit(ctx.paramlist()), False
        else:
            if ctx.INHERIT():   # if func has INHERIT, change all var inherit to True
                return ctx.ID(0).getText(), self.visit(ctx.functype()), [], ctx.ID(1).getText()
            else: return ctx.ID(0).getText(), self.visit(ctx.functype()), [], False

    # paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        if ctx.COMMA():     # if have parameter in func
            return [self.visit(ctx.param())] + self.visit(ctx.paramlist())     # direct to prime
        else: return [self.visit(ctx.param())]     # last pare

    # param.
    def visitParam(self, ctx:MT22Parser.ParamContext):      # return the tree as bool
        return ParamDecl(ctx.ID().getText(),self.visit(ctx.ty_pe()), ctx.OUT(), ctx.INHERIT())

    # funccall.
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        if ctx.arglist():
            return FuncCall(ctx.ID().getText(), self.visit(ctx.arglist()))   # lmao idk arglist, it should be exprlist
        else: return FuncCall(ctx.ID().getText(), [])

    # arglist.
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        if ctx.COMMA():         # if have more arg, add them at end
            return [self.visit(ctx.exp())] + self.visit(ctx.arglist())
        else:
            return [self.visit(ctx.exp())]

    # exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        if ctx.CONCAT():
            return BinExpr(ctx.CONCAT().getText(), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)))
        return self.visit(ctx.exp_1())     # if not based on above

    # exp_1.
    def visitExp_1(self, ctx:MT22Parser.Exp_1Context):
        if ctx.EQ():   # &&
            return BinExpr(ctx.EQ().getText(), self.visit(ctx.exp_1(0)), self.visit(ctx.exp_1(1)))
        if ctx.IEQ():   # &&
            return BinExpr(ctx.IEQ().getText(), self.visit(ctx.exp_1(0)), self.visit(ctx.exp_1(1)))
        if ctx.LESS():   # &&
            return BinExpr(ctx.LESS().getText(), self.visit(ctx.exp_1(0)), self.visit(ctx.exp_1(1)))
        if ctx.GREATER():   # &&
            return BinExpr(ctx.GREATER().getText(), self.visit(ctx.exp_1(0)), self.visit(ctx.exp_1(1)))
        if ctx.LEQ():   # &&
            return BinExpr(ctx.LEQ().getText(), self.visit(ctx.exp_1(0)), self.visit(ctx.exp_1(1)))
        if ctx.GEQ():   # &&
            return BinExpr(ctx.GEQ().getText(), self.visit(ctx.exp_1(0)), self.visit(ctx.exp_1(1)))
        return self.visit(ctx.exp_2())     # if not based on above

    # exp_2.
    def visitExp_2(self, ctx:MT22Parser.Exp_2Context):
        if ctx.AND():   # &&
            return BinExpr(ctx.AND().getText(), self.visit(ctx.exp_2()), self.visit(ctx.exp_3()))
        if ctx.OR():   # ||
            return BinExpr(ctx.OR().getText(), self.visit(ctx.exp_2()), self.visit(ctx.exp_3()))
        return self.visit(ctx.exp_3())      # if not based on above

    # exp_3.
    def visitExp_3(self, ctx:MT22Parser.Exp_3Context):
        if ctx.ADD():   # +
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.exp_3()), self.visit(ctx.exp_4()))
        if ctx.SUB():   # -
            return BinExpr(ctx.SUB().getText(), self.visit(ctx.exp_3()), self.visit(ctx.exp_4()))
        return self.visit(ctx.exp_4())      # if not based on above


    # exp_4.
    def visitExp_4(self, ctx:MT22Parser.Exp_4Context):
        if ctx.MUL():   # *
            return BinExpr(ctx.MUL().getText(), self.visit(ctx.exp_4()), self.visit(ctx.exp_5()))
        if ctx.DIV():   # /
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.exp_4()), self.visit(ctx.exp_5()))
        if ctx.MOD():   # %
            return BinExpr(ctx.MOD().getText(), self.visit(ctx.exp_4()), self.visit(ctx.exp_5()))
        return self.visit(ctx.exp_5())      # if not based on above


    # exp_5.
    def visitExp_5(self, ctx:MT22Parser.Exp_5Context):
        if ctx.NOT(): return UnExpr(ctx.NOT().getText(), self.visit(ctx.exp_5()))   # not logic
        return self.visit(ctx.exp_6())      # if not based on above

    # exp_6.
    def visitExp_6(self, ctx:MT22Parser.Exp_6Context):
        if ctx.SUB(): return UnExpr(ctx.SUB().getText(), self.visit(ctx.exp_6()))   # neg num
        return self.visit(ctx.exp_7())      # if not based on above

    # exp_7.
    def visitExp_7(self, ctx:MT22Parser.Exp_7Context):
        if ctx.INTNUM(): return IntegerLit(int(ctx.INTNUM().getText()))     # change its type to adapt py too
        if ctx.FLOATNUM():
            if ctx.FLOATNUM().getText()[0:2] == ".e":
                return FloatLit(0.0)
            else: return FloatLit(float(ctx.FLOATNUM().getText()))   #    return FloatLit(0.0) theoretically not possible since float with exp must have deci or int
        if ctx.STR(): return StringLit(ctx.STR().getText())
        if ctx.TRUE(): return BooleanLit(True)
        if ctx.FALSE(): return BooleanLit(False)
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.arrele(): return self.visit(ctx.arrele())
        if ctx.arridx(): return self.visit(ctx.arridx())
        if ctx.funccall(): return self.visit(ctx.funccall())
        if ctx.exp(): return self.visit(ctx.exp())          # the bracker ()


    # blkstmt.
    def visitBlkstmt(self, ctx:MT22Parser.BlkstmtContext):
        return BlockStmt(self.visit(ctx.stmtlist())) if ctx.stmtlist() else BlockStmt([])


    # assnstmt.
    def visitAssnstmt(self, ctx:MT22Parser.AssnstmtContext):
        if ctx.ID():        # variables
            return AssignStmt(Id(ctx.ID().getText()),self.visit(ctx.exp()))
        else:
            return AssignStmt(self.visit(ctx.arridx()),self.visit(ctx.exp()))       # array


    # forstmt.
    def visitFor_openstmt(self, ctx:MT22Parser.For_openstmtContext):
        stmt = self.visit(ctx.open_stmt())
        if type(stmt) == list:         # if return array, take the first one
            stmt = stmt[0]
        if ctx.ID():
            iniFunc = AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.exp(0)))
            return ForStmt(iniFunc, self.visit(ctx.exp(1)), self.visit(ctx.exp(2)),stmt)
        else:       # arrayindex
            iniFunc = AssignStmt(self.visit(ctx.arridx()), self.visit(ctx.exp(0)))
            return ForStmt(iniFunc, self.visit(ctx.exp(1)), self.visit(ctx.exp(2)),stmt)

        # forstmt.
    def visitFor_closedstmt(self, ctx:MT22Parser.For_closedstmtContext):
        stmt = self.visit(ctx.closed_stmt())
        if type(stmt) == list:         # if return array, take the first one
            stmt = stmt[0]
        if ctx.ID():
            iniFunc = AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.exp(0)))
            return ForStmt(iniFunc, self.visit(ctx.exp(1)), self.visit(ctx.exp(2)),stmt)
        else:       # arrayindex
            iniFunc = AssignStmt(self.visit(ctx.arridx()), self.visit(ctx.exp(0)))
            return ForStmt(iniFunc, self.visit(ctx.exp(1)), self.visit(ctx.exp(2)),stmt)

    # dowhstmt.
    def visitDowhstmt(self, ctx:MT22Parser.DowhstmtContext):
        return DoWhileStmt(self.visit(ctx.exp()), self.visit(ctx.blkstmt()))

    # brkstmt.
    def visitBrkstmt(self, ctx:MT22Parser.BrkstmtContext):
        return BreakStmt()

    # contstmt.
    def visitContstmt(self, ctx:MT22Parser.ContstmtContext):
        return ContinueStmt()

    # rtnstmt.
    def visitRtnstmt(self, ctx:MT22Parser.RtnstmtContext):
        return ReturnStmt(self.visit(ctx.exp())) if ctx.exp() else ReturnStmt()

    # callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        cllFunc = self.visit(ctx.funccall())
        return CallStmt(cllFunc.name, cllFunc.args)