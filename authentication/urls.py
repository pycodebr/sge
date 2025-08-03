from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

# Web URLs for user registration and profile management
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/change-password/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    
    # API URLs for JWT authentication (with api/v1/ prefix handled in main urls.py)
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
