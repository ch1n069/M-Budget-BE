from django.db import models

# Create your models here.
# notes model
class Notes(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title