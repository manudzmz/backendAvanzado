from rest_framework.routers import SimpleRouter

from pictures.views import PictureViewSet

router = SimpleRouter()
router.register(r'pictures', PictureViewSet)

urlpatterns = router.urls