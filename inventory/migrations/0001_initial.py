# Generated by Django 2.1.3 on 2018-12-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Sold out'), ('RESTOCKING', 'Item will restoking in few days')], default='SolD', max_length=250)),
                ('issues', models.CharField(default='No issues', max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Sold out'), ('RESTOCKING', 'Item will restoking in few days')], default='SolD', max_length=250)),
                ('issues', models.CharField(default='No issues', max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Sold out'), ('RESTOCKING', 'Item will restoking in few days')], default='SolD', max_length=250)),
                ('issues', models.CharField(default='No issues', max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
