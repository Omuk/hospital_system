# Generated by Django 4.0.4 on 2022-06-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medrec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ICDSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='user_name',
            new_name='patient',
        ),
    ]
