# Generated by Django 4.0.5 on 2022-06-09 12:02
# pylint:disable=line-too-long,missing-module-docstring,missing-class-docstring

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mail_domain', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MailUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_index=True, max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('password_cram_md5', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mail_domain.maildomain')),
            ],
            options={
                'db_table': 'virtual_users',
                'ordering': ['email'],
            },
        ),
    ]