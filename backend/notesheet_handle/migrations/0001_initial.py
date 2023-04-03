# Generated by Django 4.1.7 on 2023-04-03 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllFacultyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=30)),
                ('employee_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=255)),
                ('mobile_number', models.IntegerField()),
                ('email_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NoteSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.TextField()),
                ('school', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('objective', models.TextField()),
                ('proposal_details', models.TextField()),
                ('proposal_submitted_by', models.CharField(max_length=255)),
                ('proposal_submitted_by_1', models.CharField(max_length=255)),
                ('receiver_1', models.CharField(max_length=255)),
                ('receiver_2', models.CharField(max_length=255)),
                ('Status', models.IntegerField(default='000')),
                ('f_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notesheet_handle.facultydetails')),
            ],
        ),
    ]