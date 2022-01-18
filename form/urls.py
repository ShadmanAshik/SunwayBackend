from django.urls import path

from form.views import *

app_name="form"
urlpatterns = [ 
    path('snippets/', SnippetView.as_view(), name="snippets"),
]
