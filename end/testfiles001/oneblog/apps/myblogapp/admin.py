from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Note)
admin.site.register(Ads)
admin.site.register(Recommend)
