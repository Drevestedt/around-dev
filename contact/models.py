from django.db import models

class ContactRequest(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
