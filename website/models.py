from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=127)
    message = models.TextField()
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-created_date"]
        

class Newsletter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ["-created_date"]