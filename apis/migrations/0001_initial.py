# Generated by Django 3.2.13 on 2022-04-14 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regisration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=13)),
                ('userimage', models.ImageField(upload_to='images/')),
                ('password', models.CharField(max_length=300)),
                ('is_active', models.BooleanField(default=True)),
                ('is_loggedin', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Regisration',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=13)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.regisration')),
            ],
            options={
                'db_table': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Charts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentto', models.CharField(max_length=13)),
                ('message', models.CharField(max_length=5000)),
                ('date_sent', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.regisration')),
            ],
            options={
                'db_table': 'Charts',
            },
        ),
    ]
