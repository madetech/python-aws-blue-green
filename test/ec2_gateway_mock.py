class MockEC2Gateway:
    def __init__(self):
        self.stopped_instance_ids = []
        self.running_instance_ids = []

    def stop_instances(self, instance_ids):
        self.stopped_instance_ids = instance_ids

    def start_instances(self, instance_ids):
        self.running_instance_ids = instance_ids
