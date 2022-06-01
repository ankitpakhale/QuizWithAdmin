from django.contrib import admin
from .models import Answer,question,Quiz,Testcategory,registerform,Record,Option,AdminForm
# Register your models here.
admin.site.register([Answer,question,Quiz,Testcategory,registerform,Record,Option,AdminForm])