# Generated by Django 3.2.8 on 2022-06-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20220601_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='cgpa',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='CGPA'),
        ),
        migrations.AlterField(
            model_name='registerform',
            name='gpa',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='GPA'),
        ),
    ]