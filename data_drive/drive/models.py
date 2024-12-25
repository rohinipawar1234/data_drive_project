from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class CustomUser(AbstractUser):
    pass

    
# Folder model
class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# File model
class File(models.Model):
    name = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, related_name='files', on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_data = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name
