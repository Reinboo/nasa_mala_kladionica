# Generated by Django 2.0.3 on 2018-04-18 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('group_key', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('result', models.IntegerField(blank=True, null=True)),
                ('score', models.CharField(blank=True, max_length=6, null=True)),
                ('odd1', models.FloatField()),
                ('oddX', models.FloatField()),
                ('odd2', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_money', models.BooleanField(default=False)),
                ('points', models.FloatField(default=0)),
                ('send_mail', models.BooleanField(default=True)),
                ('activation_code', models.CharField(max_length=255)),
                ('reset_code', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(to='nmkapp.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('group_type', models.CharField(choices=[('League', 'League'), ('Cup', 'Cup')], default='League', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nmkapp.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('group_label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot_allowed', models.BooleanField(default=True)),
                ('points', models.FloatField(default=0)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nmkapp.Round')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='shot',
            name='user_round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nmkapp.UserRound'),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='away_team', to='nmkapp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='home_team', to='nmkapp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nmkapp.Round'),
        ),
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner', to='nmkapp.Player'),
        ),
        migrations.AddField(
            model_name='group',
            name='players',
            field=models.ManyToManyField(to='nmkapp.Player'),
        ),
        migrations.AlterUniqueTogether(
            name='userround',
            unique_together={('user', 'round')},
        ),
        migrations.AlterUniqueTogether(
            name='shot',
            unique_together={('user_round', 'match')},
        ),
    ]