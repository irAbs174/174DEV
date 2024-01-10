from django.test import TestCase
from .models import Newsletter_Subscribe

class NewsletterSubscribeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Newsletter_Subscribe.objects.create(lang='en', email='test@example.com')

    def test_email_content(self):
        subscribe = Newsletter_Subscribe.objects.get(id=1)
        expected_email = f'{subscribe.email}'
        self.assertEqual(expected_email, 'test@example.com')

    def test_lang_content(self):
        subscribe = Newsletter_Subscribe.objects.get(id=1)
        expected_lang = f'{subscribe.lang}'
        self.assertEqual(expected_lang, 'en')

    def test_join_at_auto_now_add(self):
        subscribe = Newsletter_Subscribe.objects.get(id=1)
        self.assertIsNotNone(subscribe.join_at)
