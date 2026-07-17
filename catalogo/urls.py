from rest_framework.routers import DefaultRouter
from .views import ArtistaViewSet, AlbumViewSet

router = DefaultRouter()
router.register(r'artistas', ArtistaViewSet)
router.register(r'albumes', AlbumViewSet)

urlpatterns = router.urls
