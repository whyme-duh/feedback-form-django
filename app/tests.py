from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.urls import reverse
from app.forms import FeedbackFormField
from app.models import FeedbackForm

class FeedbackFormCreationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username = "test", 
            email = "test@gmail.com", 
            password = "Testing@123", 
            )
        
    # this function is to test whether the operation fails when the user does not fill all necessary fields
    def test_form_validation_fails_with_missing_constraints(self):
        
        incomplete_data = {
            'full_name': 'Ritik Lal Shreestha',
            'bed_no': 12,
        }
        
        form = FeedbackFormField(data=incomplete_data)
        
        self.assertFalse(form.is_valid())

    # this function checks whether the anonymous user is redirected to home page when accessing profile page
    def test_profile_requires_account(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        





