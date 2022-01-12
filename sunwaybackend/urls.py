from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('djoser.urls')),
    path('accounts/', include('djoser.urls.authtoken')),
    path('cfd/',include('contactForm.urls')),
    
]
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]