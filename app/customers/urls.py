from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet

router = DefaultRouter()

router.register(r"", CustomerViewSet, "customer")

urlpatterns = []
urlpatterns += router.urls
