grammar BKIT;
/*                   Exercise 1            */
Int : [1-9][0-9]*;
// Example : 424, 434,645,5233,4559,2488,3110,84106,4423

Float : Int '.'? EXP? | Int DECI EXP?;
fragment DECI: '.'[0-9]+;
fragment EXP: [eE][+-]?[0-9]+;
// Example : 1.0 , 121.42 , 152e+24 , 9.3e-2, 6E5,23e+0

Binary : [01]+;
// Example : 0101 , 001101 , 1001001000010 , 01010110101001

/*                   Exercise 2            */
Id : [a-z][A-Za-z0-9_]*;
// Example : arDG_43, xfGFd_f35_, f_w3_gb5g

Operator: '+' | '-'| '*' | '/' | '%'
| '&&' | '||' | '>'| '>='| '<'| '<=';
// Example : + , -, * , / , %, | '&&' | '||' | '>'| '>='| '<'| '<='