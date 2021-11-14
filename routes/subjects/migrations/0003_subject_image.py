# Generated by Django 3.2.9 on 2021-11-14 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_rename_url_file_file'),
        ('subjects', '0002_alter_subject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='files.file'),
            preserve_default=False,
        ),
    ]
