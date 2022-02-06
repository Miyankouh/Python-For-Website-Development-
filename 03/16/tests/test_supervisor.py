import unittest
from models import Supervisor


class SupervisorTestCase(unittest.TestCase):
    """ 
    Check Supervisor class attributes methods
    """

    def test_all_data(self):
        instance = Supervisor.sample()
        self.assertIsInstance(instance, Supervisor)
        # assert instance(instance, Supervisor), "sample dose not return proper instance"
        self.assertTrue(hasattr(instance, "username"))
        self.assertTrue(hasattr(instance, "password"))
        self.assertTrue(hasattr(instance, "phone_number"))