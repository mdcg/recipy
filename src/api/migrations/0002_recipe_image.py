# Generated by Django 2.2.4 on 2019-08-29 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default=1, upload_to='recipes/'),
            preserve_default=False,
        ),
    ]
