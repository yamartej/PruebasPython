import unittest
from item_prueba import Item

class TestShopingCart(unittest.TestCase):

    def test_cinco_mas_cinco_igual_a_diez(self):
        assert 5 + 5 == 10

    def test_nombre_producto_igual_manzana(self):
        item = Item("Manzana", 5)
        self.assertEqual(item.name, "Manzana")

    def test_nombre_producto_diferente_manzana(self):
        item = Item("Manzana", 5)
        self.assertNotEqual(item.name, "Pera")



if __name__ == '__main__':
    unittest.main()