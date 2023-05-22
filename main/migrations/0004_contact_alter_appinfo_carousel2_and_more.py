# Generated by Django 4.2 on 2023-04-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='carousel2',
            field=models.ImageField(upload_to='carouse2'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='carousel3',
            field=models.ImageField(upload_to='carouse3'),
        ),
    ]
