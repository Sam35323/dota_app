# Generated by Django 4.2.2 on 2023-06-26 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=35)),
                ('disc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TopClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=35)),
                ('disc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('disc', models.CharField(max_length=300)),
                ('bio', models.CharField(max_length=300)),
                ('ultimate', models.CharField(max_length=35)),
                ('ultimate_disc', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='photos/%m/%d')),
                ('skill_1', models.CharField(max_length=35)),
                ('skill1_disc', models.CharField(max_length=300)),
                ('skill_2', models.CharField(max_length=35)),
                ('skill_2_disc', models.CharField(max_length=300)),
                ('skill_3', models.CharField(max_length=35)),
                ('skill_3_disc', models.CharField(max_length=300)),
                ('top_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotaw_app.topclass')),
                ('top_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotaw_app.position')),
            ],
        ),
    ]
