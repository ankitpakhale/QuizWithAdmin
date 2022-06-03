from operator import index
from django.contrib import admin
from django.urls import path
from.views import index,view_option,edit_option,correct_answer,delete_testcategory,delete_question,add_option,show_question,edit_testcategory,view_category,edit_questions,create_test,question_add,LoginUserView,student_report,view_test,Add_student,testcategory_add, student_signup_view, student_login_view, stu_index, stu_result, stu_question, student_logout_view, stu_profile, edit_student, delete_option

urlpatterns = [
    path('index/',index,name='index1'),
    path('createtest/',create_test,name='create1'),
    path('questionadd/',question_add,name='quistion1'),
    path('',LoginUserView,name='sign1'),
    path('studentreport/',student_report,name='studentreport1'),
    path('viewtest/',view_test,name='viewtest'),
    path('editquestions/<int:id>',edit_questions,name='editquestions'),
    path('editoption/<int:id>',edit_option,name='editoption'),
    path('editcategory/<int:id>',edit_testcategory,name='editcategory'),
    path('edit_student/<int:id>',edit_student,name='edit_student'),
    path('delcategory/<int:id>',delete_testcategory,name='delcategory'),
    path('delete_question/<int:id>',delete_question,name='delquestion'),
    path('delete_option/<int:id>',delete_option,name='deloption'),
    path('viewquestion/',show_question,name='viewquestion'),
    path('viewcategory/',view_category,name='viewcategory'),
    path('viewoption/',view_option,name='viewoption'),
    path('addcategory/',testcategory_add,name='addcategory'),
    path('addoption/',add_option,name='addoption'),
    path('correct_answer/',correct_answer,name='correct_answer'),
    path('Add_student/',Add_student,name='addstudent'),
    
    # ##################### Ankit's Work START ###############################
    path('student_signup/',student_signup_view,name='student_signup_view'),    
    path('student_login/',student_login_view,name='student_login_view'),
    path('student_logout/',student_logout_view,name='student_logout_view'),
    
    path('stu_index/',stu_index,name='stu_index'),
    path('stu_result/',stu_result,name='stu_result'),
    path('stu_question/',stu_question,name='stu_question'),
    path('stu_profile/',stu_profile,name='stu_profile'),
    # ##################### Ankit's Work END ###############################
]