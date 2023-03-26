from django.contrib import admin
from .models import Notebook

# Register your models here.
admin.site.register(Notebook)

admin.site.site_title = 'Notebook Price Predictor Administration'
admin.site.site_header = 'Админ-панель сайта "Notebook Price Predictor"'