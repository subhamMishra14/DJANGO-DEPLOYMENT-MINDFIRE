from django.contrib import admin

# Register your models here.

from MODEL_CREATION import models

admin.site.register(models.AccessRecord)
admin.site.register(models.Topic)
admin.site.register(models.WebPage)
