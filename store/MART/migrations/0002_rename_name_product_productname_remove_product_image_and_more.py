# Generated by Django 4.0.3 on 2022-12-22 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MART', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='productName',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
