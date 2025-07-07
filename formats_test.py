import unittest
from formats import generate_emails

class Test(unittest.TestCase):
    def test1(self):
        names = """Max Mustermann
        John Doe
        Toller Name"""
        format = "first.last"
        domain = "example.com"
        self.assertEqual(generate_emails(names, format, domain), "max.mustermann@example.com\njohn.doe@example.com\ntoller.name@example.com\n")
    def test2(self):
        name = "Max Mustermann\nJohn DOe\nToller Name"
        format = "f.last"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "m.mustermann@example.com\nj.doe@example.com\nt.name@example.com\n")
    def test3(self):
        name = "Max Mustermann\nJohn Doe\nTOLLER Name"
        format = "l.first"
        domain = "example.com"
        self.assertEqual(generate_emails(name, format, domain), "m.max@example.com\nd.john@example.com\nn.toller@example.com\n")








if __name__ == "__main__":
    unittest.main()