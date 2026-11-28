"""Shipping notifications."""

SUBJECTS = {"en": "Your order has shipped", "de": "Ihre Bestellung wurde versandt"}


def shipping_email(order, customer):
    subject = SUBJECTS.get(customer.locale, SUBJECTS["en"])
    body = f"Hi {customer.name}, order {order['id']} is on its way. Tracking: {order['tracking']}"
    return customer.email, subject, body


def notify(order, customer, mailer):
    """Send the shipping email. Raises if the mailer fails, so the job queue retries the job."""
    to, subject, body = shipping_email(order, customer)
    mailer.send(to, subject, body)
