from django.conf.urls import url, include
from rest_framework import routers
from .views import PetViewSet, BreedViewSet, BirthViewSet

router = routers.SimpleRouter()
router.register(r'pet', PetViewSet)
router.register(r'breed', BreedViewSet)
router.register(r'birth', BirthViewSet)

urlpatterns = [
    url(r'v1/', include(router.urls))
]
