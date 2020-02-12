# Generated by Django 3.0.3 on 2020-02-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_text', models.CharField(max_length=1000000)),
                ('latest_access', models.DateTimeField(verbose_name='Último acesso')),
                ('latest_user', models.CharField(max_length=200)),
            ],
        ),
    ]
