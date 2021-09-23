from django.contrib import admin
from blog.models import Post, Tag, Comments


class AdminTag(admin.ModelAdmin):
    list_display = ("name",)


class AdminPost(admin.ModelAdmin):
    list_display = ("title", "auther")


class AdminComments(admin.ModelAdmin):
    list_display = ("post", "auther")


admin.site.register(Tag, AdminTag)
admin.site.register(Post, AdminPost)
admin.site.register(Comments, AdminComments)