# Generated by Django 3.2.8 on 2022-06-04 11:30

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
            name='registerform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Enrollment_No', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('Attendance', models.PositiveIntegerField(default=0)),
                ('cgpa', models.CharField(blank=True, default='', max_length=10, verbose_name='CGPA')),
                ('gpa', models.CharField(blank=True, default='', max_length=10, verbose_name='GPA')),
                ('review', models.TextField(blank=True, default='')),
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
                ('dat', models.DateField(auto_now=True)),
                ('t_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.testcategory')),
                ('t_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.registerform')),
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
                ('question', models.TextField()),
                ('categoryName', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.testcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_title', models.CharField(max_length=10)),
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
