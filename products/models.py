from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
	username = models.CharField(max_length=100)
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	tuto_url = models.URLField()
	created_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('product_detail', kwargs={'pk':str(self.id)})