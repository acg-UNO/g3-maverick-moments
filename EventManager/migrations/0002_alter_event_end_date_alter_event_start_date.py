# Generated by Django 5.1.2 on 2024-10-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(help_text="The date if it's 1 day only, the start date if the event spans multiple days."),
        ),
    ]
