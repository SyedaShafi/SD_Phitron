# Generated by Django 5.0.3 on 2024-04-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('instrument_type', models.CharField(choices=[('Guitar', 'Guitar'), ('Piano', 'Piano'), ('Violin', 'Violin'), ('Drums', 'Drums'), ('Flute', 'Flute')], max_length=20)),
            ],
        ),
    ]
