from books.models import Book, Category
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BookingViewsTestCase(TestCase):

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

        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

    def all_books_sucess_200(self):
        """
        View return all books, not parametes
        """
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200, response)
        self.assertTemplateUsed(response, 'books/books.html')

    def detail_book_sucess_200(self):
        """
        View return details book
        """
        response = self.client.get(reverse('book_detail', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 200, response)
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def detail_book_error_404(self):
        """
        View return error book 404
        """
        response = self.client.get(reverse('book_detail', kwargs={'book_id': '999999999'}))
        self.assertEqual(response.status_code, 404, response)

    def add_book_not_permission(self):
        """
        View return error add book user not permission 403
        """
        response = self.client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 403, response)

    def edit_book_not_permission(self):
        """
        View return error edit book user not permission 403
        """
        response = self.client.get(reverse('edit_book'))
        self.assertEqual(response.status_code, 403, response)

    def delete_book_not_permission(self):
        """
        View return error delete book user not permission 403
        """
        response = self.client.get(reverse('delete_book'))
        self.assertEqual(response.status_code, 403, response)