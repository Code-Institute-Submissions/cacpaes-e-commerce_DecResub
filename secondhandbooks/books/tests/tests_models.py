from django.contrib.auth.models import User
from django.test import TestCase
from books.models import Review, Book



"""
class to test model Review
"""


class ReviewTestCase(TestCase):


    def setUp(self):
        """
        Defined function before condition for test
        """


        user = User.objects.create(username='test', password='test')

        user2 = User.objects.create(username='test2', password='test2')

        book = Book.objects.create(
            username=user,
            nome="Harry Potter",
            description="is very good book",
            price=73.54
        )

        book2 = Book.objects.create(
            username=user,
            nome="think and grow rich ",
            description="is very good book",
            price=82.54
        )

        Review.objects.create(
            user=user
            book=book,
            review=4
        )

        Review.objects.create(
            user=user2
            book=book,
            review=5
        )

    def test_review_return_str(self):
        """
        Test string for review
        """
        review = Review.objects.get(user=user)
        self.assertEquals(review.__str__(), "Harry Potter")

    def test_confirm_data(self):
        """
        Test confirm objects atributes
        """
        review = Review.objects.get(user=user)
        self.assertEquals(review.review, 5)
        self.assertEquals(review.reviewed, True)

    def test_review_orderind(self):
        """
        Test ordering review
        """
        reviews = Review.objects.all()
        self.assertEquals(reviews[0].review, 4)
        self.assertEquals(reviews[1].review, 5)
        self.assertGreater(reviews[0].created_on, reviews[1].created_on)