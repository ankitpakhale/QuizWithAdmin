from unicodedata import category
from django.shortcuts import render,redirect
from .models import Answer, registerform,question,Record,AdminForm,Testcategory
from django.http import HttpResponse

# Create your views here.
def index(request):
    a=Record.objects.all()
    count=Record.objects.all().count()
    q=question.objects.all()
    return render(request,'index.html',{'data':a,'c':count,'q':len(q)})



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
        time=request.POST['time']
        option1=request.POST['option1']
        option2=request.POST['option2']
        option3=request.POST['option3']
        answer=request.POST['check']

        if answer=='1':
            answer=option1
        elif answer=='2':
            answer=option2    
        else:
            answer=option3
        
        obj=Testcategory.objects.get(name=category)
            
        q=question()
        q.categoryName=obj
        q.question=getquestion
        q.time=time
        q.option1=option1
        q.option2=option2
        q.option3=option3
        q.correct=answer
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

def edit_testcategory(request,id):
    obj=Testcategory.objects.get(id=id)    
    if request.POST:
        name=request.POST['name']
        obj.name=name
        obj.save()
        return redirect('index1')
    return render(request,'edit_category.html',{'obj':obj})        

def view_category(request):
    obj=Testcategory.objects.all()    
    return render(request,'view_category.html',{'obj':obj})        

def edit_questions(request,id):
    obj=question.objects.get(id=id)
    name1=str(obj.categoryName)
    al=Testcategory.objects.all()
    if request.POST:
        category=request.POST['category']
        getquestion=request.POST['question']
        option1=request.POST['option1']
        option2=request.POST['option2']
        option3=request.POST['option3']
        answer=request.POST['check']

        if answer=='1':
            answer=option1
        elif answer=='2':
            answer=option2    
        else:
            answer=option3
        
        obj1=Testcategory.objects.get(name=category)

            
        
        obj.categoryName=obj1
        obj.question=getquestion
        obj.option1=option1
        obj.option2=option2
        obj.option3=option3
        obj.time='00:20'
        obj.correct=answer
        obj.save()
        return redirect('index1')

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
                request.session['email'] = model.id
                return redirect('index1')
            else:
                return HttpResponse("<a href = ''>Incorrect details</a>")
        except:
            return HttpResponse("<a href = ''>Incorrect details</a>")
    return render(request,'sign.html')