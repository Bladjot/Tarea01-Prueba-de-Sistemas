import grpc

import distance_unary_pb2 as distance__unary__pb2


class DistanceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.geodesic_distance = channel.unary_unary(
                '/DistanceService/geodesic_distance',
                request_serializer=distance__unary__pb2.SourceDest.SerializeToString,
                response_deserializer=distance__unary__pb2.Distance.FromString,
                )


class DistanceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def geodesic_distance(self, request, context):
        """unary services just give a single response
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DistanceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'geodesic_distance': grpc.unary_unary_rpc_method_handler(
                    servicer.geodesic_distance,
                    request_deserializer=distance__unary__pb2.SourceDest.FromString,
                    response_serializer=distance__unary__pb2.Distance.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DistanceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class DistanceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def geodesic_distance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistanceService/geodesic_distance',
            distance__unary__pb2.SourceDest.SerializeToString,
            distance__unary__pb2.Distance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
