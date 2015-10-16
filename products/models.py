from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Product(models.Model):
	pname = models.CharField(max_length=200)
	pdesc = models.CharField(max_length=200,null=True,blank=True)
	pstatus = models.BooleanField(default=True)
	pdate = models.DateTimeField('add date',default=datetime.datetime.now)
	pimage = models.FileField(upload_to='files/%Y/%m/%d/',max_length=100,null=True,blank=True)
	
	def was_published_recently(self):
		now = timezone.now();
		return now >= self.pdate >= timezone.now() - datetime.timedelta(days=1)
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
 