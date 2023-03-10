# Generated by Django 2.2.12 on 2022-11-04 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_barang_waktu_posting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='barang',
            name='jenis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Jenis'),
        ),
    ]
