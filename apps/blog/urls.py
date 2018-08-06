from rest_framework.routers import DefaultRouter

from apps.blog.views import PostViewSet, FAQViewSet, TagViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet, base_name='posts')
router.register(r'faqs', FAQViewSet, base_name='faqs')
router.register(r'tags', TagViewSet, base_name='tags')

urlpatterns = router.urls
