import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Product

# Create your tests here.

class PorductMethodTests(TestCase):

	def test_was_published_recently_with_future_product(self):
		"""
		was_published_recently() should return False for questions whose
		pub_date is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_product = Product(pdate=time)
		self.assertEqual(future_product.was_published_recently(), False)
	def test_was_published_recently_with_old_product(self):
		"""
		was_published_recently() should return False for questions whose
		pub_date is older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=30)
		old_product = Product(pdate=time)
		self.assertEqual(old_product.was_published_recently(), False)

	def test_was_published_recently_with_recent_product(self):
		"""
		was_published_recently() should return True for questions whose
		pub_date is within the last day.
		"""
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_product = Product(pdate=time)
		self.assertEqual(recent_product.was_published_recently(), True)