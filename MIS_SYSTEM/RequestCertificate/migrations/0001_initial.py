# Generated by Django 3.0.8 on 2020-08-11 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifacate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Certificate_To_Request', models.CharField(max_length=60)),
                ('Others_Certificate', models.CharField(max_length=60, null=True)),
                ('Reason', models.TextField(max_length=150, null=True)),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'Certifacate',
            },
        ),
    ]
