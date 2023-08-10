# Generated by Django 4.2.4 on 2023-08-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscription_status', models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], max_length=20)),
            ],
        ),
    ]