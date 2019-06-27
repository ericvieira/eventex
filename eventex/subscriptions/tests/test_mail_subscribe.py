from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name="Eric Vieira", cpf="12345678901",
                    email="eric.vieira@me.com", phone="21-99889-3320")
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'eric.vieira@me.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Eric Vieira',
            '12345678901',
            'eric.vieira@me.com',
            '21-99889-3320',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

        self.assertIn('Eric Vieira', self.email.body)
        self.assertIn('12345678901', self.email.body)
        self.assertIn('eric.vieira@me.com', self.email.body)
        self.assertIn('21-99889-3320', self.email.body)
