from operator import index
from django.contrib import admin
from django.urls import path
from.views import index,correct_answer,show_question,edit_testcategory,view_category,edit_questions,create_test,question_add,LoginUserView,student_report,view_test,Add_student,testcategory_add


urlpatterns = [
    path('index/',index,name='index1'),
    path('createtest/',create_test,name='create1'),
    path('questionadd/',question_add,name='quistion1'),
    path('',LoginUserView,name='sign1'),
    path('studentreport/',student_report,name='studentreport1'),
    path('viewtest/',view_test,name='viewtest'),
    path('editquestions/<int:id>',edit_questions,name='editquestions'),
    path('editcategory/<int:id>',edit_testcategory,name='editcategory'),
    path('viewquestion/',show_question,name='viewquestion'),
    path('viewcategory/',view_category,name='viewcategory'),
    path('addcategory/',testcategory_add,name='addcategory'),
    path('correct_answer/',correct_answer,name='correct_answer'),
    path('Add_student/',Add_student,name='addstudent')
]