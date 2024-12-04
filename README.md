"I think every subjects are difficult, but the subject that haunted students the most in the facility is Principle of Programming Language."

Dr.NDD

# Welcome
This is the repo of all Principle of Programming Language assignments that I have done in Semester 233 (summer).

### Contents

- Slide in semester 233.
- Exercise and lab in semester 233.
- Assignment code.


### How to run
1. (Vietnamese) You can follow my guide to install ANTLR [here](https://docs.google.com/document/d/1ad_hO3TKGJZpuh9yHApAQiyc_knbTUfAhhUeI7FtrcQ/edit?usp=sharinghttps://docs.google.com/document/d/1ad_hO3TKGJZpuh9yHApAQiyc_knbTUfAhhUeI7FtrcQ/edit?usp=sharing)

2. Change current directory to initial/src where there is file run.py
  ```
  cd PPL\src
  ```

3. Then you try the following test
  ```
python run.py gen 
  ```
4. Now you are ready to try the assignment by using the following command.
  ```

python run.py gen 
python run.py test LexerSuite
python run.py test ParserSuite
python run.py test ASTGenSuite
python run.py test CheckerSuite
python run.py test CodeGenSuite
  ```

### Features in this demo
- AST nice print, and in assignment 3 and 4, input is printed in AST (You can look for original code at suites)

- TestUtils display input, expect, and your result for you to easy to compare.

![image](https://github.com/user-attachments/assets/ebb22c8b-e85c-42a4-ac66-a87bd04737f5)
