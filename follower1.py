import grpc
from concurrent import futures
import raft_pb2
import raft_pb2_grpc
import csv

class RaftFollower(raft_pb2_grpc.RaftServiceServicer):
    def __init__(self):
        self.logs = []
        self.base_datos = "base_datos_f1.csv"  # Unique file per follower

    def AppendEntries(self, request, context):
        # Append the log entry
        self.logs.append(request)

        # Apply to local CSV file
        with open(self.base_datos, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([request.key, request.value])

        return raft_pb2.AppendResponse(success=True)

    def ReadRequest(self, request, context):
        # Read from the local CSV file
        with open(self.base_datos, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == request.key:
                    return raft_pb2.ReadResponse(value=row[1])

        return raft_pb2.ReadResponse(value="Not Found")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    raft_pb2_grpc.add_RaftServiceServicer_to_server(RaftFollower(), server)
    server.add_insecure_port('[::]:50052')  # Use a different port for each follower
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
