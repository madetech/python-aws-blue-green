from src.get_inactive_environment import GetInactiveEnvironment
from client_mock import ClientMock

class TestGetInactiveEnvironment:
    def test_gets_inactive_environment_correctly(self):
        use_case = GetInactiveEnvironment(
            blue='test-blue.example.co.uk',
            green='test-green.example.co.uk',
            target_domain='test.example.co.uk', client=ClientMock())
        assert use_case.call() == 'test-blue.example.co.uk'
