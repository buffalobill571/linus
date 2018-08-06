from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import AllowAny

from apps.blog.models import Post, FAQ, Tag
from apps.blog.serializers import PostSerializer, FAQSerializer, TagSerializer


class PostViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'body', 'tags__name')


class FAQViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('question', 'answer')


class TagViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    search_fields = ('name',)
