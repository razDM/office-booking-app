from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter
from api.register import RegisterViewSet
from api.selection import OfficeViewSet


router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'offices', OfficeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('browser-auth/', include('rest_framework.urls')),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
