from src.start_elb_instances import StartELBInstances
from test.elb_gateway_mock import MockElbGateway
from test.ec2_gateway_mock import MockEC2Gateway

class TestStartELBInstances:
    def test_start_instances_for_load_balancer(self):
        elb_gateway = MockElbGateway()
        ec2_gateway = MockEC2Gateway()
        use_case = StartELBInstances(
            elb_gateway=elb_gateway,
            ec2_gateway=ec2_gateway
        )
        use_case.call('foo')

        assert elb_gateway.instance_ids == ec2_gateway.running_instance_ids
