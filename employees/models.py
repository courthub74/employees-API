from django.db import models


class Employee(models.Model):
	idcode = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	emptype = models.CharField(max_length=100)
	empstatus = models.CharField(max_length=20)
	datejoin = models.CharField(max_length=20)
	jobdescrp = models.CharField(max_length=200)
	branch = models.CharField(max_length=100)
	photo = models.ImageField(null=True, blank=True, upload_to="images/")

	def __str__(self):
		return self.idcode