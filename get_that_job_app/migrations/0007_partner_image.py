# Generated by Django 2.2.4 on 2020-12-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_that_job_app', '0006_remove_partner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
