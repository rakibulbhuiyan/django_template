from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
]
