# Generated by Django 4.2 on 2023-06-15 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_accaunt_delete_foydalanuvchi'),
        ('asosiy', '0005_mahsulot_mavjud_mahsulot_yetkazish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.TextField()),
                ('sana', models.DateField(auto_now_add=True)),
                ('baho', models.PositiveSmallIntegerField()),
                ('accaunt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.accaunt')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]
