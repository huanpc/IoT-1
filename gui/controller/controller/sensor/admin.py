from django.contrib import admin
from .models import SensorModel
from django import forms

#TODO: Docs here: https://docs.djangoproject.com/en/1.10/ref/contrib/admin
class SensorAdminChangeForm(forms.ModelForm):
    class Meta:
        model = SensorModel
        fields = '__all__'
        exclude = ['resource_id', 'id']

    #TODO: https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#adding-custom-validation-to-the-admin
    def clean(self):
        return

    def save(self, commit=True):
        return super().save(commit)


class SensorAdmin(admin.ModelAdmin):
    # Use 2 model Admin in one admin parent page
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#inlinemodeladmin-objects
    form = SensorAdminChangeForm
    ordering = ['id']
    # list_filter = ('title', 'location', 'start_time')
    # fieldsets = (
    #                 ('Required', {
    #                     'fields': ('url_event', 'title', 'description', 'location', 'start_time', 'end_time')
    #                 }),
    #                 ('Addition options', {
    #                     'classes': ('collapse',),
    #                     'fields': ('ticket_url', 'thumbnail', 'event_thumbnail', 'number_interest', 'host', 'service_fee',
    #                                'quantity', 'contact', 'country_code', 'lang', 'slug', ),
    #                 }),
    #             )
    # readonly_fields = ('event_thumbnail',)
    exclude = ('id', 'resource_id')
    list_display = ('id', 'resource_id', 'sensor_type', 'description', 'namespace', 'label', 'version', 'manufacturer', 'platform_listener')
    # Doc_heres: https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    # search_fields = ('title',)


admin.site.register(SensorModel, SensorAdmin)
