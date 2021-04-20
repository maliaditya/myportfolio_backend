# Generated by Django 3.2 on 2021-04-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(choices=[('b', 'BASIC'), ('s', 'STANDARD'), ('p', 'PREMIUM')], default='b', max_length=1)),
                ('description', models.TextField()),
                ('days', models.CharField(max_length=4)),
                ('design_customization', models.BooleanField(default=True)),
                ('responsive_design', models.BooleanField(default=True)),
                ('source_code', models.BooleanField(default=True)),
                ('revisions', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('preview', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('review', models.CharField(max_length=255)),
                ('project', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('frontend_technologies', models.CharField(max_length=255)),
                ('backend_technologies', models.CharField(max_length=255)),
            ],
        ),
    ]
