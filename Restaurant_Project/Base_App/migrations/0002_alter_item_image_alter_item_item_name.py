# Generated by Django 5.1.4 on 2025-02-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Image',
            field=models.ImageField(upload_to='items/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='Item_Name',
            field=models.CharField(max_length=100),
        ),
    ]
