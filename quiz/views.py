import email
from unicodedata import category
from click import option
from django.shortcuts import render,redirect
from .models import Answer, registerform,question,Record,AdminForm,Testcategory,Option
from django.http import HttpResponse

# Create your views here.
def index(request):
    if 'email' in request.session:
        print(request.session['email'])        
        n=AdminForm.objects.get(email=request.session['email'])        
    # a=Record.objects.all()
        a=registerform.objects.all()
        # count=Record.objects.all().count()
        count=registerform.objects.all().count()
        q=question.objects.all()
        return render(request,'index.html',{'data':a,'c':count,'q':len(q),'n':n})
    return render('sign1')
# ------------------------------------------------------------------------------------------------
    # return render(request,'index.html')

def profile(request):
    if 'email' in request.session:
        n=AdminForm.objects.get(email=request.session['email'])
        if request.POST:
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['passowrd']

            n.name=name
            n.email=email
            n.password=password
            n.save()
            return redirect('index1')    
        return render(request,'adminprofile.html',{'n':n})    
    return redirect('sign1')
def add_option(request):
    q=question.objects.all()
    if request.POST:
        id=request.POST['quest']
        title=request.POST['op']
        try:
            ans=request.POST.get('isans')
            obj=question.objects.get(question=id)

            s=Option()
            s.question=obj
            s.option_title=title
            if ans:    
                s.is_answer=True
            s.save()
            return redirect('index1')
        except:
            pass
    return render(request,'option.html',{'question':q})

def view_option(request):
    obj=Option.objects.all()
    return render(request,'viewoption.html',{'obj':obj})


def create_test(request):
    return render(request,'createtest.html')

def correct_answer(request):
    ans=Answer.objects.all()
    return render(request,'viewanswer.html',{'ans':ans})

def question_add(request):
    al=Testcategory.objects.all()
    if request.POST:
        
        category=request.POST['category']
        getquestion=request.POST['question']
        # time=request.POST['time']
        # option1=request.POST['option1']
        # option2=request.POST['option2']
        # option3=request.POST['option3']
        # answer=request.POST['check']

        # if answer=='1':
        #     answer=option1
        # elif answer=='2':
        #     answer=option2    
        # else:
        #     answer=option3
        
        obj=Testcategory.objects.get(name=category)
            
        q=question()
        q.categoryName=obj
        q.question=getquestion
        # q.time=time
        # q.option1=option1
        # q.option2=option2
        # q.option3=option3
        # q.correct=answer
        q.save()

        return redirect('index1')

    return render(request,'questionadd.html',{'al':al})

def testcategory_add(request):
    if request.POST:
        name=request.POST['name']
        q=Testcategory()
        q.name=name
        q.save()
        return redirect('index1')
    return render(request,'category.html')   
 
def delete_testcategory(request,id):
    obj=Testcategory.objects.get(id=id)  
    obj.delete()  
    return redirect('viewcategory')

def delete_student(request,id):
    obj=registerform.objects.get(id=id)  
    obj.delete()  
    return redirect('index1')

def logout(request):
    if 'email' in request.session:
        # n=AdminForm.objects.get(email=request.session['email'])  
        del request.session['email']  
    return redirect('sign1')

def delete_option(request,id):
    obj=Option.objects.get(id=id)  
    obj.delete()  
    return redirect('viewoption')

def edit_option(request,id):
    obj=Option.objects.get(id=id)
    al=question.objects.all()    
    if request.POST:
        q=request.POST['question']
        q=question.objects.get(question=q)
        o=request.POST['op']
        a=request.POST.get('isans')

        obj.question=q
        obj.option_title=o
        if a:
            obj.is_answer=True
        else:
            obj.is_answer=False    
        obj.save()
        return redirect('viewoption')
    return render(request,'edit_option.html',{'obj':obj,'al':al})        

def edit_student(request,id):
    obj=registerform.objects.get(id=id)    
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        en=request.POST['en.no']
        password=request.POST['password']
        attend=request.POST['attendance']
        cgpa=request.POST['cgpa']
        gpa=request.POST['gpa']
        rev=request.POST['review']
        sc=request.POST['score']

        obj.name=name
        obj.email=email
        obj.Enrollment_No=en
        obj.password=password
        obj.Attendance=attend
        obj.cgpa=cgpa
        obj.gpa=gpa
        obj.review=rev
        obj.score=sc
        obj.save()
        
        return redirect('index1')
    return render(request,'editstudent.html',{'obj':obj})        


def edit_testcategory(request,id):
    obj=Testcategory.objects.get(id=id)    
    if request.POST:
        name=request.POST['name']
        obj.name=name
        obj.save()
        return redirect('viewcategory')
    return render(request,'edit_category.html',{'obj':obj})        

def view_category(request):
    obj=Testcategory.objects.all()    
    return render(request,'view_category.html',{'obj':obj})        

def delete_question(request,id):
    obj=question.objects.get(id=id)
    obj.delete()
    return redirect('viewquestion')

def edit_questions(request,id):
    obj=question.objects.get(id=id)
    name1=str(obj.categoryName)
    al=Testcategory.objects.all()
    if request.POST:
        category=request.POST['category']
        getquestion=request.POST['question']
        # option1=request.POST['option1']
        # option2=request.POST['option2']
        # option3=request.POST['option3']
        # answer=request.POST['check']

        # if answer=='1':
        #     answer=option1
        # elif answer=='2':
        #     answer=option2    
        # else:
        #     answer=option3
        
        obj1=Testcategory.objects.get(name=category)

        obj.categoryName=obj1
        obj.question=getquestion
        # obj.option1=option1
        # obj.option2=option2
        # obj.option3=option3
        # obj.time='00:20'
        # obj.correct=answer
        obj.save()
        return redirect('viewquestion')

    return render(request,'editquestion.html',{'obj':obj,'al':al,'name1':name1})    


def student_report(request):
    return render(request,'studentreport.html')

def show_question(request):
    al=question.objects.all()
    return render(request,'showquestion.html',{'al':al})

def view_test(request):
    return render(request,'viewtest.html')

def Add_student(request):
    if request.method=="POST":
        model=registerform()
        model.name=request.POST['name']
        model.email=request.POST['email']
        model.Enrollment_No=request.POST['enrollment']
        model.password=request.POST['password']
        model.save()
        s='student saved successfully'
        return render(request,'Add_student.html',{'s':s})
    return render(request,'Add_student.html')

def LoginUserView(request):
    if request.POST:
        try:
            model = AdminForm.objects.get(
                email=request.POST['email'])
            if model.password == request.POST['password']:
                request.session['email'] = model.email
                return redirect('index1')
            else:
                return HttpResponse("<a href = ''>Incorrect details</a>")
        except:
            return HttpResponse("<a href = ''>Incorrect details</a>")
    return render(request,'sign.html')

# ##################### Ankit's Work START ###############################
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
            return render(request,'student_signup.html', {'msg': msg})
        except:
            if password == con_password:
                db = registerform(
                    name = name,
                    email = email,
                    Enrollment_No = new_enroll_no,
                    password = password
                )
                db.save()
                # msg = "Signup successfully done"
                msg = f"Your Enrollment no is this, {new_enroll_no}"
                print(msg)
                return render(request,'student_signup.html', {'msg': msg})
            else:
                msg = "Both passwords are not matching"
                print(msg)
                return render(request,'student_signup.html', {'msg': msg})

    return render(request,'student_signup.html')

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
                return render(request,'student_login.html', {'msg': msg})
        except:
            msg = "Student does not exist"
            print(msg)
            return render(request,'stu_login.html', {'msg': msg})
    return render(request,'stu_login.html')

def student_logout_view(request):
    del request.session['enroll_no']
    print('Student logged out')
    return redirect('student_login_view')

def stu_index(request):
    if request.session['enroll_no']:
        # show_data = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        return render(request, 'stu_index.html')
    return redirect('student_login_view')
    
def stu_result(request):
    if request.session['enroll_no']:
        # show_data = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        return render(request, 'stu_result.html')
    return redirect('student_login_view')
    
def stu_question(request):
    if request.session['enroll_no']:
        # show_data = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        return render(request, 'stu_question.html')
    return redirect('student_login_view')
    
def stu_profile(request):
    if request.session['enroll_no']:
        show_data = ''
        msg = ''
        show_data = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        if request.POST:
            password = request.POST['password']
            show_data.password = password
            show_data.save()
            msg = 'Your Password has been updated successfully'
            print(msg)
            return render(request, 'stu_profile.html', {'msg': msg})
        return render(request, 'stu_profile.html', {'show_data': show_data})
    return redirect('student_login_view')
    
def student_dashboard(request):
    if 'enroll_no' in request.session:     
        n = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        return render(request,'stu_index.html', {'n': n})
    return render('student_login_view')

# ##################### Ankit's Work END ###############################