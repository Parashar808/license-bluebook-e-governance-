# Generated by Django 4.0.4 on 2022-07-16 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0004_nationalid_bluebook_nationalid_license_nationalid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bluebook',
            name='nationalid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nationalId', to='license.nationalid'),
        ),
        migrations.AlterField(
            model_name='license',
            name='nationalid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nationalID', to='license.nationalid'),
        ),
    ]
