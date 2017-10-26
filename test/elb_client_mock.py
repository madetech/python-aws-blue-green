class ELBClientMock:
    def __init__(self):
        self.load_balancers = {
            'LoadBalancerDescriptions': [{
                'Instances': [
                    {'InstanceId': 'instanceOne'},
                    {'InstanceId': 'instanceTwo'}
                ]}
            ]
        }

    def describe_load_balancers(self, **kwargs):
        return self.load_balancers
