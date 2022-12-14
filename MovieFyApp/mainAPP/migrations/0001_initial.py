# Generated by Django 4.1.3 on 2022-11-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=70)),
                ('origen', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=70)),
                ('origen', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('genero', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=60)),
                ('fecha_estreno', models.DateField()),
                ('presupuesto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('genero', models.CharField(max_length=30)),
                ('temporadas', models.IntegerField()),
                ('fecha_estreno', models.DateField()),
            ],
        ),
    ]
