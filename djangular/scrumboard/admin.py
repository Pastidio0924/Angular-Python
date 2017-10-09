from django.contrib import admin

# Register your models here.

from .models import List, Card

admin.site.register(List)
admin.site.register(Card)
