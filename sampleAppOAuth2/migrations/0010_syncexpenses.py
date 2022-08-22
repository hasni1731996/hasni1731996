# Generated by Django 3.2.5 on 2021-08-12 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sampleAppOAuth2', '0009_authtoken_quickbook_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_date_time', models.DateTimeField(auto_now_add=True)),
                ('procore_created_id', models.IntegerField(blank=True, null=True)),
                ('qbo_created_id', models.IntegerField(blank=True, null=True)),
                ('procore_project_id', models.IntegerField(blank=True, null=True)),
                ('procore_vendor_id', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]