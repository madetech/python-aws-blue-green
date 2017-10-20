class MockElbGateway:
    def __init__(self):
        self.instance_ids = ['instanceOne', 'instanceTwo']

    def elb_instance_ids(self, load_balancer_names):
        return {
            'LoadBalancerDescriptions': [{
                'Instances': [
                    {'InstanceId': self.instance_ids[0]},
                    {'InstanceId': self.instance_ids[1]}
                ]}
            ]
        }
