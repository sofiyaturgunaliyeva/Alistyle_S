# Generated by Django 4.2 on 2023-06-15 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0006_izoh'),
        ('userapp', '0002_accaunt_delete_foydalanuvchi'),
        ('buyurtma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umumiy_summa', models.IntegerField()),
                ('sana', models.DateField(auto_now_add=True)),
                ('holat', models.CharField(max_length=30)),
                ('accaunt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.accaunt')),
            ],
        ),
        migrations.RenameField(
            model_name='tanlangan',
            old_name='account',
            new_name='accaunt',
        ),
        migrations.CreateModel(
            name='SavatItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('summa', models.PositiveSmallIntegerField()),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('savat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.savat')),
            ],
        ),
    ]
