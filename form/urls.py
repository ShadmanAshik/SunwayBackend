from django.urls import path

from form.views import *

app_name="form"
urlpatterns = [ 
    # path('snippets/', SnippetView.as_view(), name="snippets"),
    path('contactus/', ContactUsView.as_view(), name="contactus"),
    path('scholarship/', ScholarshipView.as_view(), name="Scholarship"),
    path('skilldev/', DevelopingSkillsView.as_view(), name="skilldev"),
    path('language/', LanguageProficiencyView.as_view(), name="LanguageProficiency"),
    path('betutor/', BecomeTutorView.as_view(), name="betutor"),
    path('looktutor/', LookingTutorView.as_view(), name="looktutor"),
    path('individualagent/', AgentDataFormView.as_view(), name="individualagent"),
    path('businessagent/', BusinessAgentiew.as_view(), name="businessagent"),
]

# from django.urls import include, path
# from rest_framework import routers

# from form.views import *

# router=routers.DefaultRouter()
# router.register(r'Contactformdata',ContactFormDataViewSet)
# urlpatterns=[
#     path('',include(router.urls))
# ]
