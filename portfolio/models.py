from django.db import models
from django_google_maps import fields as map_fields
from django.core.exceptions import ValidationError

class PortfolioEntry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='portfolio_photos/', null=True, blank=True)
    video = models.FileField(upload_to='portfolio_videos/', null=True, blank=True)

    # Google Maps fields
    address = map_fields.AddressField(max_length=200, default='Ireland')
    geolocation = map_fields.GeoLocationField(max_length=100, default='53.3522908033196,-6.257729843109473')

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Portfolio Entries'

    def clean(self):
        super().clean()
        if self.geolocation:
            try:
                lat, lng = self.geolocation.split(',')
                float(lat)
                float(lng)
            except (ValueError, AttributeError):
                raise ValidationError({
                    'geolocation': 'Geolocation must be in format "latitude,longitude" (e.g., "53.350140,-6.266155")'
                })

    def __str__(self):
        return self.title