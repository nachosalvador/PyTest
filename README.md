# PyUnit

### Introducción
En Python disponemos de diferentes módulos para hacer testing unitario:
* [unittest](https://docs.python.org/2/library/unittest.html)
* [nose](http://nose.readthedocs.io/)
* [pytest](http://doc.pytest.org/)
* [doctest](https://docs.python.org/2/library/doctest.html)

Los tests unitarios nos permiten comprobar el correcto funcionamiento de nuestros módulos de código.
Muy importante destacar que sólo nos sirven para asegurar el buen funcionamiento de nuestros módulos
de código por **separado**. 

Se trata de escribir **casos de prueba** para cada función o método de nuestros módulos a modo de
abarcar todos los casos posibles que se pueden dar y haciendo que cada caso sea independiente.

Para este caso práctico emplearemos la módulo de **unittest**. La forma básica de trabajar con este
módulo es:
* Definir una clase que extienda unittest.TestCase
* Definir nuestros casos de test. Cada caso debe tener el prefijo "test_"
* Indicar al final del documento *unittest.main()* para que se ejecuten los tests.

### Requisitos
* Python 2.6 o superior

### Lanzar tests 
*python test_fizzbuzz.py*

*python -m unittest test_fizzbuzz.py*

### Referencias
* [https://docs.python.org](https://docs.python.org)

* [http://pythontesting.net/](http://pythontesting.net/)

***

### Introduction
Python has different moduls available to do unit testing:
* [unittest](https://docs.python.org/2/library/unittest.html)
* [nose](http://nose.readthedocs.io/)
* [pytest](http://doc.pytest.org/)
* [doctest](https://docs.python.org/2/library/doctest.html)

The unit tests allow us to check our code moduls works correctly. It is important to mention unit
tests only are useful to ensure the proper functioning of our moduls by **separated**.

It is about to write **test cases** for each function or method of our moduls to cover all possible
cases that can be given and making each case independent.

For this practical case we use the **unittest** modul. The basics for work with this modul are:
* Define a class that extends unittest.TestCase
* Define our test cases. Each case must have the prefix "test_"
* Include in the document (normally at the bottom) *unittest.main()* to execute all tests.

### Requirements
* Python 2.6 or higher

### Execute tests
*python test_fizzbuzz.py*

*python -m unittest test_fizzbuzz.py*

### References
* [https://docs.python.org](https://docs.python.org)

* [http://pythontesting.net/](http://pythontesting.net/)