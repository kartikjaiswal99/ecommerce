from django.contrib.auth.models import User
from rest_framework import status
import pytest
from store.models import Product,Collection
from model_bakery import baker

@pytest.fixture
def create(api_client):
    def do_create(collection):
        return api_client.post('/store/collections/',collection)
    return do_create


@pytest.mark.django_db
class TestCollection:
    def test_anonymous(self,create):
        response = create({'title':'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_not_admin(self,create,authenticate):
        authenticate()
        response = create({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_collections(self,api_client):
        response = api_client.get('/store/collections/')
        
        assert response.status_code == status.HTTP_200_OK

    def test_collection_invalid(self,authenticate,create):
        authenticate(is_staff=True)
        response = create({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_create_collection(self,authenticate,create):
        authenticate(is_staff=True)
        response = create({'title':'a'})
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

    def test_delete_collection(self,api_client,authenticate):
        authenticate(is_staff=True)
        # collection = Collection.objects.create(title='c')
        collection = baker.make(Collection)
        response = api_client.delete(f'/store/collections/{collection.id}/')
        
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_collection_with_products(self,api_client,authenticate):
        authenticate(is_staff=True)
        collection = baker.make(Collection)
        product = baker.make(Product,collection=collection)
        response = api_client.delete(f'/store/collections/{collection.id}/')
        
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response.data['error'] == 'Collection cannot be deleted because it includes one or more products.'


