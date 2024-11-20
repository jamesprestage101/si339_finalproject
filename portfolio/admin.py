from django.contrib import admin
from .models import PortfolioEntry
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class PortfolioEntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={
                'data-map-type': 'roadmap'  # Optional: sets default map type to roadmap
            })
        },
        map_fields.GeoLocationField: {
            'widget': map_widgets.GoogleMapsAddressWidget
        },
    }
    list_display = ('title', 'date', 'address')
    search_fields = ('title', 'description', 'address')
    readonly_fields = ('geolocation',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'date', 'photo', 'video')
        }),
        ('Location', {
            'fields': ('address', 'geolocation'),
            'description': 'Enter the address and the geolocation will be automatically populated'
        }),
    )

admin.site.register(PortfolioEntry, PortfolioEntryAdmin)
