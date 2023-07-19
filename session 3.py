Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("welcome")
welcome
print(234)
234
print(34+34)
68
>>> type("vicky")
<class 'str'>
>>> type(23)
<class 'int'>
>>> type(false)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> type(4.5)
<class 'float'>
>>> type(['razak',345,5.6,"zealous",false])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(['razak',345,5.6,"zealous",false])
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> type(['Razak',345,5.6,"zealous",false])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(['Razak',345,5.6,"zealous",false])
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> type(False)
<class 'bool'>
>>> type('razak',345,5.6,"zealous",False])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> type(['razak',345,5.6,"zealous",False])
<class 'list'>
>>> type({'razak',456,5.6,"zealous",False})
<class 'set'>
>>> type(('razak',453,5.6,"zealous",False))
<class 'tuple'>
>>> type({"core":"python","version":3.10,"2010":false})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type({"core":"python","version":3.10,"2010":false})
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> type({"core":"python","version":3.10,"2010";False})
SyntaxError: ':' expected after dictionary key
>>> type({"core":"python","version":3.10,"2010":False})
<class 'dict'>
