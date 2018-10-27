# Generated by Django 2.0.2 on 2018-10-23 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_no', models.CharField(max_length=50, verbose_name='Page No')),
                ('question_no', models.CharField(max_length=50, verbose_name='Question No')),
                ('question', models.TextField(verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('chapter_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapter.Chapter')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapter.classes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapter.Subject')),
            ],
            options={
                'verbose_name': 'Question Bank',
                'verbose_name_plural': 'Question Banks',
            },
        ),
    ]