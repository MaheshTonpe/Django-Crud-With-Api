# Generated by Django 5.0.4 on 2024-04-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
        migrations.AddField(
            model_name='employee',
            name='employeeemail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employeelocation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employeename',
            field=models.CharField(max_length=50, null=True),
        ),
    ]