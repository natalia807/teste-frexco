from django.contrib import admin
from .models import User
 
@admin.register(User)
class RequestUserAdmin(admin.ModelAdmin):
  list_display = ['login', 'dateNasc']