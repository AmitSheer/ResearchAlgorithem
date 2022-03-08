import unittest
import doc_to_html
from question2 import lastcall


@lastcall
def kkk(num: int):
    return num * 4


class Tests(unittest.TestCase):

    def test_check_doc_to_html(self):
        doc_to_html.in_script_name = "module_example"
        doc_to_html.out_script_name = "py_to_html_out.html"
        doc_to_html.to_html()
        with open(doc_to_html.out_script_name, 'r') as file:
            output = file.read().replace(" ", "")
        with open("expected.html", 'r') as file:
            expected = file.read().replace(" ", "")
        self.assertEqual(expected, output)

    def test_check_question2(self):
        self.assertEqual(4, kkk(1))
        self.assertEqual("value already calculated:4", kkk(1))
        self.assertEqual(8, kkk(2))
        self.assertEqual("value already calculated:4", kkk(1))
        self.assertEqual("value already calculated:8", kkk(2))

