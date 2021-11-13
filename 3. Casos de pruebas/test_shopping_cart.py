'''
coverage: es una medida porcentual el cual nos indica que % de nuestro código ha sido testeado,
por lo cual sabremos cuales lineas de nuestro código ha sido usada y cuales no.
Con esta funcionalidad podemos hacer refactor de nuestro código y eliminar aquellas líneas 
que no la estamos utilizando. Se debe instalar la libreria "pip install coverage".

utilizar los siguientes comandos en consola:
1.- coverage report nombre_archivo.py: Aqui nos va a mostrar una pequeña tabla con el indicador "Cover". este
inidcador si esta en 0% nos indica que nuestro código no ha sido utilizado.
2.- coverage run test_shopping_cart.py: Al hacer esto podemos ver que las pruebas han pasado. este crea un archvio en 
el directorio del archivo "test_shopping_cart.py". Este paso lo hacemos para aumentar el indicador Cover de la tabla.
3.- coverage report shopping_cart.py: Aquí nos damos cuenta el Cover aumentó a 96%. Si requerimos mas detalles de la cobertura,
colocamos coverage report -m shopping_cart.py. Aquí agrega una columna más llamada "Missing" con la línea del código que no se esta utilizando.
Aqu´tenemos 2 opciones: Eliminar esa linea o crear una prueba que ejecute esa línea.

Tambien podemos visualizar estos reportes vía html. Para ello hacemos los siguientes pasos:

1.- En consola escribimos "coverage html shopping_cart.py". Esto va a generar una nueva carpeta
 llamada htmlcov. Para visualizar la informacion de estas páginas levantamos el servicio web de python.
2.- python -m http.server aqui en unos segundos se levanta el servicio y vemos el puerto con el cual esta levantando.
 Buscamos nuestro navegador web y colocamos localhost:8000. Aquí si existiese lineas de códigos que no se 
 estan utilizando las marca con una sombra roja.


'''
import unittest
from shopping_cart import Item, ShoppingCart, NotExistsItemError

API_VERSION = 15
'''
#Primer ejercicio
class TestShopingCart(unittest.TestCase):

    def setUp(self):
        print("Antes de la prueba")

    def tearDown(sel):
        print("Despues de la prueba")

    def test_nombre_producto_igual_manzana(self):
        item = Item("Manzana", 5)
        self.assertEqual(item.name, "Manzana")

    def test_nombre_producto_diferente_manzana(self):
        item = Item("Manzana", 5)
        self.assertNotEqual(item.name, "Pera")

'''
#Segundo ejercicio
class TestShopingCart(unittest.TestCase):

    def setUp(self):
        self.pan = Item("Pan", 1)
        self.jugo = Item("Jugo", 3)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    #Prueba 1
    def test_nombre_producto_igual_pan(self):
        self.assertEqual(self.pan.name, "Pan")

    #Prueba 2
    def test_nombre_producto_diferente_manzana(self):
        self.assertNotEqual(self.jugo.name, "Manzana") # = >---aquí compara valores

    #Prueba 3
    def test_contiene_producto_carrito(self):
        self.assertTrue(self.shopping_cart.count_items())

    #Prueba 4
    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.count_items())

    #Prueba 5
    def test_obtener_producto(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item,self.pan) #is aquí compara objetos
        self.assertIsNot(item,self.jugo)

    #Prueba 6: Aquí es donde podemos testear nuestras funciones
    def test_exception_al_obtener_jugo(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)
    
    #Prueba 7: Aquí es donde podemos testear nuestras funciones con operadores relacionales
    def test_total_con_un_producto(self):
        total = self.shopping_cart.total()
        self.assertGreater(total, 0)
        self.assertGreaterEqual(total, 0)
        self.assertLess(total, self.pan.price + 1)
        self.assertEqual(total, self.pan.price)

    #Prueba 8: Para validar que el código lo contiene el producto
    def test_validar_codigo_producto(self):
        self.assertRegex(self.pan.code(), self.pan.name)
        
    #Prueba 9: Si los métodos assert no nos funcionan para lo que
    # necesitamos podemos hacer uso del metodo fail. 
    def test_falla(self):
        if 2 > 3:
            self.fail("2 no es mayor que 3")

    #Prueba 10: Podemos programar que salte una prueba ya que por alguna razon conocemos que 
    # la funcion no funciona, Visualizamos en el cmd una 'S'. O si queremos mas detalles
    # ejecutamos test_archivo.py -v

    #@unittest.skip("Colocamos nuestro motivos")
    #@unittest.skipiF(API_VERSION < 18, "La version es obsoleta")
    @unittest.skipUnless(3 > 5, "La version es obsoleta")
    def test_prueba_ship(self):
        pass

if __name__ == '__main__':
    unittest.main()