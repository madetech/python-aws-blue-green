class ClientMock:
    def __init__(self):
        self.hosted_zones = []
        self.resource_record_sets = []

    def change_resource_record_sets(self, HostedZoneId, ChangeBatch):
        return {
            'ChangeInfo': {
                'Id': '/change/whoooop',
                'Status': 'PENDING',
                'Comment': ChangeBatch['Comment']
            }
        }

    def list_hosted_zones_by_name(self):
        return {'HostedZones': [
            {'Id': '/hosted/other-id-1', 'Name': 'never-used-1.co.uk'},
            {'Id': '/hosted/id', 'Name': 'example.co.uk.'},
            {'Id': '/hosted/other-id-2', 'Name': 'never-used-2.co.uk'},
        ]}

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
