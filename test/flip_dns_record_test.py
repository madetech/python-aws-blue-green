from src.gateways.hosted_zone_gateway import HostedZoneGateway
from test.client_mock import ClientMock
from src.flip_dns_record import FlipDNSRecord


class TestFlipDNSRecord:
    def test_gets_correct_non_live_resource_record(self):
        client = ClientMock()
        hosted_zone_gateway = HostedZoneGateway(client)
        usecase = FlipDNSRecord(
            client=client,
            hosted_zone_gateway=hosted_zone_gateway,
            live='test-green.example.co.uk',
            green='test-green.example.co.uk',
            blue='test-blue.example.co.uk',
            target_domain='test.example.co.uk'
        )

        assert usecase.get_non_live_resource() == 'test-blue.example.co.uk.'

    def test_change_resource_dict(self):
        client = ClientMock()
        hosted_zone_gateway = HostedZoneGateway(client)
        usecase = FlipDNSRecord(
            client=client,
            hosted_zone_gateway=hosted_zone_gateway,
            live='test-green.example.co.uk',
            green='test-green.example.co.uk',
            blue='test-blue.example.co.uk',
            target_domain='test.example.co.uk'
        )

        expected_dict = {
            'Name': 'test.example.co.uk.',
            'Type': 'A',
            'AliasTarget': {
                'HostedZoneId': 'Dan-and-Seb',
                'DNSName': 'test-blue.example.co.uk.',
                'EvaluateTargetHealth': False
            }
        }

        assert usecase.build_resource_dict() == expected_dict

    def test_change_dict(self):
        client = ClientMock()
        hosted_zone_gateway = HostedZoneGateway(client)
        usecase = FlipDNSRecord(
            client=client,
            hosted_zone_gateway=hosted_zone_gateway,
            live='test-green.example.co.uk',
            green='test-green.example.co.uk',
            blue='test-blue.example.co.uk',
            target_domain='test.example.co.uk'
        )

        expected_dict = {
            'HostedZoneId': '/hosted/id',
            'ChangeBatch': {
                'Comment': 'Flipping live to test-blue.example.co.uk.',
                'Changes': [{
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': 'test.example.co.uk.',
                        'Type': 'A',
                        'AliasTarget': {
                            'HostedZoneId': 'Dan-and-Seb',
                            'DNSName': 'test-blue.example.co.uk.',
                            'EvaluateTargetHealth': False
                        }
                    }
                }]
            }
        }

        assert usecase.build_change_dict() == expected_dict

    def test_end_to_end(self):
        client = ClientMock()
        hosted_zone_gateway = HostedZoneGateway(client)
        usecase = FlipDNSRecord(
            client=client,
            hosted_zone_gateway=hosted_zone_gateway,
            live='test-green.example.co.uk',
            green='test-green.example.co.uk',
            blue='test-blue.example.co.uk',
            target_domain='test.example.co.uk'
        )

        assert usecase.call()['ChangeInfo']['Comment'] == 'Flipping live to test-blue.example.co.uk.'
