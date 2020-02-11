from django.db import models

# Create your models here.
class Project(models.Model):
	"""docstring for Project"""
	title = models.CharField(max_length = 100)
	description = models.TextField()
	technology = models.CharField(max_length= 20)
	image = models.FilePathField(path = "/img")

	# def __init__(self, arg):
	# 	super(Project, self).__init__()
	# 	# self.arg = arg
	# 	