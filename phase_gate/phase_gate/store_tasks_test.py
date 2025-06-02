import store_tasks
import unittest
from unittest import TestCase

client_info = []

class TestStoreTask(TestCase):

    def StoreSetUp(self):
        client_info = [("fish"["task"], "Get foodStuff" ".", "2. View tasks")]

    def test_to_add_task(self):
        actual = store_tasks.that_add_task("egg")
        expected_output = "egg"
        self.assertEqual(actual, expected_output)

    def test_to_view_task(self):
        actual = store_tasks.that_view_all_task("")
        expected_output = ""
        self.assertEqual(actual, expected_output)


    
