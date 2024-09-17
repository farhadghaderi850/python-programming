from django.contrib import admin

from myapp.models import Comment, Myapp


# Register your models here.

class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text', 'pub_date']
    extra = 0


@admin.register(Myapp)
class MyappAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_enable', 'updated', 'published_date']
    inlines = [CommentAdminInline, ]

# class CommentAdmin(admin.ModelAdmin):
# list_display = ['Myapp', 'text', 'pub_date', 'updated']


# admin.site.register(Myapp, MyappAdmin) میتونی بجای
# از@admin.register(Myapp) استفاده کنی
# admin.site.register(Comment, CommentAdmin)
