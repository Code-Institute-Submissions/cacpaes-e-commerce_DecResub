from books.models import Book, Category, Author
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

        self.my_admin = User.objects.create_superuser(username='myemail@test.com', password='mypassword')
        self.my_admin.save()

    def test_all_books_sucess_200(self):
        """
        View return all books, not parametes
        """
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200, response)
        self.assertTemplateUsed(response, 'books/books.html')

    def test_detail_book_sucess_200(self):
        """
        View return details book
        """
        response = self.client.get(reverse('book_detail', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 200, response)
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_detail_book_error_404(self):
        """
        View return error book 404
        """
        response = self.client.get(reverse('book_detail', kwargs={'book_id': '999999999'}))
        self.assertEqual(response.status_code, 404, response)

    def test_add_book_not_permission(self):
        """
        View return error add book user not permission 403, reponse redirect
        """
        response = self.client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 302, response)

    def test_edit_book_not_permission(self):
        """
        View return error edit book user not permission 403, reponse redirect
        """
        response = self.client.get(reverse('edit_book', kwargs={'book_id': '999999999'}))
        self.assertEqual(response.status_code, 302, response)

    def test_delete_book_not_permission(self):
        """
        View return error delete book user not permission 403, reponse redirect
        """
        response = self.client.get(reverse('delete_book', kwargs={'book_id': '999999999'}))
        self.assertEqual(response.status_code, 302, response)

    def test_delete_book_sucess(self):
        """
        View return delete book
        """
        self.client.login(username='myemail@test.com', password='mypassword')
        book = Book.objects.get(id=self.book.id)
        self.assertIsNotNone(book)
        response = self.client.get(reverse('delete_book', kwargs={'book_id': self.book.id}))
        self.assertEqual(response.status_code, 302, response)
        book = Book.objects.filter(id=self.book.id).first()
        self.assertIsNone(book)     