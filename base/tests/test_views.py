from django.test import TestCase
from  django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.user = {
            'username':'testuser',
            'password1':'Password@123',
            'password2':'Password@123'
        }
        self.login_url = reverse('login')
        self.task_url = reverse('task-create')
        return super().setUp
class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'base/register.html')
    def test_can_user_register(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEquals(response.status_code,302)

class LoginTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'base/login.html')





