# Generated by Django 4.1.3 on 2022-12-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Post uchun sarlavha', max_length=30, verbose_name='Post nomi')),
                ('image', models.ImageField(help_text='Post uchun rasmini kiriting help text', upload_to='post-images', verbose_name='Post uchun rasm')),
            ],
        ),
    ]
