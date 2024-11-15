from django.test import TestCase
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

# Create your tests here.
@pytest.mark.django_db
def test_create_customer():
    client = APIClient()
    client.login(username='admin', password='admin') # Update as needed
    response = client.post(reverse('customer-list'), {'name': 'Test', 'code': '001'})
    assert response.status_code == 201