# Generated by Django 4.0.1 on 2022-01-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(choices=[('기획부', '기획부'), ('경영지원본부', '경영지원본부'), ('연구개발전담부', '연구개발전담부')], max_length=20)),
                ('dept_team', models.CharField(max_length=20)),
                ('dept_affairs', models.CharField(max_length=30)),
                ('dept_loc', models.TextField()),
            ],
        ),
    ]
