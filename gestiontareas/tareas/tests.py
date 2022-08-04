from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from . import models
from django.utils import timezone


class TareaViewSetTest(APITestCase):
    print("running TasksListCreateAPIViewTest")

    def setUp(self):
        self.url = reverse('tareas')
        self.tarea_1 = models.Tarea.objects.create(
            name='Tarea 1',
            description='Prueba tarea',
            status='DONE',
            priority='MEDIUM',
            date_of_delivery=timezone.now(),
            comments=''
        )

        self.task_2 = models.Tarea.objects.create(
            name='Tarea 2',
            description='Prueba tarea 2',
            status='DONE',
            priority='MEDIUM',
            date_of_delivery=timezone.now(),
            comments=''
        )

    def test_get_all_tareas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        count_db_objects = models.Tarea.objects.all().count()
        self.assertEqual(count_db_objects, 2)
