# Generated by Django 2.0.2 on 2018-10-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationteacher',
            name='teacher_mobile_no',
            field=models.CharField(max_length=10, verbose_name='Teacher mobile no'),
        ),
    ]
