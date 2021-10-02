from django.contrib import admin

from myTypeidea.custom_site import custom_site
from myTypeidea.base_admin import BaseOwnerAdmin
from .models import Comment


# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'create_time')
