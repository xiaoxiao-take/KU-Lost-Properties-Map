# Generated by Django 4.1 on 2023-05-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_my_lost_property', '0002_alter_lostproperty_found_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostproperty',
            name='true_image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]