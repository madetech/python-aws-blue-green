class ELBGateway:
    def __init__(self, client):
        self.client = client

    def elb_instance_ids(self, load_balancer_names):
        return self.client.describe_load_balancers(
            LoadBalancerNames=load_balancer_names
        )
