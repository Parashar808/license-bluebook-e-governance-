# Generated by Django 4.0.4 on 2022-07-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0009_remove_bluebook_nationalid_remove_license_nationalid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationalid',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
