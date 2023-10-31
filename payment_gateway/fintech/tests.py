from django.test import TestCase

# Create your tests here.
import unittest
from django.test import RequestFactory
from fintech.views import payment
from fintech.models import PaymentRecord  

class PaymentTestCase(unittest.TestCase):

    def setUp(self):
        # Create a request object for testing
        self.factory = RequestFactory()

    def test_payment_success(self):
        # Create a mock request
        request = self.factory.get('/payment')

        # Calling the payment function with the mock request
        response = payment(request)

        # Checking the response status code
        self.assertEqual(response.status_code, 200)

    def test_payment_record_saved(self):
        # Creating a mock request
        request = self.factory.get('/payment')

        # Calling the payment function with the mock request
        response = payment(request)

        # Checking whether PaymentRecord was created in the database
        payment_record = PaymentRecord.objects.last()  
        self.assertIsNotNone(payment_record)
        self.assertEqual(payment_record.status, 'created')  

if __name__ == '__main__':
    unittest.main()
