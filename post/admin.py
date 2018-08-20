from django.contrib import admin
from post.models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('content','modify_date')
    list_filter = ('modify_date',)
    search_fields = ('modify_date','content')

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)