from django.db import models

# Create your models here.
class Pizza(models.Model):
	name = models.CharField(max_length=20)
	thumb = models.ImageField(blank=False)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	date = models.DateTimeField(auto_now_add=True)
	#add buyer later

	def __str__(self):
		return self.name