from django.contrib import admin
from .models import Answer, Testappear, question, StudentReport, Quiz123, Testcategory, registerform, Record, Option, AdminForm, newQuestion
# Register your models here.
admin.site.register([Answer, question, Testappear, Quiz123, Testcategory,
                    registerform, Record, Option, AdminForm, StudentReport])


admin.site.register(newQuestion)
