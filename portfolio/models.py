from django.db import models

# Create your models here.

class PortfolioEntry(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    google_map_embed = models.TextField(
        default='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2436871.009462155!2d-8.09925505!3d53.383399999999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x485e619e5d73698f%3A0xca9b39444d6ac68d!2sIreland!5e0!3m2!1sen!2sus!4v1731986922851!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
    )
    photo = models.ImageField(upload_to='portfolio_photos/')

    def __str__(self):
        return self.title

