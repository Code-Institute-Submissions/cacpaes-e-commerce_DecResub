from django.test import TestCase
from books.forms import ReviewForm, BookForm
from books.models import Category

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


"""
class to test form BookForm
"""
class BookFormTestCase(TestCase):

    def setUp(self):

        """
        Create setup book form
        """
        self.category = Category.objects.create(
            name="Children's Books",
            friendly_name="Children's Books"
        )

        self.category.save()

    def test_book_form_valid(self):
        """
        Check if the form is valid
        """
        form = BookForm(data={
            'name': 'Harry Potter',
            'description': 'The best book',
            'price': 70
        })
        self.assertTrue(form.is_valid())

    def test_book_form_invalid_skip_value_name(self):
        """
        Check if the form is invalid, parameter name blank
        """
        form = BookForm(data={
            'description': 'The best book',
            'price': 70
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_book_form_invalid_description(self):
        """
        Check if the form is invalid, parameter description none
        """
        form = BookForm(data={
            'name': 'Harry Potter',
            'price': 70
        })
        self.assertFalse(form.is_valid(), form.errors)


    def test_book_form_invalid_price_none(self):
        """
        Check if the form is invalid, parameter price none
        """
        form = BookForm(data={
            'name': 'Harry Potter',
            'description': 'The best book',
        })
        self.assertFalse(form.is_valid(), form.errors)    
