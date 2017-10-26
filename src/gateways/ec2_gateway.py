import boto3

class EC2Gateway:
    def __init__(self, ec2_resource):
        self.ec2_resource = ec2_resource

    def stop_instances(self, instance_ids):
        for instance_id in instance_ids:
            instance = self.ec2_resource.Instance(instance_id)
            instance.stop()

    def start_instances(self, instance_ids):
        for instance_id in instance_ids:
            instance = self.ec2_resource.Instance(instance_id)
            instance.start()
