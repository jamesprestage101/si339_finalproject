from django.db import models

# Create your models here.

class PortfolioEntry(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    google_map_url = models.URLField(max_length=500)
    photo = models.ImageField(upload_to='portfolio_photos/')

    def __str__(self):
        return self.title