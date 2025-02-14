# Generated by Django 2.2.3 on 2019-08-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SADAC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
            ],
        ),
    ]
