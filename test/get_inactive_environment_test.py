from src.gateways.hosted_zone_gateway import HostedZoneGateway
from src.get_inactive_environment import GetInactiveEnvironment
from test.client_mock import ClientMock

class TestGetInactiveEnvironment:
    def test_gets_inactive_environment_correctly(self):
        hosted_zone_gateway = HostedZoneGateway(ClientMock())
        use_case = GetInactiveEnvironment(
            blue='test-blue.example.co.uk',
            green='test-green.example.co.uk',
            target_domain='test.example.co.uk',
            hosted_zone_gateway=hosted_zone_gateway)
        assert use_case.call() == 'test-blue.example.co.uk'
