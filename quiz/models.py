from operator import mod
from django.db import models

class registerform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    Enrollment_No=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    Attendance=models.PositiveIntegerField(default=0)
    cgpa=models.CharField("CGPA",default='',max_length=10,blank=True)
    gpa=models.CharField("GPA",default='',max_length=10,blank=True)
    review=models.TextField(default="",blank=True)
    score=models.PositiveIntegerField(default=0,blank=True,)
    def __str__(self):
        return self.name

class AdminForm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Testcategory(models.Model):
    name=models.CharField(max_length=280,default="",blank=True,null=True)
    
    def __str__(self):
        return self.name

class Testappear(models.Model):
    t_category=models.ForeignKey(Testcategory,on_delete=models.CASCADE, null=True,)
    t_user=models.ForeignKey(registerform,on_delete=models.CASCADE, null=True,)
    isappear=models.BooleanField(default=False)
    dat=models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.t_user
    
# kaam ka nhi hai --> Quiz
class Quiz123(models.Model):
    title=models.CharField(max_length=10)
    category=models.ForeignKey(Testcategory,on_delete=models.CASCADE, null=True, default="")
    time_stamp=models.DateField(auto_now=True)
    def __str__(self):
        return self.title

class question(models.Model):
    categoryName=models.ForeignKey(Testcategory, on_delete=models.CASCADE, null=True, default="")
    question=models.TextField()
    # time=models.TimeField()
    # student=models.ForeignKey(registerform, on_delete=models.CASCADE, null=True, default="")
    # option1=models.CharField(max_length=280,default="",blank=True,null=True)
    # option2=models.CharField(max_length=280,default="",blank=True,null=True)
    # option3=models.CharField(max_length=280,default="",blank=True,null=True)
    # correct=models.CharField(max_length=280,default="",blank=True,null=True)
    def __str__(self):
        return self.question

class Answer(models.Model):
    owner=models.ForeignKey(registerform,on_delete=models.CASCADE, null=True, default="")
    quiz1=models.ForeignKey(Testcategory, on_delete=models.CASCADE, null=True, default="")
    question=models.ForeignKey(question, on_delete=models.CASCADE, null=True, default="")
    score=models.BooleanField()
    
    def __str__(self):
        return str(self.question)

class StudentReport(models.Model):
    stu_name=models.ForeignKey(registerform,on_delete=models.CASCADE, null=True, default="")
    cat_name=models.ForeignKey(Testcategory, on_delete=models.CASCADE, null=True, default="")
    percentage=models.CharField(max_length=100) 
    def __str__(self):
        return str(self.percentage)

# kaam ka nhi hai --> Records
class Record(models.Model):
    student=models.ForeignKey(registerform,on_delete=models.CASCADE,null=True,default="")
    # Attendance=models.PositiveIntegerField()
    # cgpa=models.CharField("CGPA",max_length=10)
    # gpa=models.CharField("GPA",max_length=10)
    # review=models.TextField(default="",blank=True,null=True)
    # score=models.PositiveIntegerField()
    def __str__(self):
        return str(self.student)

class Option(models.Model): 
    question=models.ForeignKey(question, on_delete=models.CASCADE, null=True, default="")
    option_title=models.CharField(max_length=10)
    is_answer=models.BooleanField(default=False)

    def __str__(self):
        return str(self.option_title)
    
class contactForm(models.Model):
    name = models.CharField(default="", max_length=30)
    email = models.EmailField(default="")
    phone = models.PositiveIntegerField(default="")
    message = models.TextField(default="")
    def __str__(self):
        return self.name