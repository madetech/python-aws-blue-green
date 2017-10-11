class GetCurrentLiveEnvironment:
    def __init__(self, target_domain, client):
        self.target_domain = self.sanitize_target_domain(target_domain)
        self.client = client

    def sanitize_target_domain(self, domain):
        domain = domain.strip()
        if domain[-1] != '.':
            domain += '.'
        return domain


    def get_resource_record_sets(self):
        zones = self.client.list_hosted_zones_by_name()
        zone_id = zones['HostedZones'][0]['Id']
        return self.client.list_resource_record_sets(HostedZoneId=zone_id)['ResourceRecordSets']

    def get_live_record(self):
        resource_records = self.get_resource_record_sets()
        records = next(
            record for record in resource_records if record['Name'] == self.target_domain
        )
        return records['AliasTarget']['DNSName']

    def call(self):
        return self.get_live_record()[:-1]
