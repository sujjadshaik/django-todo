from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import *

class TestUrls(SimpleTestCase):
    def test_url_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, CustomLoginView)
    def test_url_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterPage)
    def test_url_task(self):
        url = reverse('task-create')
        self.assertEquals(resolve(url).func.view_class, TaskCreate)



