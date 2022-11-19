from django.test import TestCase
from checkout.forms import OrderForm
from checkout.models import Order
from django_countries.fields import CountryField
"""
class to test form OrderFormTestCase
"""
class OrderFormTestCase(TestCase):

    def test_order_form_valid(self):
        """
        Check if the form is valid
        """

        form = OrderForm(data={
            'full_name': 'jfkhadkfhds',
            'email':'carlos@gmail.com',
            'phone_number':'91265656532',
            'street_address1':'grafton street',
            'street_address2':'grafton street',
            'town_or_city':'Dublin',
            'postcode':'65655',
            'country':'NZ',
            'county':'Dublin',
        })
        self.assertTrue(form.is_valid())

    def test_checkout_form_invalid_skip_value_full_name(self):
        """
        Check if the form is invalid, parameter full name
        """
        form = OrderForm(data={
            'email':'carlos@gmail.com',
            'phone_number':'91265656532',
            'street_address1':'grafton street',
            'town_or_city':'Dublin',
            'postcode':'65655',
            'country':'NZ',
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_ordem_form_invalid_email(self):
        """
        Check if the form is invalid, parameter email
        """
        form = OrderForm(data={
            'full_name': 'jfkhadkfhds',
            'phone_number':'91265656532',
            'street_address1':'grafton street',
            'town_or_city':'Dublin',
            'postcode':'65655',
            'country':'NZ',
        })
        self.assertFalse(form.is_valid(), form.errors)


    def test_phone_number_form_invalid(self):
        """
        Check if the form is invalid, parameter phone number
        """
        form = OrderForm(data={
            'full_name': 'jfkhadkfhds',
            'email':'carlos@gmail.com',
            'street_address1':'grafton street',
            'town_or_city':'Dublin',
            'postcode':'65655',
            'country':'NZ',
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_country_number_form_invalid(self):
        """
        Check if the form is invalid, country phone number
        """
        form = OrderForm(data={
            'full_name': 'jfkhadkfhds',
            'phone_number':'91265656532',
            'email':'carlos@gmail.com',
            'street_address1':'grafton street',
            'town_or_city':'Dublin',
            'postcode':'65655',
        })
        self.assertFalse(form.is_valid(), form.errors)