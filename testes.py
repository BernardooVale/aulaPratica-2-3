from framework import TestCase, TestResult

class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        pass

    def test_b(self):
        pass

    def test_c(self):
        pass

print("--- Execução da Seção 3 ---")
result = TestResult()

test = MyTest('test_a')
test.run(result)

test = MyTest('test_b')
test.run(result)

test = MyTest('test_c')
test.run(result)

print(result.summary())