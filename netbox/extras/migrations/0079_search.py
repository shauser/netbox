# Generated by Django 4.1.1 on 2022-10-10 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('extras', '0078_unique_constraints'),
    ]

    operations = [
        migrations.CreateModel(
            name='CachedValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveBigIntegerField()),
                ('field', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=30)),
                ('value', models.TextField()),
                ('weight', models.PositiveSmallIntegerField(default=1000)),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ('weight', 'pk'),
            },
        ),
    ]
