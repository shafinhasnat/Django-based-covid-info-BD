from django.db import models

# Create your models here.
class CovidData(models.Model):
	date = 	models.CharField(max_length=50)
	case = 	models.IntegerField()
	death = models.IntegerField()
	recover = models.IntegerField()
	def __str__(self):
		return str(self.date)+" | "+str(self.case)+" | "+str(self.death)+" | "+str(self.recover)