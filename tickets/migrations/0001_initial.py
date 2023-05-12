# Generated by Django 3.2.15 on 2023-04-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrawResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.DateField()),
                ('winning_ticket_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representative_name', models.CharField(max_length=100)),
                ('representative_email', models.EmailField(max_length=254)),
                ('ticket_number', models.CharField(max_length=10)),
            ],
        ),
    ]