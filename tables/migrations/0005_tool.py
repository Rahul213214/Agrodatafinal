# Generated by Django 4.0.2 on 2022-05-14 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0004_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('toolid', models.CharField(blank=True, max_length=60)),
                ('toolname', models.CharField(blank=True, max_length=60)),
                ('rate', models.CharField(blank=True, max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]