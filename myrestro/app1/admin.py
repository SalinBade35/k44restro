from django.contrib import admin
from .models import Contact, Momo

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')

@admin.register(Momo)
class MomoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'images', 'price')


