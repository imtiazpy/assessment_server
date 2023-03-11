# Generated by Django 4.1.7 on 2023-03-11 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_type', models.CharField(blank=True, choices=[('IT', 'Information Technology'), ('INTERNET', 'Internet'), ('SOFTWARE', 'Software')], max_length=70, null=True, verbose_name='Industry Type')),
                ('hq', models.CharField(blank=True, max_length=100, null=True, verbose_name='Head Quarter')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('company_size', models.CharField(blank=True, choices=[('1-9', '1-9'), ('10-49', '10-49'), ('50-249', '50-249')], max_length=70, null=True, verbose_name='Company Size')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('year_of_form', models.CharField(blank=True, max_length=4, null=True, verbose_name='Year Of Form')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]