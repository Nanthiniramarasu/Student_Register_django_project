from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from Myapplication.models import Data

# ---------------------------
# CRUD Tests
# ---------------------------
class DataModelTest(TestCase):

    def setUp(self):
        # Create a test record
        self.data = Data.objects.create(
            name="Test User",
            contact="1234567890",
            address="Test Address",
            mail="test@example.com"
        )

    def test_data_creation(self):
        """Test if Data object is created successfully"""
        self.assertEqual(self.data.name, "Test User")
        self.assertEqual(self.data.contact, "1234567890")
        self.assertEqual(self.data.address, "Test Address")
        self.assertEqual(self.data.mail, "test@example.com")

    def test_data_str_method(self):
        """Test __str__ method returns name"""
        self.assertEqual(str(self.data), "Test User")


# ---------------------------
# Authentication Tests
# ---------------------------
class AuthTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()

    def test_login_page(self):
        """Test login page loads correctly"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_signup_page(self):
        """Test signup page loads correctly"""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_login_authentication(self):
        """Test login with correct credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertRedirects(response, reverse('Home'))

    def test_logout(self):
        """Test logout"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
