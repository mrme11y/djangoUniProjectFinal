from djangoUniProjectFinal.wsgi import *

import unittest
from unittest import TestCase

import os

from helpdesk.models import Ticket
from django.core.exceptions import ValidationError

if __name__ == '__main__':
    unittest.main()


class TicketTestCases(unittest.TestCase):
    def test_valid_phone_number(self):
        # Create an instance of ticket model with a valid phone number
        obj = Ticket()
        obj.phone = '1234567890'

        # Ensure the phone number is saved successfully
        self.assertEqual(obj.phone, '1234567890')

    def test_invalid_phone_number(self):
        # Create an instance of ticket model with an invalid phone number and raises a ValueError
        with self.assertRaises(ValueError):
            Ticket.objects.create(phone='+ft1234567890')

    def test_valid_email(self):
        # Create an instance of ticket model with a valid phone number
        obj = Ticket()
        obj.email = 'email@email.com'

        # Ensure the email is saved successfully
        self.assertEqual(obj.email, 'email@email.com')