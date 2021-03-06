# Generated by Django 3.0.8 on 2020-09-08 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo_Routing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=20, null=True)),
                ('Type_Request', models.CharField(max_length=100)),
                ('Date_Faculty_Submitted', models.DateTimeField(null=True)),
                ('Date_Chairman_Approved', models.DateTimeField(null=True)),
                ('Date_Dean_Approved', models.DateTimeField(null=True)),
                ('Date_VP_Acad_Approved', models.DateTimeField(null=True)),
                ('Date_President_Approved', models.DateTimeField(null=True)),
                ('Date_PAO_Approved', models.DateTimeField(null=True)),
                ('Date_Accounting_Approved', models.DateTimeField(null=True)),
                ('Date_HR_Approved', models.DateTimeField(null=True)),
                ('FormID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Form')),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'Memo_Routing',
            },
        ),
    ]
