# Generated by Django 3.2.5 on 2021-07-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photodiary',
            name='image',
            field=models.ImageField(default='default-image.jpg', upload_to='doors/'),
        ),
    ]