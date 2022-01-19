from django.contrib import admin
from users.models import Admin

from form.models import *

admin.site.register(AgentDataForm)
admin.site.register(Snippet)
admin.site.register(ContactUs)
admin.site.register(Scholarship)
admin.site.register(DevelopingSkills)
admin.site.register(LanguageProficiency)