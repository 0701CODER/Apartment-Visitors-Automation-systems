# Generated by Django 4.0.3 on 2023-04-27 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avsapp', '0007_alter_addvisitor_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addvisitor',
            name='remark',
            field=models.CharField(default=0, max_length=250),
        ),
    ]
