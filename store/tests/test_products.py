from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
import pytest
from store.models import Collection, Product, OrderItem,Customer, Order

User=get_user_model()

@pytest.mark.django_db
class TestProduct:
    def test_list_products(self):
        client = APIClient()
        response = client.get('/store/products/')

        assert response.status_code == status.HTTP_200_OK

    def test_create_product_unauthorized(self):
        client = APIClient()
        response = client.post('/store/products/', {'title': 'p', 'unit_price': 10, 'inventory': 100})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_product_forbidden(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/products/', {'title': 'p', 'unit_price': 10, 'inventory': 100})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_product(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        collection = Collection.objects.create(title="c")
        response = client.post('/store/products/', {
            'title': 'p', 
            'slug':'p',
            'unit_price': 10, 
            'inventory': 100, 
            'collection': collection.id
        })

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

    def test_delete_product(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        collection = Collection.objects.create(title="c")
        product = Product.objects.create(title='p', unit_price=10, inventory=100, collection=collection)
        response = client.delete(f'/store/products/{product.id}/')
        
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_update_product(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))

        collection = Collection.objects.create(title="c")
        product = Product.objects.create(title='t', unit_price=10, inventory=100, collection=collection)

        response = client.put(
            f'/store/products/{product.id}/',
            {
                'title': 't',
                'slug': 't',
                'inventory': 150, 
                'collection': collection.id,
                'unit_price': 20
            }
        )
        assert response.status_code == status.HTTP_200_OK