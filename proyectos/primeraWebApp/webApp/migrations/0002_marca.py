# Generated by Django 5.1.1 on 2024-10-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
            ],
        ),
    ]
