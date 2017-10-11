class GetInactiveEnvironment:
    def __init__(self, blue, green, target_domain, client):
        self.target_domain = self.sanitize_domain(target_domain)
        self.blue = self.sanitize_domain(blue)
        self.green = self.sanitize_domain(green)
        self.client = client

    def sanitize_domain(self, domain):
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

    def get_inactive_record(self):
        live_domain = self.get_live_record()

        if live_domain == self.green:
            return self.blue
        elif live_domain == self.blue:
            return self.green

    def call(self):
        return self.get_inactive_record()[:-1]
