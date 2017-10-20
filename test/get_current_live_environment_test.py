from src.get_current_live_environment import GetCurrentLiveEnvironment
from test.client_mock import ClientMock

class TestGetCurrentLiveEnvironment:
    def test_gets_current_live_environment_correctly(self):
        use_case = GetCurrentLiveEnvironment(
            target_domain='test.example.co.uk', client=ClientMock())
        assert use_case.call() == 'test-green.example.co.uk'

    def test_gets_current_live_environment_correctly_when_given_fullstop(self):
        use_case = GetCurrentLiveEnvironment(
            target_domain='test.example.co.uk.', client=ClientMock())
        assert use_case.call() == 'test-green.example.co.uk'
