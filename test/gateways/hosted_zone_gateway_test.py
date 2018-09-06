from src.gateways.hosted_zone_gateway import HostedZoneGateway
from test.client_mock import ClientMock


class TestHostedZoneGateway:
    def test_correct_zone_is_found(self):
        client = ClientMock()
        hosted_zone_gateway = HostedZoneGateway(client)

        assert hosted_zone_gateway.get_hosted_zone('test-blue.example.co.uk.') == {
            'Id': '/hosted/id', 'Name': 'example.co.uk.'
        }

    def test_correct_zone_records_found(self):
        client = ClientMock()
        hosted_zone_gateway = HostedZoneGateway(client)

        assert hosted_zone_gateway.get_hosted_zone_records('test-blue.example.co.uk.') == [
            {
                'Name': 'test-blue.example.co.uk.',
                'Type': 'A',
                'AliasTarget': {
                    'HostedZoneId': 'Seb',
                    'DNSName': 'super-elastic-load-balancer.example.co.uk.',
                    'EvaluateTargetHealth': False
                }
            },
            {
                'Name': 'test-green.example.co.uk.',
                'Type': 'A',
                'AliasTarget': {
                    'HostedZoneId': 'Dan',
                    'DNSName': 'super-elastic-load-balancer.example.co.uk.',
                    'EvaluateTargetHealth': False
                }
            },
            {
                'Name': 'test.example.co.uk.',
                'Type': 'A',
                'AliasTarget': {
                    'HostedZoneId': 'Dan-and-Seb',
                    'DNSName': 'test-green.example.co.uk.',
                    'EvaluateTargetHealth': False
                }
            }]