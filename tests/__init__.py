# -*- coding: utf-8 -*-

import unittest
from pythonsearch import PythonSearch
import unidecode
import io

class TestPythonSearch(unittest.TestCase):

    def setUp(self):
        self.ps = PythonSearch('../../resources/stopwords.txt', '../../resources/stopwords_prepare.txt', '../../resources/rules.txt', '../../resources/rules_prepare.txt')
        self.maxDiff = None

    def __test_keys(self, input_file, output_file):
        input = io.open(input_file, encoding='utf-8').read()
        output = io.open(output_file, encoding='utf-8').read()
        self.assertEqual(" ".join(self.ps.get_keys(input)).strip(), output.strip())

    def test_input1(self):
        self.__test_keys("../../test/1_input.txt", "../../test/1_output.txt")
    
    def test_input2(self):
        self.__test_keys("../../test/2_input.txt", "../../test/2_output.txt")
    
    def test_input3(self):
        self.__test_keys("../../test/3_input.txt", "../../test/3_output.txt")
    
    def test_input4(self):
        self.__test_keys("../../test/4_input.txt", "../../test/4_output.txt")

    def test_string1(self):
        self.assertEqual("fung gubbe skyland sluta", " ".join(self.ps.get_keys("skylanders gubbe sluta fungera")).strip())
if __name__ == '__main__':
    unittest.main()
