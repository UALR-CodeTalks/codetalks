from django.db import models

class Presentation(models.Model):
	presHash = models.CharField(max_length = 40)
	presRank = models.IntegerField(default = 0)
	presMarkdown = models.TextField()
	presName = models.CharField(max_length = 60, default = 'name')
