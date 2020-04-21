# Generated by Django 3.0.5 on 2020-04-20 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='some', max_length=400)),
                ('description', models.TextField(default='')),
                ('city', models.CharField(default='Something', max_length=300)),
                ('address', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name1', max_length=300)),
                ('salary', models.FloatField(default=1000)),
                ('description', models.TextField(default='')),
                ('comp', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='api.Company')),
            ],
        ),
    ]
