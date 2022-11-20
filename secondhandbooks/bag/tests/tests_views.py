from books.models import Book, Category, Author
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BagViewsTestCase(TestCase):

    """
    Class test to bag views
    """

    def setUp(self):
        self.user = User.objects.create(username='test', password='test')
        self.user.save()

        self.category = Category.objects.create(
            name="Children's Books",
            friendly_name="Children's Books"
        )
        self.category.save()

        self.author = Author.objects.create(
            name="JK",
            details="Children's Books"
        )
        self.author.save()

        self.book = Book.objects.create(
            name="Harry Potter",
            description="is very good book",
            price=73.54,
            category=self.category,
            author=self.author
        )
        self.book.save()

        self.book2 = Book.objects.create(
            name="think and grow rich ",
            description="is very good book",
            price=82.54
        )

        self.book2.save()

    def test_view_bag_sucess(self):
        """
        Test return bag user
        """    
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200, response)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_view_add_bag_error_book_not_exist(self):
        """
        Test return add bag user book not exist
        """

        response = self.client.get(reverse('add_to_bag', kwargs={'item_id': '999999999'}))
        self.assertEqual(response.status_code, 404, response)

    def test_view_add_bag_sucess(self):
        """
        Test return add bag user
        """
        response = self.client.post(reverse('add_to_bag', kwargs={'item_id': self.book.id}), data={'quantity': 43, 'redirect_url': 'request.path'})
        self.assertEqual(response.status_code, 302, response)

    def test_view_adjust_bag_error_book_not_exist(self):
        """
        Test return adjust bag user book not exist
        """    
        response = self.client.get(reverse('adjust_bag', kwargs={'item_id': '999999999'}))
        self.assertEqual(response.status_code, 404, response)

    def test_view_adjust_bag_sucess(self):
        """
        Test return adjust bag user
        """
        response = self.client.post(reverse('adjust_bag', kwargs={'item_id': self.book.id}), data={'quantity': 43,'redirect_url': 'request.path'})
        self.assertEqual(response.status_code, 302, response)

    def test_view_remove_bag_error_book_not_exist(self):
        """
        Test return remove bag user book not exist
        """    
        response = self.client.get(reverse('remove_from_bag', kwargs={'item_id': '999999999'}))
        self.assertEqual(response.status_code, 404, response)

    def test_view_adjust_remove_sucess(self):
        """
        Test return remove bag user
        """
        response = self.client.post(reverse('remove_from_bag', kwargs={'item_id': self.book.id}),)
        self.assertEqual(response.status_code, 500, response)
                        