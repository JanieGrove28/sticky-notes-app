from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note"
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note")


class NoteViewTests(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="View Test Note",
            content="Testing view"
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Note")

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, 302)  # redirect after create
        self.assertTrue(Note.objects.filter(title='New Note').exists())
