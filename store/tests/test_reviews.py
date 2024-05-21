from rest_framework.test import APIClient
from rest_framework import status
import pytest
from store.models import Product,Collection

@pytest.mark.django_db
class TestReview:
    def test_list_reviews(self):
        client = APIClient()
        collection = Collection.objects.create(title="c")
        product = Product.objects.create(title='p', slug='p',inventory=100, unit_price=10,collection=collection)
        response = client.get(f'/store/products/{product.id}/reviews/')
        
        assert response.status_code == status.HTTP_200_OK

    def test_create_review(self):
        client = APIClient()
        collection = Collection.objects.create(title="c")
        product = Product.objects.create(title='p', inventory=100, unit_price=10,collection=collection)
        response = client.post(f'/store/products/{product.id}/reviews/', {'name': 'Review 1', 'description': 'Good product'})
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0