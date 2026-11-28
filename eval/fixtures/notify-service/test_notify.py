import unittest

from customers import Customer
from jobs import handle
from notify import shipping_email


class FakeMailer:
    def __init__(self):
        self.sent = []

    def send(self, to, subject, body):
        self.sent.append((to, subject, body))


class NotifyTest(unittest.TestCase):
    def test_german_subject(self):
        to, subject, _ = shipping_email({"id": 7, "tracking": "T1"}, Customer(1, "Ana", "ana@example.com", "de"))
        self.assertEqual((to, subject), ("ana@example.com", "Ihre Bestellung wurde versandt"))

    def test_handle_sends_one_email(self):
        mailer = FakeMailer()
        job = {"type": "order_shipped", "order": {"id": 7, "tracking": "T1"},
               "customer": {"id": 1, "name": "Ana", "email": "ana@example.com"}}
        handle(job, mailer)
        self.assertEqual(len(mailer.sent), 1)


if __name__ == "__main__":
    unittest.main()
