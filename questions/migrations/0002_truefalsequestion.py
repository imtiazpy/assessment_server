# Generated by Django 4.1.7 on 2023-03-13 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0002_assessment_is_public'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='Question')),
                ('is_true', models.BooleanField(default=False, help_text='Is this true')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tf_questions', to='assessments.assessment', verbose_name='Assessment')),
            ],
            options={
                'verbose_name': 'True False Question',
                'verbose_name_plural': 'True False Questions',
            },
        ),
    ]
