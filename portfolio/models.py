from django.db import models

# Create your models here.

class PortfolioEntry(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    google_map_embed = models.TextField(
        default='<iframe src="https://www.google.com/maps/embed?..."></iframe>'
    )
    photo = models.ImageField(upload_to='portfolio_photos/', blank=True, null=True)
    video = models.FileField(upload_to='portfolio_videos/', blank=True, null=True)

    def __str__(self):
        return self.title
