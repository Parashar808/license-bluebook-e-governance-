# Generated by Django 4.0.4 on 2022-07-16 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0007_nationalid_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bluebook',
            name='nationalid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bluebook_nationalid', to='license.nationalid'),
        ),
        migrations.AlterField(
            model_name='license',
            name='nationalid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='license_nationalid', to='license.nationalid'),
        ),
    ]
