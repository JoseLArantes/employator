# Generated by Django 4.2.8 on 2023-12-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_company_date_creation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='website_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='website_screenshots/'),
        ),
    ]
