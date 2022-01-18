from django.urls import path

from form.views import *

app_name="form"
urlpatterns = [ 
    path('snippets/', SnippetView.as_view(), name="snippets"),
    path('contactus/', ContactUsView.as_view(), name="contactus"),
    path('scholarship/', ScholarshipView.as_view(), name="scholarship"),
    path('language/', ScholarshipView.as_view(), name="language"),
    path('skillDev/', ScholarshipView.as_view(), name="skillDev"),
]

# from django.urls import include, path
# from rest_framework import routers

# from form.views import *

# router=routers.DefaultRouter()
# router.register(r'Contactformdata',ContactFormDataViewSet)
# urlpatterns=[
#     path('',include(router.urls))
# ]
