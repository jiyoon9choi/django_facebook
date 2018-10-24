from django.contrib import admin

# Register your models here.
from facebook.models import article, Comment

admin.site.register(article)
admin.site.register(Comment)
