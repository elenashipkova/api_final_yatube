from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'post', 'created')
    search_fields = ('text',)
    list_filter = ('created',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user__username', 'following__username')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)
