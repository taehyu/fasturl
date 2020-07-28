from rest_framework.routers import SimpleRouter

from urls.views import LinkViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'urls', LinkViewSet)
urlpatterns = router.urls
