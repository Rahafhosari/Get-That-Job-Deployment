# Generated by Django 2.2.4 on 2020-12-25 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_that_job_app', '0004_auto_20201226_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='get_that_job_app.Role'),
        ),
    ]
