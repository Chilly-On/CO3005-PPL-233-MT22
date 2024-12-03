# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#outfunc.
    def visitOutfunc(self, ctx:MT22Parser.OutfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#open_stmt.
    def visitOpen_stmt(self, ctx:MT22Parser.Open_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#closed_stmt.
    def visitClosed_stmt(self, ctx:MT22Parser.Closed_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#basic_stmt.
    def visitBasic_stmt(self, ctx:MT22Parser.Basic_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ty_pe.
    def visitTy_pe(self, ctx:MT22Parser.Ty_peContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atmtype.
    def visitAtmtype(self, ctx:MT22Parser.AtmtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functype.
    def visitFunctype(self, ctx:MT22Parser.FunctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrtype.
    def visitArrtype(self, ctx:MT22Parser.ArrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimen.
    def visitDimen(self, ctx:MT22Parser.DimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arridx.
    def visitArridx(self, ctx:MT22Parser.ArridxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrele.
    def visitArrele(self, ctx:MT22Parser.ArreleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardclr.
    def visitVardclr(self, ctx:MT22Parser.VardclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varnoini.
    def visitVarnoini(self, ctx:MT22Parser.VarnoiniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varini.
    def visitVarini(self, ctx:MT22Parser.VariniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdclr.
    def visitFuncdclr(self, ctx:MT22Parser.FuncdclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcproto.
    def visitFuncproto(self, ctx:MT22Parser.FuncprotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funccall.
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arglist.
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#explistskipable.
    def visitExplistskipable(self, ctx:MT22Parser.ExplistskipableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#explist.
    def visitExplist(self, ctx:MT22Parser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_1.
    def visitExp_1(self, ctx:MT22Parser.Exp_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_2.
    def visitExp_2(self, ctx:MT22Parser.Exp_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_3.
    def visitExp_3(self, ctx:MT22Parser.Exp_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_4.
    def visitExp_4(self, ctx:MT22Parser.Exp_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_5.
    def visitExp_5(self, ctx:MT22Parser.Exp_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_6.
    def visitExp_6(self, ctx:MT22Parser.Exp_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_7.
    def visitExp_7(self, ctx:MT22Parser.Exp_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blkstmt.
    def visitBlkstmt(self, ctx:MT22Parser.BlkstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assnstmt.
    def visitAssnstmt(self, ctx:MT22Parser.AssnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_openstmt.
    def visitFor_openstmt(self, ctx:MT22Parser.For_openstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_closedstmt.
    def visitFor_closedstmt(self, ctx:MT22Parser.For_closedstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhstmt.
    def visitDowhstmt(self, ctx:MT22Parser.DowhstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#brkstmt.
    def visitBrkstmt(self, ctx:MT22Parser.BrkstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#contstmt.
    def visitContstmt(self, ctx:MT22Parser.ContstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#rtnstmt.
    def visitRtnstmt(self, ctx:MT22Parser.RtnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)



del MT22Parser