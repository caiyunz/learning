#!/usr/bin/python3
import employee  
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.first='caiyun'
        self.last='zhao'
        self.salary=1000
        self.employee_tester=employee.Employee(self.first,self.last,self.salary)
        self.add=3000
    def test_give_default_rasie(self):
        self.salary=self.employee_tester.give_raise()
        self.assertEqual(self.salary,6000)

    def test_give_custom_rasie(self):
        self.salary=self.employee_tester.give_raise(self.add)
        self.assertEqual(self.salary,4000)

unittest.main()
