# TechTestQA
Se utilizó fastAPI, httpx, pytest como librerías externas.
## Desarrollo
Parte 1:
- Más que nada primero busqué una forma de hacer sort (típicos algorítmos ya existentes). Iba a utilizar primero Merge Sort, pero por alguna razón no funcionó en mi código, así que fuí por Bubble Sort, que es peor en términos de complejidad temporal. Después con la lista ya ordenada es simplemente borrar los números repetidos.

Parte 2:
- Decidí usar FastAPI (que se me había olvidado como funcionaba, así que anduve leyendo la documentación de nuevo). Primero, busqué en la página de patrones de diseño (refactoring.guru) cual es el patrón que mejor servía para este caso. Como lo importante es el channel en el que se envían las notificaciones, mi conclusión fue que tenía que ser uno de los creational patterns, y así llegué al Factory. Estuve viendo como se implementaba en dos páginas, y así los diseñé (en las referencias salen las páginas). Después cree los endpoints GET y POST.
- Para el POST, decidí guardar los mensajes en un archivo .txt, que posteriormente el GET va a poder leerlo. GET va a leer todos los mensajes que hay en el archivo y los retornará al hacer la llamada. También hice que si no hay nada simplemente retorna una lista vacía.
- Se me había olvidado el uso de Pydantic. Con ello se crea como es el body de request de las notificaciones.
- Finalmente, corrí el código con "fastapi dev .\parte2.py" y luego con Thunder Client hice llamadas de prueba. Para el POST, se puede usar el body:
```json
{
  "userId": "123",
  "message": "Hola",
  "channel": "sms"
}
```
y cambiar el channel a email para comprobar su funcionamiento.

Parte 3:
- Primero me dediqué a hacer los casos de prueba. Busqué en Google una página para tener un formato sobre el diseño de estos (testrigor.com), y en base a ellos los diseñé.
- Después de hacerlas, yo primero las corrí manualmente para verificar que las estaba haciendo bien. Después me dediqué a hacer las pruebas automáticas.
- Primero pensé en usar pytest directamente, y luego leyendo la documentación de FastAPI me fijé que se podía usar httpx, el cual hace uso de pytest para hacer pruebas directamente sobre la API.
- Después de eso, simplemente implementé los casos de pruebas creados anteriormente. El archivo tiene que tener la palabra test en el archivo para que al correr en la terminal 'pytest' se ejecute. Al ejecutarlo se obtuvo 4 test pasados. No es necesario tener la API corriendo de fondo para realizar estas pruebas.
## Referencias

Parte 1: 
- https://www.geeksforgeeks.org/python/python-program-for-bubble-sort/

Parte 2:
- https://fastapi.tiangolo.com/learn/
- https://fastapi.tiangolo.com/tutorial/body/
- https://www.geeksforgeeks.org/python/factory-method-python-design-patterns/
- https://refactoring.guru/es/design-patterns/catalog
- https://refactoring.guru/design-patterns/factory-method/python/example

Parte 3:
- https://testrigor.com/blog/how-to-write-test-cases-detailed-examples/
- https://docs.pytest.org/en/stable/#documentation
- https://fastapi.tiangolo.com/tutorial/testing/
- https://fastapi.tiangolo.com/tutorial/testing/#extended-testing-file