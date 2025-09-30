from framework import TestResult, TestCase, TestStub, TestSpy

class TestCaseTest(TestCase):

    def set_up(self):
        self.result = TestResult()

    def test_result_success_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        assert self.result.summary() == '1 run, 0 failed, 0 error'

    def test_result_failure_run(self):
        stub = TestStub('test_failure')
        stub.run(self.result)
        assert self.result.summary() == '1 run, 1 failed, 0 error'

    def test_result_error_run(self):
        stub = TestStub('test_error')
        stub.run(self.result)
        assert self.result.summary() == '1 run, 0 failed, 1 error'

    def test_result_multiple_run(self):
        stub_success = TestStub('test_success')
        stub_success.run(self.result)
        stub_failure = TestStub('test_failure')
        stub_failure.run(self.result)
        stub_error = TestStub('test_error')
        stub_error.run(self.result)
        assert self.result.summary() == '3 run, 1 failed, 1 error'

    def test_was_set_up(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_set_up

    def test_was_run(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_run

    def test_was_tear_down(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_tear_down

    def test_template_method(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.log == "set_up test_method tear_down"

print("--- Execução da Seção 4 ---")

result = TestResult()

TestCaseTest('test_result_success_run').run(result)
TestCaseTest('test_result_failure_run').run(result)
TestCaseTest('test_result_error_run').run(result)
TestCaseTest('test_result_multiple_run').run(result)

TestCaseTest('test_was_set_up').run(result)
TestCaseTest('test_was_run').run(result)
TestCaseTest('test_was_tear_down').run(result)
TestCaseTest('test_template_method').run(result)

print(result.summary())