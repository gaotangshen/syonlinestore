from django.db import models

# Create your models here.
class Products(models.Model):
	pname = models.CharField(max_length=200)
	pdesc = models.CharField(max_length=200)
	pstatus = models.BooleanField(default=True)

