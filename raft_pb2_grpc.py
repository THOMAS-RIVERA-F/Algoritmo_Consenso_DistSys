# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import raft_pb2 as raft__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in raft_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class RaftServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WriteRequest = channel.unary_unary(
                '/RaftService/WriteRequest',
                request_serializer=raft__pb2.WriteMessage.SerializeToString,
                response_deserializer=raft__pb2.WriteResponse.FromString,
                _registered_method=True)
        self.ReadRequest = channel.unary_unary(
                '/RaftService/ReadRequest',
                request_serializer=raft__pb2.ReadMessage.SerializeToString,
                response_deserializer=raft__pb2.ReadResponse.FromString,
                _registered_method=True)
        self.AppendEntries = channel.unary_unary(
                '/RaftService/AppendEntries',
                request_serializer=raft__pb2.LogEntry.SerializeToString,
                response_deserializer=raft__pb2.AppendResponse.FromString,
                _registered_method=True)


class RaftServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WriteRequest(self, request, context):
        """Líder recibe solicitudes del proxy para escribir en la base de datos
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadRequest(self, request, context):
        """Followers responden a las lecturas
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppendEntries(self, request, context):
        """Líder replica los logs a los followers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RaftServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WriteRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteRequest,
                    request_deserializer=raft__pb2.WriteMessage.FromString,
                    response_serializer=raft__pb2.WriteResponse.SerializeToString,
            ),
            'ReadRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadRequest,
                    request_deserializer=raft__pb2.ReadMessage.FromString,
                    response_serializer=raft__pb2.ReadResponse.SerializeToString,
            ),
            'AppendEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.AppendEntries,
                    request_deserializer=raft__pb2.LogEntry.FromString,
                    response_serializer=raft__pb2.AppendResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RaftService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('RaftService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RaftService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WriteRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftService/WriteRequest',
            raft__pb2.WriteMessage.SerializeToString,
            raft__pb2.WriteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReadRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftService/ReadRequest',
            raft__pb2.ReadMessage.SerializeToString,
            raft__pb2.ReadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AppendEntries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftService/AppendEntries',
            raft__pb2.LogEntry.SerializeToString,
            raft__pb2.AppendResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
