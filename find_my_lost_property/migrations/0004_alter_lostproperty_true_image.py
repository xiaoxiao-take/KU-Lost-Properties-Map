# Generated by Django 4.1 on 2023-05-22 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_my_lost_property', '0003_lostproperty_true_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostproperty',
            name='true_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]