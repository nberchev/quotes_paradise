# Generated by Django 3.1.3 on 2020-11-23 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=2, null=True)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.quote')),
            ],
        ),
    ]