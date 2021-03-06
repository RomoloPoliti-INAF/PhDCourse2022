# Generated by Django 4.0.5 on 2022-07-05 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lavoro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lavoro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('lavoro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.lavoro')),
            ],
        ),
    ]
