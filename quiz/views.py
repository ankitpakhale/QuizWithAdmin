import email
from unicodedata import category
from click import option
from django.shortcuts import render,redirect
from .models import Answer,StudentReport ,registerform,question,Testappear,Record,AdminForm,Testcategory,Option, contactForm
from django.http import HttpResponse
import plotly.graph_objects as go
from io import BytesIO
import plotly.express as px


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
    return redirect('sign1')
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
    msg=''
    if request.POST:
        id=request.POST['quest']
        title=request.POST['op']
        try:
            ans=request.POST.get('isans')
            print(id)
            obj=question.objects.get(id=id)
            print(obj)
            s=Option()
            s.question=obj
            s.option_title=title
            if ans:    
                s.is_answer=True
            s.save()
            msg='option added successfully'
            
        except:
            pass
    return render(request,'option.html',{'question':q,'msg':msg})

def view_option(request):
    obj=Option.objects.all()
    return render(request,'viewoption.html',{'obj':obj})


def create_test(request):
    return render(request,'createtest.html')

def correct_answer(request):
    ans=Answer.objects.all()
    return render(request,'viewanswer.html',{'ans':ans})

def view_query(request):
    c_form=contactForm.objects.all()
    return render(request,'view_query.html',{'c_form':c_form})

def question_add(request):
    al=Testcategory.objects.all()
    msg=''
    if request.POST:
        
        category=request.POST['category']
        getquestion=request.POST['question']
        
        obj=Testcategory.objects.get(name=category)
            
        q=question()
        q.categoryName=obj
        q.question=getquestion
        
        q.save()

        msg='question added successfully'

        

    return render(request,'questionadd.html',{'al':al,'msg':msg})

def testcategory_add(request):
    if request.POST:
        name=request.POST['name']
        q=Testcategory()
        q.name=name
        q.save()
        newly=Testcategory.objects.last()
        allstudent=registerform.objects.all()
        for i in allstudent:
            Testappear.objects.create(t_category=newly,t_user=i,isappear=False)
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
        print(q,'ggggggggggggg')
        q=question.objects.get(id=q)
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
        rev=request.POST['review']
        # sc=request.POST['score']

        obj.name=name
        obj.email=email
        obj.Enrollment_No=en
        obj.password=password
        obj.Attendance=attend
        obj.cgpa=cgpa
        obj.review=rev
        # obj.score=sc
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
        
        obj1=Testcategory.objects.get(name=category)

        obj.categoryName=obj1
        obj.question=getquestion
        
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
        model.Attendance=request.POST['attendence']
        model.cgpa=request.POST['cgpa']
        model.review=request.POST['review']
        # model.score=request.POST['score']
        model.save()
        newly=registerform.objects.last()
        allcat=Testcategory.objects.all()
        for i in allcat:
            Testappear.objects.create(t_category=i,t_user=newly,isappear=False)
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
                return render(request,'stu_login.html', {'msg': msg})
        except:
            msg = "Student does not exist"
            print(msg)
            return render(request,'stu_login.html', {'msg': msg})
    return render(request,'stu_login.html')

def student_logout_view(request):
    if 'enroll_no' in request.session:
        del request.session['enroll_no']  
        print('Student logged out')
    return redirect('student_login_view')


def stu_result(request):
    if 'enroll_no' in request.session:
        
        show_data = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        try:
            c1=Testcategory.objects.all()
            for i in c1:
                Testappear.objects.get(t_user=show_data,t_category=i,isappear=True)
        except:
            msg='you have to complet all Test'
            return render(request,'stu_result.html',{'msg':msg})
        stu_data = StudentReport.objects.filter(stu_name = show_data)
        
        labels = []
        all_per = []
        for i in stu_data:
            all_per.append((float(i.percentage)) * 1.5)            
            labels.append(i.cat_name.name)

        final_cgpa = (float(int(show_data.cgpa)) * 100 / 7) * 0.50
        final_att = (float(show_data.Attendance) * 100 / 12) * 0.25
        final_rating = (float(show_data.review) * 100 / 10) * 0.25
        # final_gpa = float(show_data.gpa) * 100 / 7
        
        all_per.append(final_att)
        all_per.append(final_cgpa)
        all_per.append(final_rating)
        # all_per.append(final_gpa)
        
        labels.append('Attendance')
        labels.append('CGPA')
        labels.append('Review Status')
        # labels.append('GPA')

        final_percentage = round((sum(all_per) / len(all_per)), 2)
        show_data.score=final_percentage
        show_data.save()
        
        values = []
        for i in all_per:
            values.append(i)

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.show()

        return render(request, 'stu_result.html', {'final_percentage': final_percentage})   
    return redirect('student_login_view')

def stu_question(request, id):
    if 'enroll_no' in request.session:     
        t=Testcategory.objects.get(id=id)
        ow=registerform.objects.get(Enrollment_No=request.session['enroll_no'])
        try:
            check=Testappear.objects.get(t_user=ow,t_category=t,isappear=True)
            return redirect('stu_allcat')
        except:
            final_dict={}
            obj=question.objects.filter(categoryName_id=id)
            for i in obj:
                o=Option.objects.filter(question=i)
                final_dict[i]=o
            if request.POST:
                for i in range(1,len(obj)+1):
                    q=request.POST['question'+str(i)]
                    ans=request.POST[str(i)]
                    main_list=[]
                    c1=question.objects.get(question=q)
                    c2=Option.objects.filter(question=c1,is_answer=True)
                    for i in c2:
                        main_list.append(i.option_title)
                    print(main_list)    
                    if ans in main_list:
                        Answer.objects.create(owner=ow,quiz1=t,question=c1,score=True)
                change=Testappear.objects.get(t_user=ow,t_category=t)
                print('inside except')
                change.isappear=True
                change.save()
                # return redirect('')
                return redirect('stucalu',id)             
        # show_data = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        total_size = len(final_dict)
        return render(request, 'stu_question.html',{'final':final_dict, 'total_size':total_size})
        # print("Inside particular ID", id)
        # return render(request, 'stu_question.html')
    # else:
    return redirect('student_login_view')
# ##################### Dharmendra's Work END ###############################

def stu_profile(request):
    if 'enroll_no' in request.session:     
        show_data = ''
        msg = ''
        show_data = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
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
        n = registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        obj=Testappear.objects.filter(t_user=n)
        return render(request,'stu_index.html', {'obj': obj})
    return redirect('student_login_view')

def about(request):
    return render(request,'stu_about.html')

def contact(request):
    if request.POST:
        con = contactForm()
        con.name = request.POST['name']
        con.email = request.POST['email']
        con.phone = request.POST['phone']
        con.message = request.POST['message']
        con.save()
        msg = "Your response has been saved"
        return render(request,'stu_contact.html', {'msg': msg})
    return render(request,'stu_contact.html')

def stu_allcat(request):
    # if 'enroll_no' in request.session:     
    allcat = Testcategory.objects.all()
    return render(request,'stu_allcat.html', {'allcat': allcat})
    # return render(request,'stu_allcat.html')
    # return redirect('student_login_view')

def base(request):
    return render(request,'stu_base.html')

def stu_category_calculation(request,id):
    if 'enroll_no' in request.session:
        u=registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        c=Testcategory.objects.get(id=id)
        s=Answer.objects.filter(quiz1=c)
        q=question.objects.filter(categoryName=c) 
        ans=len(s)
        total_quest=len(q)
        final=(ans*100)/total_quest
        print(ans)
        print(total_quest)
        print(final)
        print('inside stujjjjjjjjjjjjjjjjj')

        StudentReport.objects.create(stu_name=u,cat_name=c,percentage=final)
        return redirect('stu_result')    
    return redirect('student_login_view')
    



def stu_catWiseResult(request, id):
    if 'enroll_no' in request.session:     
        show_data=registerform.objects.get(Enrollment_No = request.session['enroll_no'])
        all_cat_question = question.objects.filter(categoryName = id)
        
        all_data = StudentReport.objects.filter(stu_name = show_data)
        print(all_data)
        
        return render(request,'stu_catWiseResult.html', {'all_data': all_data})
    return redirect('student_login_view')

