from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from profiles.models import UserProfile
from checkout.models import Order
from books.models import Book, Category, Author
import uuid


class ProfilesViewsTestCase(TestCase):

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

        self.my_admin = User.objects.create_superuser(username= 'myemail@test.com',password= 'mypassword')
        self.my_admin.save()

        self.uuid_number = uuid.uuid4()

        order = Order.objects.create(
            order_number=self.uuid_number,
            full_name="Carlos",
            email="teste@gmail.com",
            phone_number="989791428",
            country="ireland",
            town_or_city="Dublin",
            street_address1="grafton street",
            delivery_cost=20,
            order_total=45,
            grand_total=65,
            original_bag="bag",
            stripe_pid="9898"
        )

    def test_order_history_profile_not_found(self):
        """
        View Profiles, return order history error 404 
        """

        response = self.client.get(reverse('order_history', kwargs={'order_number':9898989}))
        self.assertEqual(response.status_code, 404, response)    

    def test_order_history_profile_sucess(self):
        """
        View Profiles, return order history error 200 
        """

        response = self.client.get(reverse('order_history', kwargs={'order_number':self.uuid_number}))
        self.assertEqual(response.status_code, 200, response)

    def test_return_profile(self):
        """
        View Profiles, return profile 
        """

        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302, response)        
