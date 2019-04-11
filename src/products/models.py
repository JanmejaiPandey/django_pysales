from django.db import models
import os
import random

def get_filename_ext(filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name , ext

def upload_image_path(instance , filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1,397625012)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'
    
class product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=20,default = 39.99)
    image = models.ImageField(upload_to="products/", null=True, blank=True )

    def __str__(self):
        return self.title
