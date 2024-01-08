# Generated by Django 4.2 on 2024-01-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='contentmodal',
            name='category',
            field=models.CharField(max_length=120),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]