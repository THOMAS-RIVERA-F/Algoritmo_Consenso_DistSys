import grpc
import raft_pb2
import raft_pb2_grpc

class Proxy:
    def __init__(self):
        self.leader_address = "localhost:50051"
        self.followers = ["localhost:50052", "localhost:50053"]

    def write(self, key, value):
        with grpc.insecure_channel(self.leader_address) as channel:
            stub = raft_pb2_grpc.RaftServiceStub(channel)
            response = stub.WriteRequest(raft_pb2.WriteMessage(key=key, value=value))
            return response.success

    def read(self, key):
        # Round-robin read from followers
        follower_address = self.followers[0]
        with grpc.insecure_channel(follower_address) as channel:
            stub = raft_pb2_grpc.RaftServiceStub(channel)
            response = stub.ReadRequest(raft_pb2.ReadMessage(key=key))
            return response.value

proxy = Proxy()
