# Generated by Django 3.0.8 on 2020-07-22 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id_Number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Full_Name', models.TextField(max_length=100)),
                ('Email', models.TextField(max_length=100)),
                ('Contact', models.BigIntegerField()),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_ID', models.AutoField(default=100, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=100)),
                ('Status_Dept', models.TextField(max_length=100)),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
        ),
    ]
