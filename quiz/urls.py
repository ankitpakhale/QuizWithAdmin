from operator import index
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index1'),
    path('adlogout/', logout, name='admlogout'),
    path('createtest/', create_test, name='create1'),
    path('questionadd/', question_add, name='quistion1'),

    path('addfile/', addFile, name='addFile'),
    path('viewquiz/', viewQuiz, name='viewquiz'),

    path('admin_login/', LoginUserView, name='sign1'),
    path('studentreport/', student_report, name='studentreport1'),
    path('category_wisereport/', category_report, name='category_wisereport'),

    path('viewtest/', view_test, name='viewtest'),
    path('adminprofile/', profile, name='adprofile'),
    path('editquestions/<int:id>', edit_questions, name='editquestions'),
    path('editoption/<int:id>', edit_option, name='editoption'),
    path('editcategory/<int:id>', edit_testcategory, name='editcategory'),
    path('edit_student/<int:id>', edit_student, name='edit_student'),

    path('delcategory/<int:id>', delete_testcategory, name='delcategory'),

    path('delstudent/<int:id>', delete_student, name='delstudent'),

    path('delete_question/<int:id>', delete_question, name='delquestion'),

    path('delete_option/<int:id>', delete_option, name='deloption'),
    path('viewquestion/', show_question, name='viewquestion'),

    path('viewcategory/', view_category, name='viewcategory'),

    path('add_category/', add_category, name='add_category'),
    path('viewoption/', view_option, name='viewoption'),
    path('addcategory/', testcategory_add, name='addcategory'),
    path('addoption/', add_option, name='addoption'),
    path('correct_answer/', correct_answer, name='correct_answer'),
    path('viewquery/', view_query, name='view_query'),
    path('Add_student/', Add_student, name='addstudent'),
    path('login/', student_login_view, name='student_login_view'),
    path('stu_logout/', student_logout_view, name='student_logout_view'),
    # path('stu_index/', student_dashboard, name='stu_index'),
    path('stu_result/', stu_result, name='stu_result'),
    path('', stu_allcat, name='stu_allcat'),
    path('stucalculation/<int:id>', stu_category_calculation, name='stucalu'),
    # path('stu_question/<int:id>', stu_question, name='stu_question'),
    path('stu_question/<test_category>', stu_question, name='stu_question'),
    path('stu_profile/', stu_profile, name='stu_profile'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('catWiseResult/', stu_catWiseResult, name='stu_catWiseResult'),
    path('stuIndex/', studentDashboardNew, name='stuIndexNew'),
]
