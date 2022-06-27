# Generated by Django 4.0.4 on 2022-06-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='savings',
            name='category',
            field=models.CharField(blank=True, choices=[('F', 'Funds'), ('C', 'Crypto')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='savings',
            name='enterprise',
            field=models.CharField(blank=True, choices=[('R', 'Racional'), ('D', 'DVA'), ('F', 'Fintual'), ('S', 'Soy Focus'), ('B', 'Binance')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spends',
            name='category',
            field=models.CharField(blank=True, choices=[('H', 'House'), ('S', 'Supermarket'), ('I', 'Investment'), ('R', 'Rent'), ('M', 'Mortage'), ('T', 'Travel'), ('C', 'Card'), ('L', 'Light'), ('W', 'Water'), ('CE', 'Celphone'), ('IN', 'Internet'), ('ST', 'Streaming'), ('M', 'Medical'), ('P', 'Party')], max_length=100, null=True),
        ),
    ]
