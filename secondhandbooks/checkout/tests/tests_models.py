from django.contrib.auth.models import User
from django.test import TestCase
from books.models import Book
from checkout.models import Order, OrderLineItem
import uuid

"""
class to test model Order
"""


class OrderTestCase(TestCase):


    def setUp(self):

        """
        Defined function before condition for test
        """

        self.uuid_number = uuid.uuid4()

        self.user = User.objects.create(username='test', password='test')

        self.user.save()
        user2 = User.objects.create(username='test2', password='test2')

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

    def test_order_return_str(self):
        """
        Test string for Order
        """
        order = Order.objects.get(order_number=self.uuid_number)
        self.assertEquals(order.__str__(), str(self.uuid_number))

"""
class to test model Order Line Item
"""


class OrderLineItemTestCase(TestCase):

    def setUp(self):
        """
        Defined function before condition for test
        """

        self.uuid_number = uuid.uuid4()

        self.user = User.objects.create(username='test', password='test')

        self.user.save()

        self.book = Book.objects.create(
            name="Harry Potter",
            description="is very good book",
            price=73.54,
        )
        self.book.save()

        self.order = Order.objects.create(
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
        self.order.save()

        order_line_item = OrderLineItem.objects.create(
            book=self.book,
            order=self.order,
            lineitem_total=5,
            quantity=12
        )

    def test_order_line_item_return_str(self):
        """
        Test string for OrderLineItem
        """
        order = OrderLineItem.objects.get(book=self.book)
        self.assertEquals(order.__str__(), f'SKU {self.book.sku} on order {self.order.order_number}')
