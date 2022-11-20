from books.models import Book, Category, Author
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from checkout.models import Order

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

        self.my_admin = User.objects.create_superuser(username= 'myemail@test.com',password= 'mypassword')
        self.my_admin.save()

    def test_cache_checkout_data_sucess_200(self):
        """
        View checkout, parametes
        """
        response = self.client.post(reverse('cache_checkout_data'), data={'client_secret':'pi_3M5yYaAqyUAdlutt0EqCCs5Z_secret_RlAGjaO9t8n7uX44mIgp0Yp4C'})
        self.assertEqual(response.status_code, 200, response)

    def test_cache_checkout_erro_400(self):
        """
        View checkout, not parametes error
        """
        response = self.client.post(reverse('cache_checkout_data'))
        self.assertEqual(response.status_code, 400, response)


    def test_checkout_erro_302(self):
        """
        View checkout, not parametes error
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302, response)
        self.assertEqual(response.url, '/', response)

    def test_checkout_form(self):
        """
        View checkout, form checkout
        """
        response = self.client.post(reverse('checkout'), data={'full_name': 'RENAN+RIBEIRO+LAGE',
        'email': 'renan.lagee@gmail.com', 'phone_number': '31989791428', 
        'street_address1': 'Rua+francisco+ovidio+227', 'street_address2': 'ap2',
        'town_or_city': 'Belo+Horizonte', 'county': 'MG', 'postcode': '30770040', 
        'country': 'BR', 'save-info': 'on',
        'client_secret': 'pi_3M5yYaAqyUAdlutt0EqCCs5Z_secret_RlAGjaO9t8n7uX44mIgp0Yp4C'})
        self.assertEqual(response.status_code, 302, response)
        self.assertIn('/checkout/checkout_success/', response.url)

    def test_checkout_sucess_ordem_not_pass(self):
        """
        View checkout, checkout sucess order not parameter invalid
        """

        response = self.client.get(reverse('checkout_success', kwargs={'order_number': 9898989}))
        self.assertEqual(response.status_code, 404, response)

    def test_checkout_sucess_ordem_pass_sucess(self):
        """
        View checkout, checkout sucess order valid
        """

        order = Order.objects.create(
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

        response = self.client.get(reverse('checkout_success', kwargs={'order_number': order.order_number}))
        self.assertEqual(response.status_code, 200, response)
