from unittest import TestCase
import controller


class TestController(TestCase):
    def test_check_bound(self):
        c = controller.Controller()
        self.assertEqual(c.check_bound([-10, 0]), True)
        self.assertEqual(c.check_bound([700, 0]), True)
        self.assertEqual(c.check_bound([0, 0]), False)


