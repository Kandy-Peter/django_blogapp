from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog.models import Category, Post

class PosTests(APITestCase):
  
  def tes_view_post(self):
    
    url = reverse("blog_api:listcreate")
    response = self.client.get(url, format='json')
    #use of client for simulating a client(browser). get the url and display it in json format
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  def create_post(self):
    self.test_category = Category.objects.create(name='django')
    
    self.testuser1 = User.objects.create_user(
      username='test_user1', password='12345678'
    )
    data = {
      "title": "new", "author": 1, "excerpt": "new", "content": "new"
    }
    url = reverse("blog_api:listcreate")
    response = self.client.get(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
