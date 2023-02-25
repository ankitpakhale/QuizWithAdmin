import contextlib
import email
from unicodedata import category
# from click import option
from django.shortcuts import render, redirect
from .models import Answer, StudentReport, registerform, question, Testappear, Record, AdminForm, Testcategory, Option, contactForm, newQuestion, StudentMarks
from django.http import HttpResponse
# import plotly.graph_objects as go
from io import BytesIO
import pandas as pd
# import plotly.express as px


# Create your views here.
def index(request):
    if 'email' in request.session:
        print(request.session['email'])
        n = AdminForm.objects.get(email=request.session['email'])
        a = registerform.objects.all()
        count = registerform.objects.all().count()
        q = question.objects.all()
        r = StudentReport.objects.all()
        return render(request, 'index.html', {'data': a, 'c': count, 'q': len(q), 'n': n, 'r': r})
    return redirect('sign1')


def profile(request):
    if 'email' in request.session:
        n = AdminForm.objects.get(email=request.session['email'])
        if request.POST:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['passowrd']
            n.name = name
            n.email = email
            n.password = password
            n.save()
            return redirect('index1')
        return render(request, 'adminprofile.html', {'n': n})
    return redirect('sign1')


def add_option(request):
    if 'email' in request.session:

        q = question.objects.all()
        msg = ''
        if request.POST:
            id = request.POST['quest']
            title = request.POST['op']
            try:
                ans = request.POST.get('isans')
                print(id)
                obj = question.objects.get(id=id)
                print(obj)
                s = Option()
                s.question = obj
                s.option_title = title
                if ans:
                    s.is_answer = True
                s.save()
                msg = 'option added successfully'
            except:
                pass
        return render(request, 'option.html', {'question': q, 'msg': msg})
    return redirect('sign1')


def view_option(request):
    if 'email' in request.session:
        obj = Option.objects.all()
        return render(request, 'viewoption.html', {'obj': obj})
    return redirect('sign1')


def create_test(request):
    if 'email' in request.session:
        return render(request, 'createtest.html')
    return redirect('sign1')


def correct_answer(request):
    if 'email' in request.session:
        ans = Answer.objects.all()
        return render(request, 'viewanswer.html', {'ans': ans})
    return redirect('sign1')


def view_query(request):
    if 'email' in request.session:
        c_form = contactForm.objects.all()
        return render(request, 'view_query.html', {'c_form': c_form})
    return redirect('sign1')


def question_add(request):
    if 'email' in request.session:
        al = Testcategory.objects.all()
        msg = ''
        if request.POST:
            category = request.POST['category']
            getquestion = request.POST['question']
            obj = Testcategory.objects.get(name=category)
            q = question()
            q.categoryName = obj
            q.question = getquestion
            q.save()
            msg = 'question added successfully'
            # return redirect('quistion1')
        return render(request, 'questionadd.html', {'al': al, 'msg': msg})
    return redirect('sign1')


def addFile(request):
    if 'email' in request.session:
        msg = ''
        if request.POST:
            file = request.FILES.get('uploadFile')
            df = pd.read_excel(file)
            for i in df.values:
                try:
                    newQuestion.objects.create(
                        question=i[0], option1=i[1], option2=i[2], option3=i[3], option4=i[4], ans=i[5], categoryName=i[6])
                    msg = "Questions added successfully"
                except:
                    pass
        return render(request, 'addFile.html', {'msg': msg})
    return redirect('sign1')


def viewQuiz(request):
    if 'email' in request.session:
        quiz = newQuestion.objects.all()
        return render(request, 'view_quiz.html', {'quiz': quiz})
    return redirect('sign1')


def testcategory_add(request):
    if 'email' in request.session:
        if request.POST:
            name = request.POST['name']
            q = Testcategory()
            q.name = name
            q.save()
            newly = Testcategory.objects.last()
            allstudent = registerform.objects.all()
            for i in allstudent:
                Testappear.objects.create(
                    t_category=newly, t_user=i, isappear=False)
            return redirect('index1')
        return render(request, 'category.html')
    return redirect('sign1')


def delete_testcategory(request, id):
    if 'email' in request.session:
        obj = Testcategory.objects.get(id=id)
        obj.delete()
        return redirect('viewcategory')
    return redirect('sign1')


def delete_question(request, id):
    if 'email' in request.session:
        obj = newQuestion.objects.get(id=id)
        print(obj)
        obj.delete()
        return redirect('viewcategory')
    return redirect('sign1')


def delete_student(request, id):
    if 'email' in request.session:
        obj = registerform.objects.get(id=id)
        obj.delete()
        return redirect('index1')
    return redirect('sign1')


def logout(request):
    del request.session['email']
    print('inside logout')
    return redirect('sign1')


def delete_option(request, id):
    if 'email' in request.session:
        obj = Option.objects.get(id=id)
        obj.delete()
        return redirect('viewoption')
    return redirect('sign1')


def edit_option(request, id):
    if 'email' in request.session:
        obj = Option.objects.get(id=id)
        al = question.objects.all()
        if request.POST:
            q = request.POST['question']
            print(q, 'ggggggggggggg')
            q = question.objects.get(id=q)
            o = request.POST['op']
            a = request.POST.get('isans')
            obj.question = q
            obj.option_title = o
            if a:
                obj.is_answer = True
            else:
                obj.is_answer = False
            obj.save()
            return redirect('viewoption')
        return render(request, 'edit_option.html', {'obj': obj, 'al': al})
    return redirect('sign1')


def edit_student(request, id):
    if 'email' in request.session:
        obj = registerform.objects.get(id=id)
        if request.POST:
            name = request.POST['name']
            email = request.POST['email']
            en = request.POST['en.no']
            password = request.POST['password']
            attend = request.POST['attendance']
            cgpa = request.POST['cgpa']
            rev = request.POST['review']
            obj.name = name
            obj.email = email
            obj.Enrollment_No = en
            obj.password = password
            obj.Attendance = attend
            obj.cgpa = cgpa
            obj.review = rev
            obj.save()
            return redirect('index1')
        return render(request, 'editstudent.html', {'obj': obj})
    return redirect('sign1')


def edit_testcategory(request, id):
    if 'email' in request.session:
        obj = Testcategory.objects.get(id=id)
        if request.POST:
            name = request.POST['name']
            obj.name = name
            obj.save()
            return redirect('viewcategory')
        return render(request, 'edit_category.html', {'obj': obj})
    return redirect('sign1')


def view_category(request):
    if 'email' in request.session:
        obj = Testcategory.objects.all()
        return render(request, 'view_category.html', {'obj': obj})
    return redirect('sign1')


def add_category(request):
    if 'email' in request.session:
        if request.POST:
            name = request.POST['name']
            q = Testcategory()
            q.name = name
            q.save()
            return redirect('viewcategory')
        return render(request, 'categoryadd.html')
    return redirect('sign1')


def category_report(request):
    if 'email' in request.session:
        cat = Testcategory.objects.all()
        data = ''
        if request.POST:
            category = request.POST['category']
            type = request.POST['type']
            obj = Testcategory.objects.get(name=category)
            data = StudentReport.objects.filter(
                cat_name=obj, percentage__range=(50.0, 100.0))
            if type == 'below':
                data = StudentReport.objects.filter(
                    cat_name=obj, percentage__range=(0.0, 50.0))
        return render(request, 'CategoryWiseReport.html', {'cat': cat, 'data': data})
    return redirect('sign1')


def delete_question(request, id):
    if 'email' in request.session:
        obj = newQuestion.objects.get(id=id)
        obj.delete()
        return redirect('viewquiz')
    return redirect('sign1')


def edit_questions(request, id):
    if 'email' in request.session:
        obj = question.objects.get(id=id)
        name1 = str(obj.categoryName)
        al = Testcategory.objects.all()
        if request.POST:
            category = request.POST['category']
            getquestion = request.POST['question']
            obj1 = Testcategory.objects.get(name=category)
            obj.categoryName = obj1
            obj.question = getquestion
            obj.save()
            return redirect('viewquestion')
        return render(request, 'editquestion.html', {'obj': obj, 'al': al, 'name1': name1})
    return redirect('sign1')


def student_report(request):
    if 'email' in request.session:
        return render(request, 'studentreport.html')
    return redirect('sign1')


def show_question(request):
    if 'email' in request.session:
        al = question.objects.all()
        return render(request, 'showquestion.html', {'al': al})
    return redirect('sign1')


def view_test(request):
    if 'email' in request.session:
        return render(request, 'viewtest.html')
    return redirect('sign1')


def Add_student(request):
    if 'email' in request.session:
        if request.method == "POST":
            model = registerform()
            model.name = request.POST['name']
            model.email = request.POST['email']
            model.Enrollment_No = request.POST['enrollment']
            model.password = request.POST['password']
            model.Attendance = request.POST['attendence']
            model.cgpa = request.POST['cgpa']
            model.review = request.POST['review']
            model.save()
            newly = registerform.objects.last()
            allcat = Testcategory.objects.all()
            for i in allcat:
                Testappear.objects.create(
                    t_category=i, t_user=newly, isappear=False)
            s = 'student saved successfully'
            return render(request, 'Add_student.html', {'s': s})
        return render(request, 'Add_student.html')
    return redirect('sign1')


def LoginUserView(request):
    if request.POST:
        try:
            model = AdminForm.objects.get(
                email=request.POST['email'])
            if model.password == request.POST['password']:
                request.session['email'] = model.email
                return redirect('index1')
            else:
                msg = "Enter valid password"
                print(msg)
                return render(request, 'sign.html', {'msg': msg})
        except:
            msg = "Admin Does not exists"
            print(msg)
            return render(request, 'sign.html', {'msg': msg})
    return render(request, 'sign.html')


def student_signup_view(request):
    msg = ''
    prev_enroll_no = registerform.objects.last()
    new_enroll_no = str(int(prev_enroll_no.Enrollment_No)+1)
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']
        try:
            get_email = registerform.objects.get(email=email)
            msg = "This user already exist"
            print(msg)
            return render(request, 'student_signup.html', {'msg': msg})
        except:
            if password == con_password:
                db = registerform(
                    name=name,
                    email=email,
                    Enrollment_No=new_enroll_no,
                    password=password
                )
                db.save()
                msg = f"Your Enrollment no is this, {new_enroll_no}"
                print(msg)
                return render(request, 'student_signup.html', {'msg': msg})
            else:
                msg = "Both passwords are not matching"
                print(msg)
                return render(request, 'student_signup.html', {'msg': msg})
    return render(request, 'student_signup.html')


def student_login_view(request):
    msg = ''
    if request.POST:
        enroll_no = request.POST['enroll_no']
        password = request.POST['password']
        try:
            get_enroll = registerform.objects.get(Enrollment_No=enroll_no)
            if get_enroll.password == password:
                request.session['enroll_no'] = enroll_no
                msg = "Student Successfully logged in"
                print(msg)
                return redirect('stu_index')
            else:
                msg = "Enter valid password"
                print(msg)
                return render(request, 'stu_login.html', {'msg': msg})
        except:
            msg = "Student does not exist"
            print(msg)
            return render(request, 'stu_login.html', {'msg': msg})
    return render(request, 'stu_login.html')


def student_logout_view(request):
    if 'enroll_no' in request.session:
        del request.session['enroll_no']
        print('Student logged out')
    return redirect('student_login_view')


def stu_result(request):
    if 'enroll_no' in request.session:
        show_data = registerform.objects.get(
            Enrollment_No=request.session['enroll_no'])
        try:
            c1 = Testcategory.objects.all()
            for i in c1:
                Testappear.objects.get(
                    t_user=show_data, t_category=i, isappear=True)
        except:
            msg = 'Please complete all the tests first'
            return render(request, 'stu_result.html', {'msg': msg})
        stu_data = StudentReport.objects.filter(stu_name=show_data)
        labels = []
        all_per = []
        for i in stu_data:
            all_per.append((float(i.percentage)) * 1.5)
            labels.append(i.cat_name.name)
        labels.append('Attendance')
        labels.append('CGPA')
        labels.append('Rating')
        final_cgpa = (float(int(show_data.cgpa)) * 100 / 7) * 0.50
        final_att = (float(show_data.Attendance) * 100 / 12) * 0.25
        final_rating = (float(show_data.review) * 100 / 10) * 0.75
        all_per.append(final_att)
        all_per.append(final_cgpa)
        all_per.append(final_rating)
        final_percentage = round((sum(all_per) / len(all_per)), 2)
        show_data.score = final_percentage
        show_data.save()
        values = []
        # for i in all_per:
        #     values.append(i)
        # fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        # fig.show()
        res = {}
        for key in labels:
            for value in values:
                res[key] = round(value, 2)
                values.remove(value)
                break

        return render(request, 'stu_result.html', {'final_percentage': final_percentage, 'res': res})
    return redirect('student_login_view')


# def stu_question(request, id):
#     if 'enroll_no' in request.session:
#         t = Testcategory.objects.get(id=id)
#         ow = registerform.objects.get(
#             Enrollment_No=request.session['enroll_no'])
#         try:
#             check = Testappear.objects.get(
#                 t_user=ow, t_category=t, isappear=True)
#             return redirect('stu_allcat')
#         except:
#             final_dict = {}
#             obj = question.objects.filter(categoryName_id=id)
#             for i in obj:
#                 o = Option.objects.filter(question=i)
#                 final_dict[i] = o
#             if request.POST:
#                 for i in range(1, len(obj)+1):
#                     q = request.POST['question'+str(i)]
#                     ans = request.POST[str(i)]
#                     main_list = []
#                     c1 = question.objects.get(question=q)
#                     c2 = Option.objects.filter(question=c1, is_answer=True)
#                     for j in c2:
#                         main_list.append(j.option_title)
#                     print(main_list)
#                     if ans in main_list:
#                         Answer.objects.create(
#                             owner=ow, quiz1=t, question=c1, score=True)
#                 change = Testappear.objects.get(t_user=ow, t_category=t)
#                 print('inside except')
#                 change.isappear = True
#                 change.save()
#                 return redirect('stucalu', id)
#         total_size = len(final_dict)
#         return render(request, 'stu_question.html', {'final': final_dict, 'total_size': total_size})
#     return redirect('student_login_view')

def stu_question(request, test_category):
    if 'enroll_no' in request.session:
        # t = Testcategory.objects.get(id=id)
        ow = registerform.objects.get(
            Enrollment_No=request.session['enroll_no'])
        obj = ''
        total_size = ''

        obj = newQuestion.objects.filter(categoryName=test_category)
        if request.POST:
            count = 0
            for i in range(1, len(obj)+1):
                userQue = request.POST[f'question{i}']
                userAns = request.POST[f'{i}']

                userObj = newQuestion.objects.get(question=userQue)
                if userObj.ans == userAns:
                    count += 1

            percentage = (count / len(obj))*100
            StudentMarks.objects.create(
                stu_name=ow, cat_name=test_category, percentage=percentage,attempt=True)
            return redirect('stu_allcat')

        total_size = len(obj)
        return render(request, 'stu_question.html', {'final': obj, 'total_size': total_size})
    return redirect('student_login_view')


def stu_profile(request):
    if 'enroll_no' in request.session:
        show_data = ''
        msg = ''
        show_data = registerform.objects.get(
            Enrollment_No=request.session['enroll_no'])
        if request.POST:
            password = request.POST['password']
            show_data.password = password
            show_data.save()
            msg = 'Your Password has been updated successfully'
            print(msg)
            return render(request, 'stu_profile.html', {'msg': msg, 'show_data': show_data})
        return render(request, 'stu_profile.html', {'show_data': show_data})
    return redirect('student_login_view')


def student_dashboard(request):
    if 'enroll_no' in request.session:
        n = registerform.objects.get(
            Enrollment_No=request.session['enroll_no'])
        obj = Testappear.objects.filter(t_user=n)
        return render(request, 'stu_index.html', {'obj': obj})
    return redirect('student_login_view')


def about(request):
    return render(request, 'stu_about.html')


def contact(request):
    if request.POST:
        con = contactForm()
        con.name = request.POST['name']
        con.email = request.POST['email']
        con.phone = request.POST['phone']
        con.message = request.POST['message']
        con.save()
        msg = "Your response has been saved"
        return render(request, 'stu_contact.html', {'msg': msg})
    return render(request, 'stu_contact.html')


# def stu_allcat(request):
#     allcat = Testcategory.objects.all()
#     return render(request, 'stu_allcat.html', {'allcat': allcat})

def stu_allcat(request):
    if 'enroll_no' in request.session:
        allcat = newQuestion.objects.values('categoryName').distinct()
        studentData = registerform.objects.get(
            Enrollment_No=request.session['enroll_no'])
        
        appeared=StudentMarks.objects.filter(stu_name = studentData,attempt=True)
        apperaed_list=[i.cat_name for i in appeared]
        return render(request, 'stu_allcat.html', {'allcat': allcat,'appeared':apperaed_list})
    return redirect('student_login_view')

def base(request):
    return render(request, 'stu_base.html')


def stu_category_calculation(request, id):
    if 'enroll_no' in request.session:
        u = registerform.objects.get(
            Enrollment_No=request.session['enroll_no'])
        c = Testcategory.objects.get(id=id)
        s = Answer.objects.filter(quiz1=c)
        q = question.objects.filter(categoryName=c)
        ans = len(s)
        total_quest = len(q)
        final = (ans*100)/total_quest
        StudentReport.objects.create(stu_name=u, cat_name=c, percentage=final)
        return redirect('stu_catWiseResult')
    return redirect('student_login_view')


def stu_catWiseResult(request):
    if 'enroll_no' in request.session:
        show_data = registerform.objects.get(
            Enrollment_No=request.session['enroll_no'])
        all_data = StudentReport.objects.filter(stu_name=show_data)
        print(all_data)
        return render(request, 'stu_catWiseResult.html', {'all_data': all_data})
    return redirect('student_login_view')
