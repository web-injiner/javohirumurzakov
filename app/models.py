from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=30,verbose_name="Post nomi",help_text="Post uchun sarlavha")
    image = models.ImageField(upload_to='post-images',verbose_name="Post uchun rasm",help_text="Post uchun rasmini kiriting help text")
    def __str__(self):
        return self.name 
