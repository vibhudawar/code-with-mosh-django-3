from rest_framework.test import APIClient
import pytest

# define all the parts that are repetitive in the tests
# only define those, which are same for all the classes/functions
# if changes are there in the passing of object, then define this in the test_collection only
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate