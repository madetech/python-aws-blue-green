from src.gateways.elb_gateway import ELBGateway
from test.elb_client_mock import ELBClientMock

class TestELBGateway:
    def test_returns_instance_ids_from_elb_client(self):
        client = ELBClientMock()
        gateway = ELBGateway(client=client)
        assert gateway.elb_instance_ids(['foo']) == client.load_balancers
