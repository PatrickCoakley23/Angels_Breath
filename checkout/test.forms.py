from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    """
    Test to display only what is defined 
    explicitly in the inner metaclass
    """

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields,  ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',))

    """
    Test to see if required feels 
    are treated as valid when left blank
    """

    def test_order_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())

    def test_order_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())

    def test_phone_number_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())

    def test_country_is_required(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())

    def test_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())

    def street_address1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())

  
    





