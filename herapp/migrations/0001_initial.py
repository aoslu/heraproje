# Generated by Django 3.2.5 on 2021-07-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BriketKomur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='images')),
                ('resim_adi', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'BriketKomurResim',
                'verbose_name_plural': 'BriketKomurResimleri',
            },
        ),
        migrations.CreateModel(
            name='MeseKomur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='images')),
                ('resim_adi', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'MeseKomurResim',
                'verbose_name_plural': 'MeseKomurResimleri',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NakliyeFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='images')),
                ('resim_adi', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'NakliyeResim',
                'verbose_name_plural': 'NakliyeResimleri',
            },
        ),
        migrations.CreateModel(
            name='NargileKomuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='images')),
                ('resim_adi', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'NargileKömürResim',
                'verbose_name_plural': 'NargileKömürüResimleri',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='images')),
                ('resim_adı', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Resim',
                'verbose_name_plural': 'AnasayfadaPaylaşılanResimler',
            },
        ),
        migrations.CreateModel(
            name='PresSosisMangalKuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='images')),
                ('resim_adi', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'PresSosisMangalKuruResim',
                'verbose_name_plural': 'PresSosisMangalKuruResimleri',
            },
        ),
        migrations.CreateModel(
            name='Urunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Urunler',
                'verbose_name_plural': 'Ürünlerim',
            },
        ),
    ]