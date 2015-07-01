#pytest

### Introducción
Es una herramienta muy potente para realizar tests con Python. Entre sus principales características podemos destacar:

* Que requiere relativamente poco código en los tests (no-boilerplate) (sample1-test1.py y sample1-test2.py)
* Se integra con otros métodos y herramientas de testeo como unittest, nose y doctest
* Es relativamente sencillo poder escalar desde test unitario a test funcional

***

### Test unitario
 
Los tests unitarios nos permiten comprobar el correcto funcionamiento de nuestros módulos de código. Muy importante destacar que sólo nos sirven para asegurar el buen funcionamiento de nuestros módulos de código por **separado**. 

Se trata de escribir **casos de prueba** para cada función o método de nuestros módulos a modo de abarcar todos los casos posibles que se pueden dar y haciendo que cada caso sea independiente. 

**Pytest** para este caso también nos ayuda permitiendo tener *setups* y *teardowns* de forma bastante especifica. Podemos ejecutar código al principio y final de: 
* los módulos(*setup_module/teardown_module*)
* las clases(*setup_class/teardown_class*)
* las funciones(*setup_function/teardown_function*) 
* los métodos(*setup_method/teardown_method*)

Uso: [](http://pytest.org/latest/assert.html#assert-with-the-assert-statement) http://pytest.org/latest/assert.html#assert-with-the-assert-statement

### Requisitos
* Python 2.6 o superior, Python 3
 
***
 
### Instalación
* via Pip:* pip install pytest*
* via Aptitude: *apt-get install python-pytest*
 
 
***
 
### Lanzar tests 
*python -m pytest test_um_pytest.py*

*py.test test_um_pytest.py*
 

Uso: [](https://pytest.org/latest/usage.html) https://pytest.org/latest/usage.html
 
***

###Referencias
* [](http://pytest.org/) http://pytest.org/
 
* [](http://pythontesting.net/) http://pythontesting.net/
