// Phùng Gia Minh Khôi - 2252381
grammar MT22;

@lexer::header {
from lexererr import *

}

options{
	language=Python3;
}

// change EBNF to BNF hope for flawless btl3,4's preparation and force the priority

//          PARSER

program: outfunc EOF
        | EOF;      //  a program has stmt to run

outfunc: (vardclr | assnstmt| funcdclr) outfunc
        | (vardclr | assnstmt| funcdclr);//  Statements available for outside function
// vardclr, assnstmt: global var

// Statements
stmtlist: stmt stmtlist
        | stmt;     // list or one; CFG

// If, while
stmt: open_stmt | closed_stmt;
open_stmt: IF LC exp RC stmt                    // only this allows if no else
        |   IF LC exp RC closed_stmt ELSE open_stmt
        |   WHILE LC exp RC open_stmt         // while only keeps their status.
        |   for_openstmt;                       // for stmt
closed_stmt: basic_stmt
        |   IF LC exp RC closed_stmt ELSE closed_stmt
        |   WHILE LC exp RC closed_stmt
        |   for_closedstmt;                       // for stmt

// Other statements
basic_stmt: vardclr | assnstmt  //  everything for a program to run, EXCEPT IF ELSE WHILE in BTL2
    | dowhstmt | brkstmt | contstmt | rtnstmt | callstmt | blkstmt ;

// Types for various uses
ty_pe: BOOL | INT | FLOAT | STRING | AUTO | arrtype;        // all type; the ARR if removed will cause prob
atmtype: BOOL | INT | FLOAT | STRING ;                  // base type
functype: BOOL | INT | FLOAT | STRING | AUTO | VOID | arrtype;     // type for funtion return

// Identify list
idlist: ID (COMMA idlist)
        |ID;           // list or one; CFG

// Array declaration, access index, ele
arrtype: ARR LS dimen RS OF atmtype;    // ini the arr
dimen: INTNUM (COMMA dimen)           // ini dims
        | INTNUM;
arridx: ID LS explist RS;               // dimen cannot be null; this used to access ele in arr
arrele: LB explistskipable RB;          // aka the bracket {ele in arr}

// Variable declaration
vardclr:  varnoini SEMI                // no ini declare
	    | varini SEMI;                           // variables ini with #var = #exp
varnoini: idlist COMMA varnoini COMMA ty_pe     // use CFG aka recursion
        | idlist COLON ty_pe;   // 1 name with exp dclr; must have #var = #exp
varini: ID COMMA varini COMMA exp     // use CFG aka recursion
        | ID COLON ty_pe ASSN exp;   // 1 name with exp dclr; must have #var = #exp

// Function declaration
funcdclr: funcproto blkstmt;                // raw func declare; body is blkstmt

// Function prototype
funcproto:  ID COLON FUNC functype LC paramlist RC (INHERIT ID)   // the proto func can contain no para
        | ID COLON FUNC functype LC RC (INHERIT ID)
        | ID COLON FUNC functype LC paramlist RC
        | ID COLON FUNC functype LC RC;
paramlist: param (COMMA paramlist)
        | param;      // just a list of parameter in function
param: INHERIT OUT ID COLON ty_pe
        |  INHERIT ID COLON ty_pe
        |  OUT ID COLON ty_pe
        |  ID COLON ty_pe;

// Function call
funccall: ID LC arglist RC              // add arg or nothing
        |   ID LC RC;
arglist: exp (COMMA arglist)
        |exp; // prime is only for CFG

// Expression; mainly for array
explistskipable: explist | ;                   // can be nothing
explist: exp (COMMA explist)       // list or one for array; CFG
        | exp;

// Operator association and precedence from low to high
exp : exp CONCAT exp | exp_1;      // string concatenation
exp_1: exp_1 (EQ | IEQ | LESS | GREATER | LEQ | GEQ) exp_1 | exp_2;      // compare; neither left to right
exp_2: exp_2 (AND | OR) exp_3 | exp_3;          // logical
exp_3: exp_3 (ADD | SUB) exp_4 | exp_4;         // +, -
exp_4: exp_4 (MUL | DIV | MOD) exp_5 | exp_5;   // * / %
exp_5: NOT exp_5 | exp_6;                       // not logic
exp_6: SUB exp_6 | exp_7;                       // the negative number
exp_7: INTNUM | FLOATNUM  | STR | TRUE | FALSE | ID
        | arrele | arridx | arrtype | funccall | (LC exp RC);   // atomic type, TF, array is possible, or even func
// must evaluate inside () 1st
// Block statement
blkstmt: LB stmtlist RB
        | LB RB;

// assn variable statements
assnstmt: (ID) ASSN exp SEMI
        | (arridx) ASSN exp SEMI;

// For
for_openstmt: FOR LC (ID) ASSN exp COMMA exp COMMA exp RC open_stmt
        |FOR LC (arridx) ASSN exp COMMA exp COMMA exp RC open_stmt;
for_closedstmt: FOR LC (ID) ASSN exp COMMA exp COMMA exp RC closed_stmt
        |FOR LC (arridx) ASSN exp COMMA exp COMMA exp RC closed_stmt;

// Do-while
dowhstmt: DO blkstmt WHILE LC exp RC SEMI;

// Brk
brkstmt: BRK SEMI;

// Cont
contstmt: CONT SEMI;

// Rtn
rtnstmt: RTN exp SEMI
        |RTN SEMI;

// Call
callstmt: funccall SEMI;

//          LEXER

//          AND NOW THE MT22'S NO-BRAIN PPL TIME
// Keyword
AUTO: 'auto';
BRK: 'break';
BOOL: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNC: 'function';
IF: 'if';
INT: 'integer';
RTN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONT: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARR: 'array';

// Operators
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
MOD : '%';
NOT : '!';
AND : '&&';
OR : '||';
EQ : '==';
IEQ : '!=';
LESS : '<';
LEQ : '<=';
GREATER : '>';
GEQ : '>=';
CONCAT: '::';

// Separator
LC : '(';   // Left Circle
RC : ')';
LS : '[';   // Left Square
RS : ']';
DOT: '.' ;
COMMA: ',';
SEMI: ';';
COLON: ':';
LB : '{';   // Left bracket
RB : '}';
ASSN: '=';
//          THE MT22'S NO-BRAIN PPL TIME ENDED

// Ellimate comment after no-brain
// Area comment; skip bc not used in code; dot match any char
ACMT: '/*' .*? '*/'-> skip;
// Line comment; stop when get newline
CMT:   '//' ~[\n]* -> skip;

// Integer, float; int with exp is float.


INTNUM: '0' | [1-9]('_'?[0-9])* { self.text = self.text.replace('_', '') };
//FLOATNUM: ([0-9]('_'?[0-9]+)*)? DECI | INTNUM EXP | ([0-9]('_'?[0-9]+)*)? DECI EXP { self.text = self.text.replace('_', '')};
FLOATNUM: INTNUM EXP | DECI EXP | [0-9]('_'?[0-9]+)* DECI EXP? { self.text = self.text.replace('_', '')};
// int with exp, or deci with int n' exp optional
fragment DECI: [.][0-9]*;
fragment EXP: [eE][+-]?[0-9]+;

STR: ["] (~[\\\r\n\f'"] | '\\'[bfrnt'"\\])* ["]   {self.text = self.text[1:-1]};  /* string has to be with "", inside is
not WS, or \\followed by any WS char behind it; lmao idk how /" works via this, works on LMS but not this
Later: is to solve \" => "
*/

// Fragment
// Identify
ID: [A-Za-z_][A-Za-z_0-9]*;
WS : [ \t\r\n]+ -> skip ; // skip meaningless factors such as sp, tb, endl

// Error area
UNCLOSE_STRING: '"' (~[\\\r\n\f'"] | '\\' [bfrnt'"\\])*[\f]?[\r]?[\n]?
{
	if self.text.find('\r\n') != -1:          # if not found newline
        pos = self.text.find('\r\n')          # go to endline;
        raise UncloseString(self.text[1:pos])  # not found: raise error to end
	if self.text.find('\r') != -1:          # if not found newline
        pos = self.text.find('\r')          # go to endline;
        raise UncloseString(self.text[1:pos])   #  then raise Error
	if self.text.find('\n') != -1:          # if not found newline
        pos = self.text.find('\n')          # go to endline;
        raise UncloseString(self.text[1:pos])   #  then raise Error
	if self.text.find('\f') != -1:          # if not found newline
        pos = self.text.find('\f')          # go to endline;
        raise UncloseString(self.text[1:pos])   #  then raise Error
	else:
        raise UncloseString(self.text[1:])  # not found: raise error to end
	};
ILLEGAL_ESCAPE: ["] (~[\\\n\b\f\r\t'"] | [\\][bfrnt'"\\])*[\\]~[bfrnt'"\\] {
        raise IllegalEscape(self.text[1:])
    };
ERROR_CHAR: .{raise ErrorToken(self.text)};