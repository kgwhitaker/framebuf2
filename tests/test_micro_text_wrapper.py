import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import micro_text_wrapper

class MicroTextWrapperTestSuite(unittest.TestCase):
    """
    Tests for MicroTextWrapper class
    """

    def test_find_word_break(self):
        """
        make sure we can walk backwards in a sentence to find the last word brake position
        """
        test_string = "oneword"
        line_len = 10
        wrapper = micro_text_wrapper.MicroTextWrapper()
        word_end = wrapper._find_word_break(test_string)
        self.assertEqual(word_end,7)

        test_string = "two words"
        word_end = wrapper._find_word_break(test_string)
        self.assertEqual(word_end, 3)
        self.assertEqual("two",test_string[0:word_end])

    def test_word_wrap_small(self):
        """
        Make sure that a small sentence is just wrapped.
        """
        test_string = "my little pony"
        line_len = 40
        wrapper = micro_text_wrapper.MicroTextWrapper()
        lines = wrapper.wrap_text(test_string, line_len)
        self.assertEqual(len(lines),1)
        self.assertEqual(lines[0],test_string)

    def test_word_wrap_word_delimiter(self):
        """
        test wrapping text where the wrap point is a word delimiter
        """
        test_string = "my little pony"
        line_len = 9
        wrapper = micro_text_wrapper.MicroTextWrapper()
        lines = wrapper.wrap_text(test_string, line_len)
        self.assertEqual(len(lines),2)
        self.assertEqual(lines[0],"my little")
        self.assertEqual(lines[1],"pony")

    def test_word_wrap_word_hyphen(self):
        """
        test the need to force in a hyphen
        """
        test_string = "my little pony has a verylongnamethaticannotpronounce"

        line_len = 9
        wrapper = micro_text_wrapper.MicroTextWrapper()
        lines = wrapper.wrap_text(test_string, line_len)
        self.assertEqual(len(lines), 7)
        self.assertEqual(lines[0],"my little")
        self.assertEqual(lines[1],"pony has")
        self.assertEqual(lines[2],"a")
        self.assertEqual(lines[3],"verylong-")
        self.assertEqual(lines[4],"namethat-")
        self.assertEqual(lines[5],"icannotp-")
        self.assertEqual(lines[6],"ronounce")

    def test_word_wrap_word_multiline(self):
        """
        test a multi line sentence with word breaks.
        """
        test_string = "my little pony has a very long name that I cannot pronounce"
        line_len = 9
        wrapper = micro_text_wrapper.MicroTextWrapper()
        lines = wrapper.wrap_text(test_string, line_len)
        self.assertEqual(len(lines), 7)
        self.assertEqual(lines[0],"my little")
        self.assertEqual(lines[1],"pony has")
        self.assertEqual(lines[2],"a very")
        self.assertEqual(lines[3],"long name")
        self.assertEqual(lines[4],"that I")
        self.assertEqual(lines[5],"cannot")
        self.assertEqual(lines[6],"pronounce")


    def test_word_wrap_all_word_delims(self):
        """
        Test that makes use of all the word delimiters.
        """
        test_string = "my-little\tpony has a very;long name-that! I cannot.pronounce"
        line_len = 9
        wrapper = micro_text_wrapper.MicroTextWrapper()
        lines = wrapper.wrap_text(test_string, line_len)
        self.assertEqual(len(lines), 8)
        self.assertEqual(lines[0],"my-little")
        self.assertEqual(lines[1],"pony has")
        self.assertEqual(lines[2],"a very;")
        self.assertEqual(lines[3],"long")
        self.assertEqual(lines[4],"name-")
        self.assertEqual(lines[5],"that! I")
        self.assertEqual(lines[6],"cannot.")
        self.assertEqual(lines[7],"pronounce")

    def test_word_wrap_blank_lines(self):
        """
        Validates that blank lines in the string are respected in the wrapped output.
        """
        test_string = """Captain's log, stardate unknown... I've managed to dig up a purr-fectly dreadful joke from Pirate, the feline humorist.

Why did the cat join a band?

Because it wanted to be the purr-cussionist!

I hope that one struck a chord with you! (Sorry, had to - Pirate's jokes can be a bit of a cat-astrophe...)"""
        line_len = 50
        wrapper = micro_text_wrapper.MicroTextWrapper()
        lines = wrapper.wrap_text(test_string, line_len)
        self.assertEqual(len(lines), 11)
        self.assertEqual(lines[0],"Captain's log, stardate unknown... I've managed to")
        self.assertEqual(lines[1],"dig up a purr-fectly dreadful joke from Pirate,")
        self.assertEqual(lines[2],"the feline humorist.")
        self.assertEqual(lines[3],"")
        self.assertEqual(lines[4],"Why did the cat join a band?")
        self.assertEqual(lines[5],"")
        self.assertEqual(lines[6],"Because it wanted to be the purr-cussionist!")
        self.assertEqual(lines[7],"")
        self.assertEqual(lines[8],"I hope that one struck a chord with you! (Sorry,")
        self.assertEqual(lines[9],"had to - Pirate's jokes can be a bit of a cat-")
        self.assertEqual(lines[10],"astrophe...)")








        # for line in lines:
            # test_str = str(len(line)) + "=" + line
            # print(test_str)
            # if "\r" in test_str: print("*CR*")
            # if "\n" in test_str: print("*LF*" + str(test_str.find('\n')))




    
