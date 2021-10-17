from django.db import models

# Create your models here.

class URL(models.Model):
    id = models.AutoField(primary_key=True)
    original_url = models.URLField(max_length=500, null=True)
    generated_url = models.URLField(max_length=100, null=True)

    def __str__(self):
        return self.original_url