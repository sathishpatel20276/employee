# Generated by Django 3.2 on 2021-04-23 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ID', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=15)),
                ('type_of_leave', models.CharField(choices=[('Earned Leave', 'Earned Leave'), ('Casual Leave', 'Casual Leave'), ('Sick Leave', 'Sick Leave'), ('Paid Leave', 'Paid Leave')], default=None, max_length=15)),
                ('from_date', models.DateField(help_text='mm/dd/yy')),
                ('to_date', models.DateField(help_text='mm/dd/yy')),
                ('reporting_manager', models.CharField(default=None, max_length=50)),
                ('reason', models.CharField(max_length=200)),
                ('accepted', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=50)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssignedAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emsapp.asset')),
            ],
        ),
    ]
