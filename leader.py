import grpc
from concurrent import futures
import raft_pb2
import raft_pb2_grpc
import csv

class RaftLeader(raft_pb2_grpc.RaftServiceServicer):
    def __init__(self):
        self.logs = []
        self.current_term = 0
        self.followers = ["localhost:50052", "localhost:50053"]  # Followers' addresses

    def WriteRequest(self, request, context):
        # Write to the log
        self.current_term += 1
        log_entry = raft_pb2.LogEntry(term=self.current_term, key=request.key, value=request.value)
        self.logs.append(log_entry)

        # Replicate to followers
        for follower in self.followers:
            with grpc.insecure_channel(follower) as channel:
                stub = raft_pb2_grpc.RaftServiceStub(channel)
                response = stub.AppendEntries(log_entry)

                if not response.success:
                    return raft_pb2.WriteResponse(success=False)

        # Append the entry to the local CSV file
        with open('base_datos.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([request.key, request.value])

        return raft_pb2.WriteResponse(success=True)

    def AppendEntries(self, request, context):
        # Replication logic for followers
        return raft_pb2.AppendResponse(success=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    raft_pb2_grpc.add_RaftServiceServicer_to_server(RaftLeader(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
