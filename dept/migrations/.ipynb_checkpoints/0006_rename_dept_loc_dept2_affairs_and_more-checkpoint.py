# Generated by Django 4.0.1 on 2022-01-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0005_alter_dept2_dept_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dept2',
            old_name='dept_loc',
            new_name='affairs',
        ),
        migrations.RenameField(
            model_name='dept2',
            old_name='dept_team',
            new_name='head_num',
        ),
        migrations.RenameField(
            model_name='dept3',
            old_name='number',
            new_name='em_id',
        ),
        migrations.RenameField(
            model_name='dept3',
            old_name='name',
            new_name='em_name',
        ),
        migrations.RenameField(
            model_name='dept3',
            old_name='department',
            new_name='team_num',
        ),
        migrations.RemoveField(
            model_name='dept1',
            name='dept_name',
        ),
        migrations.RemoveField(
            model_name='dept2',
            name='dept_affairs',
        ),
        migrations.AddField(
            model_name='dept1',
            name='head_man',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='dept1',
            name='head_num',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='dept1',
            name='headquarters',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='dept2',
            name='loc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dept2',
            name='team_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='dept2',
            name='team_num',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]