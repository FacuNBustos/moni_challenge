from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)

urlpatterns = [
    path( 'login/', TokenObtainPairView.as_view() ),
    path( 'token/refresh/', TokenRefreshView.as_view() ),
    path( 'token/verify/', TokenVerifyView.as_view() )
]