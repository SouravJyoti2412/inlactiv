# Generated by Django 4.2.1 on 2023-06-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_singup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=15, null=True, verbose_name='phone number')),
                ('password', models.CharField(max_length=255)),
                ('forgetpass', models.IntegerField(blank=True, default=0, null=True)),
                ('Customer_otp', models.CharField(max_length=4)),
                ('is_number_validate', models.BooleanField(default=False)),
                ('Create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Student List',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
