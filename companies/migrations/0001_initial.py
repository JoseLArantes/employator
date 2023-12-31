# Generated by Django 4.2.8 on 2023-12-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('type', models.CharField(choices=[('Company', 'Empresa'), ('Agency', 'Agência'), ('HR/Recruitment', 'RH/Recrutamento')], default='HR/Recruitment', max_length=50, verbose_name='Type')),
                ('url', models.CharField(max_length=100, verbose_name='URL')),
                ('rating', models.IntegerField(max_length=2, verbose_name='Rating')),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactivated'), ('N', 'NeverVisited')], default='N', max_length=2, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Company name',
                'verbose_name_plural': 'Companies names',
            },
        ),
    ]
