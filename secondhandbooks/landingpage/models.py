from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    # image = CloudinaryField('image')
    image = models.FileField(upload_to ='static/media/uploads/')
    details = models.CharField(max_length=1024) 

    def __str__(self):
        return self.name
    
class Books(models.Model):
    name = models.CharField(max_length=30, null=False , blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    value = models.FloatField(null=False, blank=False)
    # book_cover = CloudinaryField('image')
    book_cover = models.FileField(upload_to ='static/media/uploads/')
    synopsis = models.CharField(max_length=2048, null=False , blank=False)
    details = models.CharField(max_length=2048, null=False , blank=False)
    amount = models.IntegerField()
    

    def __str__(self):
        return self.name
