from django.contrib import admin
from .models import UploadImage

# Register your models here.
@admin.register(UploadImage)
class UploadImageAdmin(admin.ModelAdmin):
    list_display = ('author', 'upload_time', 'img1')
