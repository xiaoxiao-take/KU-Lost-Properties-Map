# Generated by Django 4.1 on 2023-05-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_my_lost_property', '0004_alter_lostproperty_true_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostproperty',
            name='dummy_image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lostproperty',
            name='dummy_image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lostproperty',
            name='dummy_image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lostproperty',
            name='dummy_image4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]