# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from test_app.models import MediaTestUUIDPKModel, MediaTestModel
from thecut.media.models import AttachedMediaItem
from thecut.media.mediasources.models import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings
import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):

    email = factory.Sequence(lambda n: '{}@users.example.com'.format(n))

    class Meta(object):
        django_get_or_create = ['email']
        model = User


class TestAttachingMediaItemsToModels(TestCase):
    def test_attaching_uuid_pk(self):
        m = MediaTestUUIDPKModel()
        m.save()

        u = UserFactory()
        i = Image()
        i.created_by = u
        i.updated_by = u
        i.image = SimpleUploadedFile(name='German_Flag.jpg', content=open(
            os.path.join(settings.BASE_DIR,
                         'thecut/media/tests/assets/German_Flag.jpg'), 'rb'
                         ).read(), content_type='image/jpeg')
        i.save()

        ami = AttachedMediaItem()
        ami.content_object = i
        ami.parent_content_object = m
        ami.save()

        # Reload the model and check everything is as we expect it
        self.assertEqual(len(MediaTestModel.objects.all()), 1)
        m2 = MediaTestModel.objects.first()
        self.assertEqual(m2.pk, m.pk)
        self.assertEqual(len(m2.media.all()), 1)
        self.assertEqual(m2.media.all()[0].pk, ami.pk)
        self.assertEqual(m2.media.all()[0].content_object.pk,
                         ami.content_object.pk)

    def test_attaching_int_pk(self):
        m = MediaTestModel()
        m.save()

        u = UserFactory()
        i = Image()
        i.created_by = u
        i.updated_by = u
        i.image = SimpleUploadedFile(name='German_Flag.jpg', content=open(
            os.path.join(settings.BASE_DIR,
                         'thecut/media/tests/assets/German_Flag.jpg'), 'rb'
                         ).read(), content_type='image/jpeg')
        i.save()

        ami = AttachedMediaItem()
        ami.content_object = i
        ami.parent_content_object = m
        ami.save()

        # Reload the model and check everything is as we expect it
        self.assertEqual(len(MediaTestModel.objects.all()), 1)
        m2 = MediaTestModel.objects.first()
        self.assertEqual(m2.pk, m.pk)
        self.assertEqual(len(m2.media.all()), 1)
        self.assertEqual(m2.media.all()[0].pk, ami.pk)
        self.assertEqual(m2.media.all()[0].content_object.pk,
                         ami.content_object.pk)
