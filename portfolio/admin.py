from django.contrib import admin
from .models import PortfolioEntry
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class PortfolioEntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={
                'data-map-type': 'roadmap',  # Default map type to roadmap
                'data-autocomplete-options': '{"types": ["geocode"]}'  # Restrict autocomplete to geocoding
            })
        },
        map_fields.GeoLocationField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={
                'data-map-type': 'roadmap'  # Match the map type for consistency
            })
        },
    }

    list_display = ('title', 'date', 'address', 'geolocation')
    search_fields = ('title', 'description', 'address', 'geolocation')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'date', 'photo', 'video')
        }),
        ('Location', {
            'fields': ('address', 'geolocation'),
            'description': 'Enter the address, and the geolocation will be automatically populated, or adjust it manually.'
        }),
    )

admin.site.register(PortfolioEntry, PortfolioEntryAdmin)
