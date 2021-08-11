# Generated by Django 3.2.6 on 2021-08-11 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210811_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.IntegerField()),
                ('ram_used', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ram_percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('is_active', models.BooleanField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('proj_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.project')),
            ],
        ),
    ]
