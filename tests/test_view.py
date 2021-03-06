from flask_testing import TestCase
from wsgi import app, PRODUCTS

class TestViews(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_read_my_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        
        #on test si le product est une dictionnaire (instance dictionnaire)
        self.assertIsInstance(products, dict)

        #on test sa taille si plus grand que 2
        self.assertGreater(len(products), 2)

        #on test si tous le produits est retourné
        self.assertEqual(len(products), len(PRODUCTS))

    def test_read_one_found_product(self):
        resp = self.client.get("/api/v1/products/1")

        #on test que le code de retour est 200
        self.assertEqual(resp.status_code, 200)


    def test_read_one_not_found_product(self):
        resp = self.client.get("/api/v1/products/6")

        #on test que le code de retour est 404
        self.assertEqual(resp.status_code, 404) 

    def test_create_product(self):
        old_product_size = len(PRODUCTS)

        response = self.client.post("/api/v1/products", json={'name': "France3"})
    
        products = response.json

        #on test que le code de retour est 201
        self.assertEqual(response.status_code, 201)

        #on test si on a un produit ajouté taille new produit > taille old produit
        self.assertGreater(len(products), old_product_size)

    def test_update_product(self):
        response = self.client.patch("/api/v1/products/1", json={"name": "Name updated"})

          #on test que le code de retour est 204
        self.assertEqual(response.status_code, 204)

    def test_update_product_validation_error(self):
        response = self.client.patch("/api/v1/products/2", json={"name": ""})

          #on test que le code de retour est 422
        self.assertEqual(response.status_code, 422)     
