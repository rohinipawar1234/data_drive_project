from django.contrib import admin
from drive.models import CustomUser,Folder,File

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Folder)
admin.site.register(File)