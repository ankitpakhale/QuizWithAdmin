from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Answer, question, Testappear, Quiz123, Testcategory,
                    registerform, Record, Option, AdminForm, StudentReport])


admin.site.register(newQuestion)
admin.site.register(StudentMarks)
