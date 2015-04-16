# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_polymorphic_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_polymorphic_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='django_polymorphic_auth.User')),
                ('email', models.EmailField(help_text='Required. Unique.', unique=True, max_length=254, verbose_name='email address', error_messages={b'unique': 'A user with that email address already exists.'})),
                ('first_name', models.CharField(help_text='Required.', max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(help_text='Required.', max_length=255, verbose_name='last name')),
            ],
            options={
                'verbose_name': 'user with email login',
                'verbose_name_plural': 'users with email login',
            },
            bases=(django_polymorphic_auth.models.NameMethodsMixin, 'django_polymorphic_auth.user', models.Model),
            managers=[
                (b'objects', django_polymorphic_auth.models.UserManager()),
            ],
        ),
    ]