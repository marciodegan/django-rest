# Generated by Django 3.0.6 on 2020-05-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20200510_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='city',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customers',
            name='company',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customers',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
