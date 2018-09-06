from os.path import commonprefix


class GetCurrentLiveEnvironment:
    def __init__(self, target_domain, hosted_zone_gateway):
        self.target_domain = self.sanitize_target_domain(target_domain)
        self.hosted_zone_gateway = hosted_zone_gateway

    def sanitize_target_domain(self, domain):
        domain = domain.strip()
        if domain[-1] != '.':
            domain += '.'
        return domain

    def get_resource_record_sets(self):
        return self.hosted_zone_gateway.get_hosted_zone_records(self.target_domain)

    def get_live_record(self):
        resource_records = self.get_resource_record_sets()
        records = next(
            record for record in resource_records if record['Name'] == self.target_domain
        )
        return records['AliasTarget']['DNSName']

    def call(self):
        return self.get_live_record()[:-1]
