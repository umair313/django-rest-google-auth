from django.urls import path
from users.api.views import GoogleLoginView

urlpatterns = [
    path("google/login/", GoogleLoginView.as_view(), name='login_with_google')
]