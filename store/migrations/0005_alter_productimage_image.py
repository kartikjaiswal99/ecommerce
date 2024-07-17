# Generated by Django 4.2.12 on 2024-07-17 12:13

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='store/images', validators=[store.validators.validate_file_size]),
        ),
    ]