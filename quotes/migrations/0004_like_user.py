# Generated by Django 3.1.3 on 2020-11-26 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201126_1747'),
        ('quotes', '0003_auto_20201126_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.profileuser'),
            preserve_default=False,
        ),
    ]