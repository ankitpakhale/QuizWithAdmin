from operator import mod
from django.db import models


class registerform(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Enrollment_No = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    Attendance = models.PositiveIntegerField(default=0, blank=True)
    cgpa = models.IntegerField("CGPA", default=0, blank=True)
    gpa = models.IntegerField("GPA", default=0, blank=True)
    review = models.IntegerField(default=0, blank=True)
    score = models.PositiveIntegerField(default=0, blank=True,)

    def __str__(self):
        return self.name


class Testcategory(models.Model):
    name = models.CharField(max_length=280, default="", blank=True, null=True)

    def __str__(self):
        return self.name


class StudentReport(models.Model):
    stu_name = models.ForeignKey(
        registerform, on_delete=models.CASCADE, null=True, default="")
    cat_name = models.ForeignKey(
        Testcategory, on_delete=models.CASCADE, null=True, default="")
    percentage = models.FloatField(max_length=100)

    def __str__(self):
        return str(self.percentage)

class StudentMarks(models.Model):
    stu_name = models.ForeignKey(
        registerform, on_delete=models.CASCADE, null=True, default="")
    cat_name = models.CharField(max_length=100)
    percentage = models.FloatField(max_length=100)

    def __str__(self):
        return str(self.cat_name)


class AdminForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Testappear(models.Model):
    t_category = models.ForeignKey(
        Testcategory, on_delete=models.CASCADE, null=True,)
    t_user = models.ForeignKey(
        registerform, on_delete=models.CASCADE, null=True,)
    isappear = models.BooleanField(default=False)
    dat = models.DateField(auto_now_add=True)


class Quiz123(models.Model):
    title = models.CharField(max_length=10)
    category = models.ForeignKey(
        Testcategory, on_delete=models.CASCADE, null=True, default="")
    time_stamp = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class question(models.Model):
    categoryName = models.ForeignKey(
        Testcategory, on_delete=models.CASCADE, null=True, default="")
    question = models.TextField(max_length=1000)

    def __str__(self):
        return self.question


class Answer(models.Model):
    owner = models.ForeignKey(
        registerform, on_delete=models.CASCADE, null=True, default="")
    quiz1 = models.ForeignKey(
        Testcategory, on_delete=models.CASCADE, null=True, default="")
    question = models.ForeignKey(
        question, on_delete=models.CASCADE, null=True, default="")
    score = models.BooleanField()

    def __str__(self):
        return str(self.question)


class Record(models.Model):
    student = models.ForeignKey(
        registerform, on_delete=models.CASCADE, null=True, default="")

    def __str__(self):
        return str(self.student)


class Option(models.Model):
    question = models.ForeignKey(
        question, on_delete=models.CASCADE, null=True, default="")
    option_title = models.CharField(max_length=1000)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.option_title)


class contactForm(models.Model):
    name = models.CharField(default="", max_length=30)
    email = models.EmailField(default="")
    phone = models.PositiveIntegerField(default="")
    message = models.TextField(default="")

    def __str__(self):
        return self.name


# ************************* New Work ******************************
class newQuestion(models.Model):
    question = models.TextField()
    option1 = models.CharField(
        "Answer 1", max_length=280, default="", blank=True, null=True)
    option2 = models.CharField(
        "Answer 2", max_length=280, default="", blank=True, null=True)
    option3 = models.CharField(
        "Answer 3", max_length=280, default="", blank=True, null=True)
    option4 = models.CharField(
        "Answer 4", max_length=280, default="", blank=True, null=True)
    ans = models.CharField("Answer", max_length=280, default="", blank=True)

    categoryName = models.CharField(
        "Category Name", max_length=280, default="", blank=True, null=True)

    def __str__(self):
        return self.question
