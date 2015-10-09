from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Product(models.Model):
	pname = models.CharField(max_length=200)
	pdesc = models.CharField(max_length=200,null=True,blank=True)
	pstatus = models.BooleanField(default=True)
	pdate = models.DateTimeField('add date',default=datetime.datetime.now)
	
	def was_published_recently(self):
		return self.pdate >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pdate'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	def __str__(self):
		return '%s : %s' % (self.pname,self.pdesc)
 
class Ingredient(models.Model):
	product = models.ForeignKey(Product)
	iname = models.CharField(max_length=200)
	idesc = models.CharField(max_length=200,null=True,blank=True)

	def __str__(self):
		return '%s : %s' % (self.iname,self.idesc)
 