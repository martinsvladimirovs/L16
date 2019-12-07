Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> v0=0
>>> t=0.1
>>> y = v0*t-0.5*g*t**2
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    y = v0*t-0.5*g*t**2
NameError: name 'g' is not defined
>>> y=v0*t-0.5*g*t**2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    y=v0*t-0.5*g*t**2
NameError: name 'g' is not defined
>>> g=9.81
>>> y=v0*t-0.5*g*t**2
>>> print y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(y)?
>>> print y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(y)?
>>> print y;
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(y)?
>>> print(y)
-0.04905000000000001
>>> t=1
>>> y=v0*t-0.5*g*t**2
>>> print(Y)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(Y)
NameError: name 'Y' is not defined
>>> print(y)
-4.905
>>> 
v0=5 ; t=1 ; y=v0*t-0.5*g*t**2
>>> print 'Pēc %g sekundēm bumba būs %.2f metru augstumā \n' % (t,y)
SyntaxError: invalid syntax
>>> print ('Pēc %g sekundēm bumba būs %.2f metru augstumā \n' % (t,y))
Pēc 1 sekundēm bumba būs 0.09 metru augstumā 

>>> print ('Pēc %.g sekundēm bumba būs %.f metru augstumā \n' % (t,y)) #samainīts .2f uz .f
Pēc 1 sekundēm bumba būs 0 metru augstumā 

>>> print ('Pēc %.g sekundēm bumba būs %.2f metru augstumā \n' % (t,y))
Pēc 1 sekundēm bumba būs 0.09 metru augstumā 

>>> t=5 ; v0=20 ; g=9.80 ; y=v0*t-0.5*g*t**2;
>>> print ('Pēc %.g sekundēm bumba būs %.2f metru augstumā \n' % (t,y))
Pēc 5 sekundēm bumba būs -22.50 metru augstumā 

>>> t=2; v0=20; g=9.80 ; y=v0*t-0.5*g*t**2;
>>> print ('Pēc %.g sekundēm bumba būs %.2f metru augstumā \n' % (t,y))
Pēc 2 sekundēm bumba būs 20.40 metru augstumā 

>>> 
