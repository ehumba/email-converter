import unittest
from formats import generate_emails

class Test(unittest.TestCase):
    def test1(self):
        name = "Max Mustermann"
        format = "first.last"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "max.mustermann@example.com")
    def test2(self):
        name = "Max Mustermann"
        format = "f.last"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "m.mustermann@example.com")
    def test3(self):
        name = "Max Mustermann"
        format = "first_last"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "max_mustermann@example.com")
    def test4(self):
        name = "Max Mustermann"
        format = "first.l"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "max.m@example.com")
    def test5(self):
        name = "Max Mustermann"
        format = "last.first"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "mustermann.max@example.com")
    def test6(self):
        name = "Max Mustermann"
        format = "l.first"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "m.max@example.com")
    def test7(self):
        name = "Max Mustermann"
        format = "flast"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "mmustermann@example.com")







if __name__ == "__main__":
    unittest.main()