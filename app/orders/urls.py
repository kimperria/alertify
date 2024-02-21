from rest_framework.routers import DefaultRouter

from app.orders.views import OrderViewSet

router = DefaultRouter()

router.register(r"", OrderViewSet, "order")

urlpatterns = []
urlpatterns += router.urls
