from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views.auth_views import (
    UserRegisterView,
    UserProfileView,
    ChangePasswordView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)
from api.views.note_views import NoteViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

# Auth URLs
auth_urls = [
    # JWT Token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # User management
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('password-reset-confirm/<str:uid>/<str:token>/', 
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    
    # Auth endpoints
    path('auth/', include(auth_urls)),
] 