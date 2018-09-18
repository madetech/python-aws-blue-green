class MockEC2Gateway:
    def __init__(self):
        self.stopped_instance_ids = []
        self.running_instance_ids = []
        self.waiting_for_running_instance_ids = []

    def stop_instances(self, instance_ids):
        self.stopped_instance_ids = instance_ids

    def start_instances(self, instance_ids):
        self.running_instance_ids = instance_ids

    def wait_for_instances_running(self, instance_ids):
        self.waiting_for_running_instance_ids = instance_ids
