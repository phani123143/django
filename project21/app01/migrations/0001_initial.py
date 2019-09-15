# Generated by Django 2.1.2 on 2019-09-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('username', models.IntegerField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
