# Generated by Django 4.1.7 on 2023-03-13 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0002_assessment_is_public'),
        ('questions', '0002_truefalsequestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Write down the answer for the Short Answer Question', max_length=1000, verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='SAQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='Question Content')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sa_questions', to='assessments.assessment', verbose_name='Assessment')),
            ],
            options={
                'verbose_name': 'Short Answer Question',
                'verbose_name_plural': 'Short Answer Questions',
            },
        ),
        migrations.CreateModel(
            name='TFQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='Question Content')),
                ('is_true', models.BooleanField(default=False, help_text='Is this true')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tf_questions', to='assessments.assessment', verbose_name='Assessment')),
            ],
            options={
                'verbose_name': 'True False Question',
                'verbose_name_plural': 'True False Questions',
            },
        ),
        migrations.AlterField(
            model_name='mcquestion',
            name='content',
            field=models.CharField(max_length=500, verbose_name='Question Content'),
        ),
        migrations.DeleteModel(
            name='TrueFalseQuestion',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.saquestion', verbose_name='Question'),
        ),
    ]
