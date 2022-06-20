from django.db import models

# Create your models here.
class CallbackRequest(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    phone = models.CharField(max_length=35, null=False, blank=False)
    comment = models.CharField(max_length=850, null=True, blank=True, default="NA")
    request_date = models.DateTimeField(auto_now_add=True, blank=True)    
    
    def __str__(self):
        return self.name
