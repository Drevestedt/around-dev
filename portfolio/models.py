from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to="projects/")
  link = models.URLField(blank=True, null=True)
  featured = models.BooleanField(default=False)