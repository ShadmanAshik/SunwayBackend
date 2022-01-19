from django.urls import include, path
from rest_framework import routers

from .views import ContactFormDataViewSet

router=routers.DefaultRouter()
router.register(r'Contactformdata',ContactFormDataViewSet)
urlpatterns=[
    path('',include(router.urls))
]
