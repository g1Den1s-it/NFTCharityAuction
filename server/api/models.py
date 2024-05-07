from django.db import models

# Create your models here.
class MetadataNFT(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    # attributes
    value = models.IntegerField()
    
    def __str__(self):
        return self.name