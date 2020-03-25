import io
import sys
import unittest

from test.update_readme import update_readme


class MyTestCase(unittest.TestCase):
    manually_test_method = ['process_pool']
    words_result = ['Life is short', 'Life is short ', 'Life is short\n', 'life is short\n', 'life is short ']

    def setUp(self):
        self.stdout, sys.stdout = sys.stdout, io.StringIO()
        self.msg_buffer = ""

    def tearDown(self):
        sys.stdout = self.stdout
        print(self.msg_buffer)

        self.msg_buffer = ""

    @staticmethod
    def get_StringIO():
        string = str(sys.stdout.getvalue())
        sys.stdout.seek(0)
        sys.stdout.truncate()
        return string

    def test_a(self):
        from LifeIsShort.a import __all__ as method_list

        for method in method_list:
            exec(f'from LifeIsShort.a import {method}')
            self.assertIn(self.get_StringIO(), self.words_result, msg=method)

    def test_b(self):
        from LifeIsShort.b import __all__ as method_list

        for method in method_list:
            exec(f'from LifeIsShort.b import {method}')
            self.assertIn(self.get_StringIO(), self.words_result, msg=method)

    def test_c(self):
        from LifeIsShort.c import __all__ as method_list

        for method in method_list:
            exec(f'from LifeIsShort.c import {method}')
            self.assertIn(self.get_StringIO(), self.words_result, msg=method)

    def test_d(self):
        from LifeIsShort.d import __all__ as method_list

        for method in method_list:
            if method in self.manually_test_method:
                self.msg_buffer += f"Since sys.stdout sometimes cannot be captured, {method} needs to be tested manually.\n"
                continue
            for _ in range(10):
                exec(f'from LifeIsShort.d import {method}')
                eval(method).main()
                self.assertIn(self.get_StringIO(), self.words_result, msg=method)


if __name__ == '__main__':
    unittest.main()
    update_readme()
