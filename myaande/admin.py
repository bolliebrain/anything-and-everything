from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
