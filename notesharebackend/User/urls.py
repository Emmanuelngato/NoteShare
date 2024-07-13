from django.urls import path
from .views import UserViewSet, CustomAuthToken, UserRegisterView

urlpatterns = [
    path('get_user/<int:id>', UserViewSet.as_view({'get': 'get'})),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('register/', UserRegisterView.as_view(), name='register'),
]
