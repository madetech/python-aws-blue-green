class StopELBInstances:
    def __init__(self, elb_gateway, ec2_gateway):
        self.elb_gateway = elb_gateway
        self.ec2_gateway = ec2_gateway

    def call(self, elb_name):
        elb_descriptions = self.elb_gateway.elb_instance_ids([elb_name])
        instanceIds = self.__extract_instance_ids(elb_descriptions)
        self.ec2_gateway.stop_instances(instanceIds)

    # private

    def __extract_instance_ids(self, elb_descriptions):
        return [instance['InstanceId'] for instance in elb_descriptions['LoadBalancerDescriptions'][0]['Instances']]
