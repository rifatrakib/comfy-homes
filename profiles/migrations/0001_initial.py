# Generated by Django 4.0.4 on 2022-05-28 09:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='username connecting profile owner with user account', max_length=150, unique=True, verbose_name='profile owner username')),
                ('first_name', models.CharField(error_messages={'max_length': 'First name can be at most 150 characters.', 'required': 'Must provide a first name.'}, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(error_messages={'max_length': 'Last name can be at most 150 characters.', 'required': 'Must provide a last name.'}, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this profile should be treated as active.', verbose_name='active status')),
                ('last_name_first', models.BooleanField(default=False, verbose_name='show last name first')),
                ('nicknames', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, verbose_name='add nicknames'), default=list, help_text='add up to 5 nicknames', size=5)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True, verbose_name='gender')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='add birthday')),
                ('short_bio', models.CharField(blank=True, max_length=1000, null=True, verbose_name='add a short introduction')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('profile_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, verbose_name='add special tags to profile'), default=list, help_text='add important tags so that others can find you easily', size=10)),
                ('mail_accounts', models.JSONField(blank=True, help_text='link your email addresses', null=True, verbose_name='add emails')),
                ('phone_numbers', models.JSONField(blank=True, help_text='link your phone numbers', null=True, verbose_name='add phone numbers')),
                ('social_links', models.JSONField(blank=True, help_text='link your social world', null=True, verbose_name='add social accounts')),
                ('places', models.JSONField(blank=True, help_text='places you have lived in', null=True, verbose_name='add places')),
                ('educations', models.JSONField(blank=True, help_text='educational institutes you have studied at', null=True, verbose_name='add educations')),
                ('workplaces', models.JSONField(blank=True, help_text='companies you have worked at', null=True, verbose_name='add workplaces')),
                ('cover_picture', models.URLField(blank=True, help_text='cover picture will be displayed in your profile page', null=True, verbose_name='add cover picture')),
            ],
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['username'], name='profiles_pr_usernam_b7f118_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['first_name'], name='profiles_pr_first_n_cd868f_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['last_name'], name='profiles_pr_last_na_47702d_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['gender'], name='profiles_pr_gender_fc2e15_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['first_name', 'last_name'], name='profiles_pr_first_n_360bc4_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['first_name', 'gender'], name='profiles_pr_first_n_4f5370_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['last_name', 'gender'], name='profiles_pr_last_na_78427c_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['first_name', 'last_name', 'gender'], name='profiles_pr_first_n_469619_idx'),
        ),
    ]
