from os.path import commonprefix


class HostedZoneGateway:
    def __init__(self, client):
        self.client = client

    def get_hosted_zone(self, target_domain):
        target_domain = self._sanitize_domain(target_domain)
        zones = self.client.list_hosted_zones_by_name()
        for zone in zones['HostedZones']:
            if self._hosted_zone_matches_domain(zone, target_domain):
                return zone

        raise ValueError('Could not find hosted zone for target domain: {}'.format(target_domain))

    def get_hosted_zone_records(self, target_domain):
        zone = self.get_hosted_zone(target_domain)
        return self.client.list_resource_record_sets(HostedZoneId=zone['Id'])['ResourceRecordSets']

    def _sanitize_domain(self, domain):
            domain = domain.strip()
            if domain[-1] != '.':
                domain += '.'
            return domain

    def _hosted_zone_matches_domain(self, zone, domain):
        reversed_domain = ''.join(reversed(domain))
        reversed_hosted_zone_name = ''.join(reversed(zone['Name']))
        common_name = commonprefix((reversed_hosted_zone_name, reversed_domain))
        return len(common_name) == len(reversed_hosted_zone_name)
