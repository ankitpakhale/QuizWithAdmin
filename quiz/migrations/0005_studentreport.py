# Generated by Django 3.2.8 on 2022-06-04 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_testappear_isappear'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.CharField(max_length=100)),
                ('cat_name', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.testcategory')),
                ('stu_name', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.registerform')),
            ],
        ),
    ]
