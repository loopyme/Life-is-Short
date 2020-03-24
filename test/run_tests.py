import io
import sys
import unittest

from Word import words_result


def stub_stdout(testcase_inst):
    def cleanup():
        sys.stderr, sys.stdout = stderr, stdout

    testcase_inst.addCleanup(cleanup)
    stderr, sys.stderr = sys.stderr, io.StringIO()
    stdout, sys.stdout = sys.stdout, io.StringIO()


class MyTestCase(unittest.TestCase):

    def test_a(self):
        from LifeIsShort.a import __all__ as method_list

        for method in method_list:
            stub_stdout(self)
            exec(f'from LifeIsShort.a import {method}')
            eval(method).main()
            self.assertIn(str(sys.stdout.getvalue()), words_result)

    def test_b(self):
        from LifeIsShort.b import __all__ as method_list

        for method in method_list:
            stub_stdout(self)
            exec(f'from LifeIsShort.b import {method}')
            eval(method).main()
            self.assertIn(str(sys.stdout.getvalue()), words_result)

    def test_c(self):
        from LifeIsShort.c import __all__ as method_list

        for method in method_list:
            stub_stdout(self)
            exec(f'from LifeIsShort.c import {method}')
            eval(method).main()
            self.assertIn(str(sys.stdout.getvalue()), words_result)

    def test_d(self):
        from LifeIsShort.d import __all__ as method_list

        for method in method_list:
            stub_stdout(self)
            exec(f'from LifeIsShort.d import {method}')
            eval(method).main()
            self.assertIn(str(sys.stdout.getvalue()), words_result)


if __name__ == '__main__':
    unittest.main()
