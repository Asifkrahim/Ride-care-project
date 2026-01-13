from django.urls import path,include

urlpatterns=[
    path('',include('maintenance.urls')),
    path('accounts/', include('accounts.urls')),
]