from unittest import TestCase

#import seng
importlib.import_module(seng)


class SengTestCase(TestCase):
    def test_main(self):
        self.assertTrue(seng.main() == seng.SUCCESS)

    def test_another_func(self):
        self.assertTrue(seng.another_func() == seng.SUCCESS)
