# Generated by Django 4.0.6 on 2023-04-25 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0021_remove_license_fine_fine_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license_fine',
            name='national_id',
        ),
        migrations.AddField(
            model_name='license',
            name='fine',
            field=models.CharField(max_length=1000000, null='TRUE'),
            preserve_default='TRUE',
        ),
        migrations.AddField(
            model_name='license_fine',
            name='nid',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='license.license'),
            preserve_default='True',
        ),
    ]
