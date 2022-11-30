# Generated by Django 4.0.5 on 2022-11-30 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animestore', '0003_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.CharField(help_text='Current Status', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='Product Description', help_text='Product Description', max_length=500),
        ),
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=15)),
                ('lastName', models.CharField(help_text='Last Name', max_length=20)),
                ('email', models.EmailField(blank=True, help_text='Email Address', max_length=254, null=True)),
                ('comment', models.CharField(help_text='Give us a information of your case', max_length=500, null=True)),
                ('status', models.ForeignKey(default='New', null=True, on_delete=django.db.models.deletion.SET_NULL, to='animestore.status')),
            ],
        ),
    ]