from django import forms
from django.contrib.admin import widgets
from django.db import models


# Create your models here.

class Section(models.Model):
    title=models.CharField(max_length=150)
    def __str__(self):
        return self.title


class SubSection(models.Model):
    title=models.CharField(max_length=150)
    section=models.ForeignKey(Section)
    def __str__(self):
        return self.title

class User(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=500)
    firstName=models.CharField(max_length=150)
    lastName=models.CharField(max_length=150)
    address=models.TextField()
    tel=models.CharField(max_length=20)
    email=models.CharField(max_length=150)
    class Meta:
        abstract = True

    def __str__(self):
        return self.username

class Merchant(User):
    sell_amount=models.PositiveIntegerField()



class Customer(User):
    favorite=models.TextField()


class Product(models.Model):
    name=models.CharField(max_length=150)
    price=models.PositiveIntegerField()
    picture=models.ImageField(upload_to="product_pic/")
    score=models.PositiveIntegerField()
    details=models.TextField()
    createDate=models.DateTimeField()
    subSection=models.ForeignKey(SubSection)
    merchant=models.ForeignKey(Merchant)
    def __str__(self):
        return self.name



class SlideshowProduct(models.Model):
    text=models.CharField(max_length=500)
    SlideshowPic=models.ImageField(upload_to="slideshow/")
    product=models.ForeignKey(Product)
    def __str__(self):
        return self.product.name


class Comment(models.Model):
    content=models.TextField()
    customer=models.ForeignKey(Customer)
    product=models.ForeignKey(Product)
    def __str__(self):
        return self.content

class Bill(models.Model):
    customer=models.ForeignKey(Customer)
    paidFlag=models.BooleanField()
    price=models.PositiveIntegerField()
    product=models.ManyToManyField(Product)
    def __str__(self):
        return self.customer.username + str(self.id)




