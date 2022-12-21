from django.db import models

# Create your models here.
# notes model
class Notes(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)