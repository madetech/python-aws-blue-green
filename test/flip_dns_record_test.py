from client_mock import ClientMock
from src.flip_dns_record import FlipDNSRecord


class TestFlipDNSRecord:
    def test_gets_correct_non_live_resource_record(self):
        usecase = FlipDNSRecord(
            client=ClientMock(),
            live='test-green.example.co.uk',
            green='test-green.example.co.uk',
            blue='test-blue.example.co.uk',
            target_domain='test.example.co.uk'
        )

        assert usecase.get_non_live_resource() == 'test-blue.example.co.uk.'

    def test_change_resource_dict(self):
        usecase = FlipDNSRecord(
            client=ClientMock(),
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

        assert usecase.build_resource_struct() == expected_dict
