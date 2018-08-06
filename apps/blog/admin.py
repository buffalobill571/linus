from django.contrib import admin

from apps.blog.models import Post, FAQ, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    autocomplete_fields = ('tags',)
