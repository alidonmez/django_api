from django.test import TestCase
from ..models import FormEntry
from datetime import datetime

class FormTest(TestCase):
    """ test module for FormEntry model """

    def setUp(self):
        FormEntry.objects.create(
            name='Jon Jones',
            dob='1900-1-1',
            notes='free text field'
        )

    def test_get_dob(self):
        jon = FormEntry.objects.get(name='Jon Jones')
        self.assertEqual(
            jon.get_dob(), datetime.strptime('1900-1-1', "%Y-%m-%d").date())

    