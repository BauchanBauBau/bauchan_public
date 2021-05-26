# Generated by Django 3.1.7 on 2021-05-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210523_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_top_title', models.CharField(max_length=25, verbose_name='トップタイトル')),
                ('home_sub_title', models.CharField(max_length=25, verbose_name='サブタイトル')),
            ],
        ),
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_keywords', models.CharField(max_length=30, verbose_name='metaタグ(name="keywords")')),
                ('meta_description', models.CharField(max_length=120, verbose_name='metaタグ(name="description")')),
                ('meta_prop_ogTitle', models.CharField(max_length=30, verbose_name='metaタグ(property="og:title")')),
                ('meta_prop_ogImage', models.ImageField(blank=True, upload_to='images/', verbose_name='metaタグ(property="og:image")')),
                ('meta_prop_ogWidth', models.PositiveSmallIntegerField(verbose_name='metaタグ(property="og:image:width")')),
                ('meta_prop_ogHeight', models.PositiveSmallIntegerField(verbose_name='metaタグ(property="og:image:height")')),
                ('meta_prop_ogDescription', models.CharField(max_length=120, verbose_name='metaタグ(property="og:description")')),
                ('meta_prop_ogSiteName', models.CharField(max_length=30, verbose_name='metaタグ(property="og:site_name")')),
                ('meta_prop_ogUrl', models.URLField(verbose_name='metaタグ(property="og:url")')),
                ('meta_twi_imgSrc', models.ImageField(blank=True, upload_to='images/', verbose_name='metaタグ(name="twitter:image:src")')),
                ('meta_twi_title', models.CharField(max_length=120, verbose_name='metaタグ(name="twitter:title")')),
            ],
        ),
    ]