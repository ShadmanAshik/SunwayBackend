from django.contrib import admin

from users.models import *

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Student)
admin.site.register(Admin)
