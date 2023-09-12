from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_date',)  # Change 'approved_comment' to 'is_approved'
    list_filter = ('created_date',)  # Change 'approved_comment' to 'is_approved'

    def is_approved(self, obj):
        return obj.approved_comment  # Use the 'approved_comment' method to check if the comment is approved

    is_approved.short_description = 'Approved'
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)