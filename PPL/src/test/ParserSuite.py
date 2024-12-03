import unittest
from TestUtils import TestParser
# 200
testcaseArray = [
    ["""main: function void(){
    print(
        "WARNING: THIS IS ULTIMATE TESTCASES FOR MT22 IN 233",
    "FINISH BASIC TESTCASES BEFORE TRYING THIS.",    
    "THE TEST WILL CONTAINS AT MOST 1 ERROR, VIEW ERROR IN HEADER COMMENT.");}"""
        ,"""successful"""],
    # 201 unclose string
    [        """ // 201 unclose string
main: function void(){
i : integer;
for (i = x + 2,i < 4, i + 1){
    if (i ==3){
        i = i + 10;     // Made by Chiily On
    }
    else {
        if (i==2){
            i = i + 1;
        }
    }
    print("Made by Chiily On 100%);
}}""","""Made by Chiily On 100%);"""],
    # 202 ID start with num ;
    [""" // ID start with num ;
del: function void (out str: string , n: integer) inherit deef{                 // del let.
        for (n = n, n < (strlen(str) - 1), n + 1)
                str[n] = str[n + 1];                    // copy af. to bef.
                str[strlen(0score) - 1] = "";                      // last is blank
        return;
}""", """Error on line 5 col 28: score"""],
    [   # 203 do while w/o blkstmt
        """ // do while w/o blkstmt
            main: function integer() 
            {
                    char : string = "     doAn VAN   *(()hau       ";
                    // TODO
                    i : integer;                                                                    // letter str
                    sp1 : boolean = false;                                          // check 1st space
                    // CUT SP HEAD, FIND 1ST LETTER.
                    // CUT >2ND REPEAT SP
                    for (i = 0, i < strlen(str), i + 1) {
                            if (str[i] == " ")
                                    if (sp1 == true) {
                                            del(str, i);
                                            i = i - 1;                                              // auto-move => no plus i
                                    }
                                    else
                                            sp1 = true;
                            else
                                    sp1 = false;
                    }
                    // CUT SP TAILS
                    for (i = (strlen(str) - 1), ((str[i] == " ") && (i >= 0)), i - 1) {
                            str[i] = "";
                    }
                    // TRANSFER TO OUTSTR (this var is harder to code)
                    for (i = 0, (i < strlen(str)), i + 1) {
                        outstr[i] = str[i];
                    }
                    for (n = n, (i < strlen(outstr)), i + 1) {              // set redundant char slots to blank
                            outstr[i] = "";
                    }
                    // REMOVE BELOW WHEN ENTER CODE, THIS IS RESULT DISP.
                    print(outstr, ".");
                    do del(str, 0);
                    while (str[0] == " ");
                    return 0; //REMOVE 0
            }
            ""","""Error on line 34 col 23: del"""],
    #204
    ["""    //
process : function void (str : string, outstr : string) {
	// TODO
	// REWORK use knowledge of pointer and c-str

	strcpy(outstr, str);
	outstr = outstr + strlen(str) - 1;
	
	for (i = 0, i :: strLen, i+1)		// bring ptr outstr to end; when str++, cut head, pointer is the 1st ltr
	{
		outstr = str;
		str = str + 1;
		outstr = outstr -1;
	}
	if (bool())
		strLen : integer  = strlen[];
	return "\\n";
}""","""\\n"""],
    #205    /" -> " in string;
    ["""    // declare in if expression
main : function integer() {
	str, outstr : string = "timing", strlen(str) + 1;
	process(str, outstr);
	print("df\"");
}
if (strstr(szString1, " ") != c && g : float)
	print("1");
	else print("/");""",""");"""],
    #206 else with no stmt
    ["""    // else with no stmt
// InLab_Q1_CString header
isValidChar: function boolean (c: string) {
        if (c >= "a" && c <= "z" || c >= "A" && c <= "Z"){
                return true;
                }
        else;
}""","""Error on line 7 col 12: ;"""],
    #207 unclosed bracket
    ["""    // unclosed bracket
lowercase : function string(c: string) {
        OFFSET : integer = 32;
        if (c >= "A" && c <= "Z")
            {
            }
        else {}
""","""Error on line 8 col 0: <EOF>"""],
    #208
    ["""        // missed closing
uppercase : function string(c: string) inherit {
        OFFSET : integer = 32;
        if (c >= "a" && c <= "z")
                return ((c) - ((OFFSET));
        else return c;
}""","""Error on line 2 col 47: {"""],
    #209
    [""" // outstr = DELIM = DELIM;
 process: function void(str: string, outstr: string) {
        flag : boolean = true;
         SPACE : string= " ";
       DELIM : string= "";
        // Check the first character

        while (str) {
                if (isValidChar(str) || str == SPACE && !flag) {
                        outstr = flag(uppercase(str) , lowercase(str));
                        outstr  = outstr + 1;
                }
                if (str == SPACE) {
                        flag = true;
                }
                else if (isValidChar(str)) {
                        flag = false;
                }

                str = str + 1;
        }

        // Check the last character and add eliminator
        if ((outstr - 1) == SPACE) {
                DELIM = (outstr - 13_454_675_56.213E8) ;
        }
        else {
                outstr = DELIM = DELIM;
        }
}""","""Error on line 28 col 31: ="""],
    #210
    [""" // return if
 del: function void(inherit str: string, out n: integer) inherit _Ig4{                  // del let.
        for (n=n, n < (strlen(str) - 1), n + 1)
                str[n] = str[n + 1];                    // copy af. to bef.
        str[strlen(str) - 1] = "";                      // last is blank
        return if;
}""", """Error on line 6 col 15: if"""],
    #211
    ["""    // Array access w/o expression
calc: function integer(str : string) {                                                                  // convert from bin to dec
        // TODO
        i, j, a: integer = 8,6,0;                                                                       // num pos, seq of binary multi loop
        //int a;                                                                        // temp var to save pow(2)
         sum: integer = 0;                                                      // output
        // if necessary: use proper
        // use pointer
         bin: string = strlen(str) + 1;
        strcpy(bin, str);
        lenBin : integer = strlen(bin);
        for (i = 0,  i < lenBin, i+1) {
                if (bin == "1") {
                        a = 1;                                                                                  // build value from pos
                        for (j = 0, j < (lenBin - 1 - i), j+1)
                                a = a * 2;
                        sum = sum + a;
                }
                bin = bin+1;
        }
        return strlen[];
}""", """Error on line 21 col 22: ]"""],
    #212 3 variables but 2 values
    ["""    // 3 variables but 2 values
main:function integer() {
        i, j, a: integer = 8,6;     
        print(calc(str));
}
""", """Error on line 3 col 30: ;"""],
    #213
    ["""    // float have _
 sp1 : boolean = false;
 main: function void(){
        for (i = strlen(str) - 1, i >= 0, i-1) {
                if (str[i] == "1") {
                        a = 1;
                        for (j = 0, j < (strlen(str) - i-1), j+1)
                                a = a * 2.3_4E8;
                        sum = sum + a;
                }
        }
}        """, """Error on line 8 col 43: _4E8"""],
    #214 EXP w/o num
    ["""    // EXP w/o num
main: function void(){
    print(strlen(str));// REMOVE

        // if need, use proper process header
        // CAL FOR SUM (old)
                /**/
    a = a * 2.34e-;
}""", """Error on line 8 col 16: e"""],

    #215
    ["""    // function call 2-level (())
    del : function void(str : string, n: integer) {			// del let.
	for (n=n, n < (strlen(str) - 1), n+1)
		str[n] = str[n + 1];			// copy af. to bef.
	str[strlen(str) - 1] = "";			// last is blank
	foo(2 + x, 4.0 / y);
    goo((2 + x, 4.0 / y));
	return;
}
""", """Error on line 7 col 14: ,"""],

    #216
    ["""    // multi declare on prototype
proper: function void(str, outstr : string) {			// "   d&OaN   V$aN  hA*U    "
	// REWORK use pointer
	process(str,outstr);
	return;
}
""", """Error on line 2 col 25: ,"""],

    #217
    ["""    // array missed ]
 main : function integer ()
{
	str, outstr : string = "   d&OaN   V$aN  hA*U    ", char[strlen(str) + 1;
	proper(str, outstr);
	/* TODO*/
}""", """Error on line 4 col 73: ;"""],
    #218
    ["""    // Cannot be Array
calc: function integer(str : string) {                                                                  // convert from bin to dec
        // TODO
        i, j, a: integer = {8,6,0};                                                                       // num pos, seq of binary multi loop
}""", """Error on line 4 col 34: ;"""],
    #219
    ["""    // Cannot declare variables in for
clrRightChar: function void(str : string) {
	for (i : integer = 3, i < strlen(str), i+1) {		// set redundant char slots to blank
		stri: string;
	}
}""", """Error on line 3 col 8: :"""],
    #220
    ["""    // Reverse INHERIT and OUT
    main : function void(out inherit str : string, n: integer) {			// del let.
	for (n=n, n < (strlen(str) - 1), n+1)
		str[n] = str[n + 1];			// copy af. to bef.
	str[strlen(str) - 1] = "";			// last is blank
	foo(2 + x, 4.0 / y);
    goo();
	return;
}""", """Error on line 2 col 29: inherit"""],
    #221
    ["""    // Wrong array dimension access
        main : function void(str : string, n: integer) {			// del let.
                // TRANSFER TO OUTSTR (this var is harder to code)
            for (i = 0, (i < strlen(str)), i + 1) {
                            outstr[i][j] = str[i];
            }
}""", """Error on line 5 col 37: ["""],
    #222
    ["""    // Dots in ID
    cutString : function void(s : string, index: integer) {
    // TO DO
    if (index < s.size()) {
        s = s.substr(index, s.size() - index);
        print(s);
    }
}
""", """Error on line 4 col 17: ."""],
    #223
    ["""    // Unclosed String with newline
    main : function integer(inherit out str : string) {
    s : string = "Truong Dai Hoc\n";
    cutString(s, 4);
}
""", """Truong Dai Hoc"""]
]
class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        testcaseNo = 200
        for testcase in testcaseArray:
            TestParser.test(testcase[0], testcase[1], testcaseNo)
            #TestParser.test(testcase[0], testcase[1], testcaseNo)
            testcaseNo+=1