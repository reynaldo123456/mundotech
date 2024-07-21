from django.contrib import admin

from .models import *

class AdminComments(admin.ModelAdmin):
    list_display = ['text', 'name', 'email','created_date', 'time_begin', 'time_final','topic']

class AdminBlog(admin.ModelAdmin):
    list_display = ["title", "category", "banner", "description", "CCI", "price",]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, AdminBlog)
admin.site.register(Comment, AdminComments)
admin.site.register(Reply)
