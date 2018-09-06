from src.gateways.hosted_zone_gateway import HostedZoneGateway
from src.get_current_live_environment import GetCurrentLiveEnvironment
from test.client_mock import ClientMock

class TestGetCurrentLiveEnvironment:
    def test_gets_current_live_environment_correctly(self):
        hosted_zone_gateway = HostedZoneGateway(ClientMock())
        use_case = GetCurrentLiveEnvironment(
            target_domain='test.example.co.uk', hosted_zone_gateway=hosted_zone_gateway)
        assert use_case.call() == 'test-green.example.co.uk'

    def test_gets_current_live_environment_correctly_when_given_fullstop(self):
        hosted_zone_gateway = HostedZoneGateway(ClientMock())
        use_case = GetCurrentLiveEnvironment(
            target_domain='test.example.co.uk.', hosted_zone_gateway=hosted_zone_gateway)
        assert use_case.call() == 'test-green.example.co.uk'
