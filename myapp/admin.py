from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(UserInformationModal)
class UserInformationModal2(admin.ModelAdmin):
    list_display=["email","phone","country"]
    
    
@admin.register(ContentModal)
class USerContent(admin.ModelAdmin):
    list_display=["title","body","summary","category"]

admin.site.register(UserLogin)