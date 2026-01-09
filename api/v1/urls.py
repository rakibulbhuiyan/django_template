from django.urls import path, include

urlpatterns = [
    path('account/', include('apps.account.urls')),
    path('auth/', include('apps.socialauth.urls')),
]