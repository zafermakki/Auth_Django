from django.urls import path
from .views import RegisterView, LoginView,LogoutView,ClientRegisterView, ClientLoginView, ClientLogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # client
    path('client/register/', ClientRegisterView.as_view(), name='register'),
    path('client/login/', ClientLoginView.as_view(), name='login'),
    path('client/logout/', ClientLogoutView.as_view(), name='logout'),
]
