from rest_framework.test import APIClient
from rest_framework import status
import pytest
from store.models import Cart,Product,CartItem,Collection


@pytest.mark.django_db
class TestCart:
    def test_create_cart(self):
        client = APIClient()
        response = client.post('/store/carts/', {})
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] is not None

    def test_retrieve_cart(self):
        client = APIClient()
        cart = Cart.objects.create()
        response = client.get(f'/store/carts/{cart.id}/')
        
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestCartItem:
    def test_add_item_to_cart(self):
        client = APIClient()
        cart = Cart.objects.create()
        collection = Collection.objects.create(title="c")
        product = Product.objects.create(title='p', inventory=100, unit_price=10,collection=collection)
        response = client.post(f'/store/carts/{cart.id}/items/', {'product_id': product.id, 'quantity': 1})
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

    def test_update_cart_item(self):
        client = APIClient()
        cart = Cart.objects.create()
        collection = Collection.objects.create(title="c")
        product = Product.objects.create(title='p', inventory=100, unit_price=10,collection=collection)
        item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        response = client.patch(f'/store/carts/{cart.id}/items/{item.id}/', {'quantity': 2})
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['quantity'] == 2