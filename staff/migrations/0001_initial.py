# Generated by Django 3.0.4 on 2020-04-05 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffid', models.CharField(max_length=20, unique=True)),
                ('staffname', models.CharField(max_length=30)),
                ('staffgender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('staffposition', models.CharField(max_length=30)),
                ('staffImage', models.ImageField(upload_to='static/images')),
            ],
        ),
    ]