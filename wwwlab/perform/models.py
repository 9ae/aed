from django.db import models

# Create your models here.

class Experiment(models.Model):
	time_start = models.TimeField()
	time_complete = models.TimeField(null=True, blank=True)
	trials_completed = models.IntegerField(default=0)

class Trial(models.Model):
	experiment = models.ForeignKey(Experiment)
	time_start = models.TimeField()
	duration = models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
	completed = models.BooleanField()

class Event(models.Model):
	trial = models.ForeignKey(Trial)
	trial_time_occurred = models.DecimalField(max_digits=8, decimal_places=3)
	action_name = models.CharField(max_length=16)
