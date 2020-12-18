# Generated by Django 3.1.1 on 2020-12-07 06:24

from django.db import migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20201207_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='winner',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='winner',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]