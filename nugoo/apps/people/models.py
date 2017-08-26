import random
import uuid
from django.db import models
from django.urls import reverse


class Hashtag(models.Model):
    name = models.CharField(
        '이름',
        max_length=20,
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(
        '이름',
        max_length=60,
    )
    events = models.ManyToManyField(
        'Event',
        through='PersonToEvent',
        related_name='person_set',
        verbose_name='사건들',
        blank=True,
    )
    hashtags = models.ManyToManyField(
        Hashtag,
        related_name='person_set',
        verbose_name='해시태그',
        blank=True,
    )

    def get_photo_upload_to(self, filename):
        return "{}/{}/{}.{}".format(
            self.__class__.__name__.lower(),
            'photo',
            uuid.uuid4(),
            filename.split(".")[-1],
        )
    photo = models.ImageField(
        '사진',
        upload_to=get_photo_upload_to,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people:person-detail', args=[self.pk])

    def get_hashtags(self):
        return self.hashtags.order_by('?')

    def get_stat(self):
        stats = self.stat_set.all()
        if stats:
            index = random.randrange(len(stats))
            return stats[index]
        else:
            return None


class PersonToEvent(models.Model):
    person = models.ForeignKey(
        Person,
        models.SET_NULL,
        related_name='event_throughs',
        verbose_name='인물',
        blank=True,
        null=True,
    )
    event = models.ForeignKey(
        'Event',
        models.SET_NULL,
        related_name='person_throughs',
        verbose_name='사건',
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{} : {}".format(self.person, self.event)


class Event(models.Model):
    name = models.CharField(
        '이름',
        max_length=255,
    )
    reference = models.URLField(
        '참조 자료',
        blank=True,
    )

    def __str__(self):
        return self.name


class Stat(models.Model):
    person = models.ForeignKey(
        Person,
        models.SET_NULL,
        related_name='stat_set',
        verbose_name='인물',
        blank=True,
        null=True,
    )
    name = models.CharField(
        '이름',
        max_length=10,
    )
    value = models.SmallIntegerField(
        '능력치 값',
    )

    def __str__(self):
        return "{} : {}".format(self.person, self.name)
