# Generated by Django 4.2 on 2023-04-22 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('is_finished', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='authentication.profile')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]