from django.db import models
from django_google_maps import fields as map_fields
from django.core.exceptions import ValidationError
import re

class PortfolioEntry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='portfolio_photos/', null=True, blank=True)
    video = models.FileField(upload_to='portfolio_videos/', null=True, blank=True)

    # Google Maps fields
    address = map_fields.AddressField(max_length=200, default='Ireland')
    geolocation = map_fields.GeoLocationField(
        max_length=100,
        default='53.3522908033196,-6.257729843109473',
        blank=True
    )

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Portfolio Entries'

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.geolocation:
            # Using regular expressions from SI206
            coord_pattern = r'^-?\d+\.?\d*,-?\d+\.?\d*$'

            if not re.match(coord_pattern, str(self.geolocation)):
                raise ValidationError({
                    'geolocation': 'Geolocation must be in format "latitude,longitude" (e.g., "63.984851,-22.625563")'
                })

            try:
                lat, lng = str(self.geolocation).split(',')
                lat = float(lat)
                lng = float(lng)

                # Validate latitude range
                if not -90 <= lat <= 90:
                    raise ValidationError({
                        'geolocation': 'Latitude must be between -90 and 90 degrees'
                    })

                # Validate longitude range
                if not -180 <= lng <= 180:
                    raise ValidationError({
                        'geolocation': 'Longitude must be between -180 and 180 degrees'
                    })

                # 6 decimal places
                self.geolocation = f"{lat:.6f},{lng:.6f}"

            except (ValueError, TypeError):
                raise ValidationError({
                    'geolocation': 'Invalid coordinate format. Must be two decimal numbers separated by a comma.'
                })