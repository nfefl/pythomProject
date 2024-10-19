from django.contrib import admin
from .models import Articles, INews, Make

admin.site.register(Articles)
admin.site.register(Make)
admin.site.register(INews)
# Register your models here.
