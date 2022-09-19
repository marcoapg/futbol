# Generated by Django 4.1.1 on 2022-09-17 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='competicion',
            fields=[
                ('competicion_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('pais_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='deporte',
            fields=[
                ('deporte_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='detalle_grupo',
            fields=[
                ('detalle_grupo_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='grupo',
            fields=[
                ('grupo_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='pais',
            fields=[
                ('pais_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_competicion',
            fields=[
                ('tipo_competicion_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='tabla',
            fields=[
                ('tabla_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ganado', models.IntegerField()),
                ('perdido', models.IntegerField()),
                ('empatado', models.IntegerField()),
                ('goles_favor', models.IntegerField()),
                ('goles_contra', models.IntegerField()),
                ('tarjetas_amarillas', models.IntegerField()),
                ('tarjetas_rojas', models.IntegerField()),
                ('puntos', models.IntegerField()),
                ('competicion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.competicion')),
            ],
        ),
    ]