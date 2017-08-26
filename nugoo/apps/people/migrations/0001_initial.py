# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import nugoo.apps.people.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('reference', models.URLField(blank=True, verbose_name='참조 자료')),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='이름')),
                ('photo', models.ImageField(blank=True, upload_to=nugoo.apps.people.models.Person.get_photo_upload_to, verbose_name='사진')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_throughs', to='people.Event', verbose_name='사건')),
                ('hashtags', models.ManyToManyField(blank=True, related_name='person_to_event_set', to='people.Hashtag', verbose_name='해시태그')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_throughs', to='people.Person', verbose_name='인물')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('value', models.SmallIntegerField(verbose_name='능력치 값')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stat_set', to='people.Person', verbose_name='인물')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='people.PersonToEvent', to='people.Event', verbose_name='사건들'),
        ),
    ]
