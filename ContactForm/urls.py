from django.urls import path,include
from rest_framework import routers
from .views import ContactFormDataViewSet

router=routers.DefaultRouter()
router.register(r'contactformdata',ContactFormDataViewSet)
urlpatterns=[
    path('',include(router.urls))
]