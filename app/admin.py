from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name'] #Admin pageda korinadigan maydonlar
    list_per_page: 10 # Admin Sahifada ko'rinadigan postlar soni
    