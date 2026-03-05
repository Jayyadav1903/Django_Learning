from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class biryani_variety(models.Model):
    biryani_types=[
        ("Hybd","Hyderabadi"),
        ("Luck","Lucknowi"),
        ("Kol","Kolkata"),
        ("Amb","Ambur"),
        ("Din","Dindigul")
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="biryani/images")
    date_added=models.DateTimeField(default=timezone.now)
    types=models.CharField(max_length=20,choices=biryani_types)
    description=models.TextField(default='')
    def __str__(self):
        return self.name


# one to many relationship     
class review(models.Model):
    biryani=models.ForeignKey(biryani_variety,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=[
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5")
    ]
    ratings=models.IntegerField(choices=rating)
    comment=models.TextField(default='')
    date_added=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Review of {self.biryani.name} by {self.user.username}"
    
#Many to many relationship

class store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    biryani=models.ManyToManyField(biryani_variety, related_name='stores')
    
    def __str__(self):
        return self.name

#One to one relationship

class Biryani_Certificate(models.Model):
    biryani=models.OneToOneField(biryani_variety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    date_issued=models.DateTimeField(default=timezone.now)
    valid_until=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Certificate for {self.biryani.name}"
     