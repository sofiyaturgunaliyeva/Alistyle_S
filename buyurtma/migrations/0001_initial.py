# Generated by Django 4.2 on 2023-06-15 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0002_accaunt_delete_foydalanuvchi'),
        ('asosiy', '0006_izoh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tanlangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.accaunt')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]