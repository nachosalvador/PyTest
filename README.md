# PyUnit

### Introducción
En Python también disponemos de diferentes módulos para poder hacer testing unitario:
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
* Definir nuestros casos de test. Cada caso(función) debe tener el prefijo "test_"
* Indicar al final del documento unittest.main() para que se ejecuten los tests.

### Requisitos
* Python 2.6 o superior
 
***
### Lanzar tests 
*python test_fizzbuzz.py*

*python -m unittest test_fizzbuzz.py*
 
***
### Referencias
* [https://docs.python.org](https://docs.python.org)
 
* [http://pythontesting.net/](http://pythontesting.net/)