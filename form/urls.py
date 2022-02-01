from django.urls import path

from form.views import *

app_name="form"
urlpatterns = [ 
    # path('snippets/', SnippetView.as_view(), name="snippets"),
    path('contactusget/', ContactUsGetView.as_view(), name="contactusget"),
    path('contactuspost/', ContactUsPostView.as_view(), name="contactuspost"),
    path('commonformget/', CommonFormGetView.as_view(), name="commonformget"),
    path('commonformpost/', CommonFormPostView.as_view(), name="commonformpost"),
    path('scholarshipget/', ScholarshipGetView.as_view(), name="Scholarship"),
    path('scholarshippost/', ScholarshipPostView.as_view(), name="Scholarship"),
    path('skilldevget/', DevelopingSkillsGetView.as_view(), name="skilldev"),
    path('skilldevpost/', DevelopingSkillsPostView.as_view(), name="skilldev"),
    path('betutorget/', BecomeTutorGetView.as_view(), name="betutor"),
    path('betutorpost/', BecomeTutorPostView.as_view(), name="betutor"),
    path('looktutorget/', LookingTutorGetView.as_view(), name="looktutor"),
    path('looktutorpost/', LookingTutorPostView.as_view(), name="looktutor"),
    path('individualagentget/', IndivisualAgentGetView.as_view(), name="individualagent"),
    path('individualagentpost/', IndivisualAgentPostView.as_view(), name="individualagent"),
    path('businessagentget/', BusinessAgentGetView.as_view(), name="businessagent"),
    path('businessagentpost/', BusinessAgentPostView.as_view(), name="businessagent"),
    path('languageget/', LanguageProficiencyGetView.as_view(), name="language"),
    path('languagepost/', LanguageProficiencyPostView.as_view(), name="language"),
    path('admissionget/', AdmissionFormGetView
    .as_view(), name="admission"),
    path('admissionpost/', AdmissionFormPostView.as_view(), name="admission"),
]
