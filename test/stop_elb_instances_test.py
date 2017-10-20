from src.stop_elb_instances import StopELBInstances
from test.elb_gateway_mock import MockElbGateway
from test.ec2_gateway_mock import MockEC2Gateway

class TestStopELBInstances:
    def test_stops_instances_for_load_balancer(self):
        elb_gateway = MockElbGateway()
        ec2_gateway = MockEC2Gateway()
        use_case = StopELBInstances(
            elb_gateway=elb_gateway,
            ec2_gateway=ec2_gateway
        )
        use_case.call('foo')

        assert elb_gateway.instance_ids == ec2_gateway.stopped_instance_ids
