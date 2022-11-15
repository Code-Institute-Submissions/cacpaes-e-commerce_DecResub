from django.test import TestCase
from books.forms import ReviewForm


"""
class to test form ReviewForm
"""
class ReviewFormTestCase(TestCase):

    def test_review_form_valid(self):
        """
        Check if the form is valid
        """
        form = ReviewForm(data={
            'review': 1,
        })
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_skip_value_review(self):
        """
        Check if the form is invalid, parameter name not review
        """
        form = ReviewForm(data={
            'review': None,
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_review_form_invalid_review_negative(self):
        """
        Check if the form is invalid, parameter review value negative
        """
        form = ReviewForm(data={
            'review': -5,
        })
        self.assertFalse(form.is_valid(), form.errors)


    def test_review_form_invalid_review_value_greather_than_five(self):
        """
        Check if the form is invalid, parameter review value greather than 5 
        """
        form = ReviewForm(data={
            'review': 10,
        })
        self.assertFalse(form.is_valid(), form.errors)    
