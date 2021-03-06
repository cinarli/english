# Generated by Django 3.1.2 on 2020-10-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('translate', models.CharField(max_length=255)),
                ('key', models.CharField(editable=False, max_length=12)),
            ],
            options={
                'unique_together': {('name', 'translate')},
            },
        ),
    ]
