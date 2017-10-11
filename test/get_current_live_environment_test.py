from src.get_current_live_environment import GetCurrentLiveEnvironment


class ClientMock:
    def __init__(self):
        self.hosted_zones = []
        self.resource_record_sets = []

    def list_hosted_zones_by_name(self):
        return {'HostedZones': [{'Id': '/hosted/id', 'Name': 'example.co.uk.'}]}

    def list_resource_record_sets(self, HostedZoneId):
        return {'ResourceRecordSets': [
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
            }]}


class TestGetCurrentLiveEnvironment:
    def test_gets_current_live_environment_correctly(self):
        use_case = GetCurrentLiveEnvironment(
            target_domain='test.example.co.uk', client=ClientMock())
        assert use_case.call() == 'test-green.example.co.uk'

    def test_gets_current_live_environment_correctly_when_given_fullstop(self):
        use_case = GetCurrentLiveEnvironment(
            target_domain='test.example.co.uk.', client=ClientMock())
        assert use_case.call() == 'test-green.example.co.uk'
