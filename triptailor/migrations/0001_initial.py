# Generated by Django 2.0.2 on 2018-02-13 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isCity', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=14)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=14)),
                ('description', models.TextField()),
                ('sequence', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('stars', models.IntegerField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_travelers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maxNumTravelers', models.IntegerField()),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('categories', models.ManyToManyField(related_name='trips', to='triptailor.Category')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='triptailor.Guide')),
                ('travelers', models.ManyToManyField(through='triptailor.Ticket', to='triptailor.Traveler')),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='traveler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptailor.Traveler'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptailor.Trip'),
        ),
        migrations.AddField(
            model_name='review',
            name='traveler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='triptailor.Traveler'),
        ),
        migrations.AddField(
            model_name='review',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='location', to='triptailor.Trip'),
        ),
        migrations.AddField(
            model_name='location',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locaitons', to='triptailor.Trip'),
        ),
    ]