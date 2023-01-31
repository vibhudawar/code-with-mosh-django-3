from store.models import Collection
from rest_framework import status
import pytest
from .conftest import *
from model_bakery import baker


# Test for CREATING collections
# fixture to replace repeating code [response = api_client.post('/store/collections/', {'title': 'a'})]
@pytest.fixture
def create_collection(api_client):
    # we are defining the collection in inside function because if we pass collection as the second argument in create_collection function, then it will think collection as a fixture, and not as parameter, therefore, we are required to do that like
    def do_create_collection(collection):
        # to send the response
        return api_client.post('/store/collections/', collection)
    return do_create_collection


# to skip a test, just decorate the method with @pytest.mark.skip


# following conventions
@pytest.mark.django_db
class TestCreateCollections:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        # test is made up of (AAA) ie Arrange, Act, and Assert
        
        # Arrange (BLANK HERE)
        
        # Act
        response = create_collection({'title': 'a'})
        
        # Assertion part
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_user_is_not_admin_returns_403(self, create_collection):
        # Act
        authenticate(is_staff=False)
        response = create_collection({'title': 'a'})
        
        # Assertion part
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_data_is_invalid_returns_400(self, create_collection):
        # Act
        authenticate(is_staff=True)
        response = create_collection({'title': ''})
        
        # Assertion part
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, create_collection):
        # Act
        authenticate(is_staff=True)
        response = create_collection({'title': 'a'})
        
        # Assertion part
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Test for RETRIEVING collections

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self, api_client):
        # Arrange
        # this will create the collection and will fill the fields with random values
        collection = baker.make(Collection) 
        
        # Act
        response = api_client.get(f'/store/collections/{collection.id}/')

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }
        
