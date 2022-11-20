from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import  reverse

class Category(models.Model):
    """
    Entity Category
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Author(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    details = models.CharField(max_length=1024, null=True, blank=True)
    site_url = models.URLField(max_length=1024, null=True, blank=True) 

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Entity books
    """

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, null=True,blank=True, 
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    special = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField(default=0, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    site_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id})    


class Review(models.Model):
    """
    Entity Review
    """
    REVIEW_VALUE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="book_review"
        )
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300, null= True, blank=True)
    reviewed = models.BooleanField(default=True)
    review = models.IntegerField(choices=REVIEW_VALUE, default=5)
    

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return str(self.book)
