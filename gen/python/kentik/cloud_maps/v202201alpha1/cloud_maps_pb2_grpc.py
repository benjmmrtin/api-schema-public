# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kentik.cloud_maps.v202201alpha1 import cloud_maps_pb2 as kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2


class CloudMapsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProvideAwsMetadataStorageLocation = channel.unary_unary(
                '/kentik.cloud_maps.v202201alpha1.CloudMapsService/ProvideAwsMetadataStorageLocation',
                request_serializer=kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.ProvideAwsMetadataStorageLocationRequest.SerializeToString,
                response_deserializer=kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.ProvideAwsMetadataStorageLocationResponse.FromString,
                )
        self.GetAwsCrawlerConfiguration = channel.unary_unary(
                '/kentik.cloud_maps.v202201alpha1.CloudMapsService/GetAwsCrawlerConfiguration',
                request_serializer=kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.GetAwsCrawlerConfigurationRequest.SerializeToString,
                response_deserializer=kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.GetAwsCrawlerConfigurationResponse.FromString,
                )


class CloudMapsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProvideAwsMetadataStorageLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAwsCrawlerConfiguration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CloudMapsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProvideAwsMetadataStorageLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.ProvideAwsMetadataStorageLocation,
                    request_deserializer=kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.ProvideAwsMetadataStorageLocationRequest.FromString,
                    response_serializer=kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.ProvideAwsMetadataStorageLocationResponse.SerializeToString,
            ),
            'GetAwsCrawlerConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAwsCrawlerConfiguration,
                    request_deserializer=kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.GetAwsCrawlerConfigurationRequest.FromString,
                    response_serializer=kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.GetAwsCrawlerConfigurationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kentik.cloud_maps.v202201alpha1.CloudMapsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CloudMapsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProvideAwsMetadataStorageLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kentik.cloud_maps.v202201alpha1.CloudMapsService/ProvideAwsMetadataStorageLocation',
            kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.ProvideAwsMetadataStorageLocationRequest.SerializeToString,
            kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.ProvideAwsMetadataStorageLocationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAwsCrawlerConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kentik.cloud_maps.v202201alpha1.CloudMapsService/GetAwsCrawlerConfiguration',
            kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.GetAwsCrawlerConfigurationRequest.SerializeToString,
            kentik_dot_cloud__maps_dot_v202201alpha1_dot_cloud__maps__pb2.GetAwsCrawlerConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
