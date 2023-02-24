# Generated by Django 4.0.3 on 2023-02-24 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='contactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.PositiveIntegerField(default='')),
                ('message', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='newQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Answer 1')),
                ('option2', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Answer 2')),
                ('option3', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Answer 3')),
                ('option4', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Answer 4')),
                ('ans', models.CharField(blank=True, default='', max_length=280, verbose_name='Answer')),
                ('categoryName', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='registerform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Enrollment_No', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('Attendance', models.PositiveIntegerField(blank=True, default=0)),
                ('cgpa', models.IntegerField(blank=True, default=0, verbose_name='CGPA')),
                ('gpa', models.IntegerField(blank=True, default=0, verbose_name='GPA')),
                ('review', models.IntegerField(blank=True, default=0)),
                ('score', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Testcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=280, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testappear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isappear', models.BooleanField(default=False)),
                ('dat', models.DateField(auto_now_add=True)),
                ('t_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.testcategory')),
                ('t_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.registerform')),
            ],
        ),
        migrations.CreateModel(
            name='StudentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(max_length=100)),
                ('cat_name', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.testcategory')),
                ('stu_name', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.registerform')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.registerform')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz123',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('time_stamp', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.testcategory')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('categoryName', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.testcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_title', models.CharField(max_length=1000)),
                ('is_answer', models.BooleanField(default=False)),
                ('question', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.BooleanField()),
                ('owner', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.registerform')),
                ('question', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('quiz1', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.testcategory')),
            ],
        ),
    ]
