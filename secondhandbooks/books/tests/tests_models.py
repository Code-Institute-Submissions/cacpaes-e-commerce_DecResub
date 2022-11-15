from django.contrib.auth.models import User
from django.test import TestCase
from books.models import Review, Book, Category, Author



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
            user=user,
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


"""
class to test model Categoria
"""


class CategoriaTestCase(TestCase):


    def setUp(self):


        """
        Defined function before condition for test
        """


        user = User.objects.create(username='test', password='test')

        category_children = Category.objects.create(
            name="Children's Books",
            friendly_name="Children's Books"
        )

        category_health = Category.objects.create(
            name="Health",
            friendly_name="Health"
        )

        category_food = Category.objects.create(
            name="Food&Drink",
            friendly_name="Food&Drink"
        )

        category_crime = Category.objects.create(
            name="Crime, Thrillers&Mystery",
            friendly_name="Crime, Thrillers&Mystery"
        )

        book_children = Book.objects.create(
            username=user,
            nome="Harry Potter",
            description="is very good book",
            price=73.54,
            category=category_children
        )

        book_health = Book.objects.create(
            username=user,
            nome="think and grow rich ",
            description="is very good book",
            price=82.54,
            category=category_health
        )

        book_food = Book.objects.create(
            username=user,
            nome="think and grow rich ",
            description="is very good book",
            price=82.54,
            category=category_food
        )

        book_crime = Book.objects.create(
            username=user,
            nome="think and grow rich ",
            description="is very good book",
            price=82.54,
            category=category_crime
        )

    def test_cetegory_return_str(self):
        """
        Test string for cetegory
        """
        category = Category.objects.get(name="Children's Books")
        self.assertEquals(category.__str__(), "Children's Books")

    def test_confirm_data(self):
        """
        Test confirm objects atributes
        """
        category = Category.objects.get(name="Health")
        self.assertEquals(category.name, "Health")
        self.assertEquals(category.friendly_name, "Health")

    def test_get_book_category(self):
        """
        Test return books in filter category
        """
        category = Category.objects.get(name="Health")
        books = Book.objects.get(category=category)
        self.assertIsNotNone(book)

        Category.objects.delete(category)
        books = Book.objects.get(category=category)
        self.assertIsNone(book)        


"""
class to test model Author
"""


class AuthorTestCase(TestCase):


    def setUp(self):
        """
        Defined function before condition for test
        """


        user = User.objects.create(username='test', password='test')

        author = Author.objects.create(
            name="JK",
            details="Children's Books"
        )

        category_children = Category.objects.create(
            name="Children's Books",
            friendly_name="Children's Books"
        )

        book_children = Book.objects.create(
            username=user,
            nome="Harry Potter",
            description="is very good book",
            price=73.54,
            category=category_children,
            author=author
        )

    def test_author_return_str(self):
        """
        Test string for author
        """
        author = Authot.objects.get(name="JK")
        self.assertIsNotNone(author)
        self.assertEquals(author.__str__(), "JK")

    def test_confirm_data(self):
        """
        Test confirm objects atributes
        """
        author = Auhtor.objects.get(name="JK")
        self.assertEquals(author.name, "JK")
        self.assertEquals(author.details, "Children's Books")

    def test_get_book_author(self):
        """
        Test return books in filter author
        """
        author = Author.objects.get(name="JK")
        books = Book.objects.get(author=author)
        self.assertIsNotNone(book)

        Author.objects.delete(author)
        books = Book.objects.get(author=author)
        self.assertIsNone(book)     