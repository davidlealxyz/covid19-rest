# Generated by Django 3.0.3 on 2020-03-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generaldata',
            old_name='Suspected',
            new_name='suspected',
        ),
        migrations.AddField(
            model_name='generaldata',
            name='data_file_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='report_day',
            field=models.DateField(null=True),
        ),
    ]
