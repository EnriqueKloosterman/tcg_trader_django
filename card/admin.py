from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Card_Type)
admin.site.register(models.Faction)
admin.site.register(models.Card)