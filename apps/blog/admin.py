from django.contrib import admin

from apps.blog.models import Post, FAQ, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pk', 'truncated_question', 'truncated_answer')
    search_fields = ('answer', 'question')

    def truncated_question(self, obj):
        return obj.question[:50]

    def truncated_answer(self, obj):
        return obj.answer[:50]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'published_date', 'truncated_body')
    search_fields = ('title', 'body')
    autocomplete_fields = ('tags',)
    list_filter = ('tags',)

    def truncated_body(self, obj):
        return obj.body[:50]
