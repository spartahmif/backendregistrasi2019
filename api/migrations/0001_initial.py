# Generated by Django 2.2.2 on 2019-06-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_nim', models.CharField(max_length=8)),
                ('student_name', models.TextField()),
                ('student_nickname', models.CharField(max_length=10)),
                ('student_gender', models.BooleanField()),
                ('student_birthplace', models.CharField(max_length=30)),
                ('student_birthdate', models.CharField(max_length=15)),
                ('student_email', models.CharField(max_length=30)),
                ('student_line', models.CharField(max_length=30)),
                ('student_mobile', models.CharField(max_length=15)),
            ],
        ),
    ]