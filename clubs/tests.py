from django.test import TestCase
from .models import Whiskey_club, Subscription_type

class TestViews(TestCase):


    def test_whiskey_club(self):
            response = self.client.get('/whiskey_clubs/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'clubs/whiskey_clubs.html')

   

    
