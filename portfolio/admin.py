from django.contrib import admin
from .models import PortfolioEntry
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class PortfolioEntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={
                'data-map-type': 'roadmap',
                'data-autocomplete-options': '{"types": ["geocode"]}',
                'size': '40'
            })
        },
        map_fields.GeoLocationField: {
            'widget': admin.widgets.AdminTextInputWidget(attrs={
                'size': '40'
            })
        },
    }

    list_display = ('title', 'date', 'address', 'geolocation')
    search_fields = ('title', 'description', 'address')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'date', 'photo', 'video')
        }),
        ('Location', {
            'fields': ('address', 'geolocation'),
            'description': 'Enter the address and coordinates. Format: latitude,longitude (e.g., 63.984851,-22.625563)'
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.full_clean()  # This will trigger the validation
        super().save_model(request, obj, form, change)

admin.site.register(PortfolioEntry, PortfolioEntryAdmin)