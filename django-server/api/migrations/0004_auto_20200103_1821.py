# Generated by Django 2.2.5 on 2020-01-03 12:51

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200103_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='csv_data',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='dataframe',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False, null=True),
        ),
    ]
