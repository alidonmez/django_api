import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import FormEntry
from ..serializers import FormEntrySerializer


client = Client()


class GetAllformsTest(TestCase):
    """ Test module for GET all forms API """

    def setUp(self):
        self.entry = FormEntry.objects.create(
            name='Jon Jones',
            dob='1900-1-1',
            notes='free text field'
        )

    def test_get_all_forms(self):
        response = client.get(reverse('get_post_forms'))

        forms = FormEntry.objects.all()
        serializer = FormEntrySerializer(forms, many=True)
    
        self.assertEqual(response.data, serializer.data)    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(serializer.data)

class GetSingleFormEntryTest(TestCase):
    """ Test module for GET single form API """

    def setUp(self):
        self.entry = FormEntry.objects.create(
            name='Jon Jones',
            dob='1900-1-1',
            notes='free text field'
        )

        self.entry2 = FormEntry.objects.create(
            name='Steve Stevens',
            dob='2000-2-2',
            notes='text field'
        )

    def test_get_valid_single_form(self):
        response = client.get(
            reverse('get_delete_update_forms', kwargs={'pk': self.entry2.pk}))
        form = FormEntry.objects.get(pk=self.entry2.pk)
        serializer = FormEntrySerializer(form)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_form(self):
        response = client.get(
            reverse('get_delete_update_forms', kwargs={'pk': 3000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print(response)

class CreateNewFormEntryTest(TestCase):
    """ Test module for inserting a new form """

    def setUp(self):
        self.valid = {
            'name': 'Jon Jones',
            'dob': '1900-1-1',
            'notes': 'free text field'
        }
        self.invalid = {
            'name': '',
            'dob': '1900-1-1',
            'notes': 'free text field'
        }
    def test_create_valid_form(self):
        response = client.post(
            reverse('get_post_forms'),
            data=json.dumps(self.valid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_form(self):
        response = client.post(
            reverse('get_post_forms'),
            data=json.dumps(self.invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
