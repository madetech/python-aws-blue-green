from os.path import commonprefix


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

        # we need to find the zone that matches our target domain
        # we do this by reversing the domains, and checking to see if there's a common prefix
        zone_id = None
        reversed_target_domain = ''.join(reversed(self.target_domain))
        for zone in zones['HostedZones']:
            reversed_hosted_zone_name = ''.join(reversed(zone['Name']))
            common_name = commonprefix((reversed_hosted_zone_name, reversed_target_domain))
            if len(common_name) == len(reversed_hosted_zone_name):
                zone_id = zone['Id']
                break
        else:
            raise ValueError('Could not find hosted zone for target domain: {}'.format(self.target_domain))

        return self.client.list_resource_record_sets(HostedZoneId=zone_id)['ResourceRecordSets']

    def get_live_record(self):
        resource_records = self.get_resource_record_sets()
        records = next(
            record for record in resource_records if record['Name'] == self.target_domain
        )
        return records['AliasTarget']['DNSName']

    def call(self):
        return self.get_live_record()[:-1]
