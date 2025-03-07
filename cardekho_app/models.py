from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Showeroom_model(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    website=models.URLField(max_length=100)
    # cars=models.ForeignKey(Carlist,on_delete=models.CASCADE,related_name="Carlist")

    def __str__(self):
        return self.name
    

class Carlist(models.Model):
    name=models.CharField(max_length=50)
    descriptions=models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    chassinumber=models.CharField(max_length=100,blank=True,null=True)
    price=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True) 
    showroom=models.ForeignKey(Showeroom_model,on_delete=models.CASCADE,related_name="showroom",null=True)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(validators=[MaxValueValidator,MinValueValidator])
    comment=models.CharField(max_length=200,null=True)
    car=models.ForeignKey(Carlist,on_delete=models.CASCADE,related_name="reviews")
    create=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)



    def __str__(self):
        return "the rating of "+self.car.name +"----"+str(self.user_name)
    