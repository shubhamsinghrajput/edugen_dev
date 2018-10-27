# Generated by Django 2.0.2 on 2018-10-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0009_auto_20181023_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbank',
            name='category',
            field=models.CharField(choices=[('0', 'Intext'), ('1', 'Textbook Exercise')], max_length=50, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='question_type',
            field=models.CharField(choices=[('0', 'Oral Questions'), ('1', 'Name of the following ')], max_length=50, verbose_name='Question Type'),
        ),
    ]
