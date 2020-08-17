from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Product(models.Model):
	pdt_name=models.TextField()
	pdt_price=models.TextField()
	pdt_cat=models.TextField()
class Category(models.Model):
	cat_name=models.TextField()
	cat_gst=models.TextField()
class Invoice(models.Model):
	pname=models.TextField()
	qty=models.TextField()
	unitprice=models.TextField()
	cname=models.TextField()
	cnumber=models.TextField()
	gst=models.TextField()
	dis=models.TextField()
	total=models.TextField()
class Import(models.Model):
	pdt_name=models.TextField()
	qty=models.TextField()
	