# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: grpc/channelz/channelz.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.any_pb2
import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import grpc.channelz.channelz_pb2


class ChannelzBase(abc.ABC):

    @abc.abstractmethod
    async def GetTopChannels(self, stream: 'grpclib.server.Stream[grpc.channelz.channelz_pb2.GetTopChannelsRequest, grpc.channelz.channelz_pb2.GetTopChannelsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetServers(self, stream: 'grpclib.server.Stream[grpc.channelz.channelz_pb2.GetServersRequest, grpc.channelz.channelz_pb2.GetServersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetServer(self, stream: 'grpclib.server.Stream[grpc.channelz.channelz_pb2.GetServerRequest, grpc.channelz.channelz_pb2.GetServerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetServerSockets(self, stream: 'grpclib.server.Stream[grpc.channelz.channelz_pb2.GetServerSocketsRequest, grpc.channelz.channelz_pb2.GetServerSocketsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetChannel(self, stream: 'grpclib.server.Stream[grpc.channelz.channelz_pb2.GetChannelRequest, grpc.channelz.channelz_pb2.GetChannelResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSubchannel(self, stream: 'grpclib.server.Stream[grpc.channelz.channelz_pb2.GetSubchannelRequest, grpc.channelz.channelz_pb2.GetSubchannelResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSocket(self, stream: 'grpclib.server.Stream[grpc.channelz.channelz_pb2.GetSocketRequest, grpc.channelz.channelz_pb2.GetSocketResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/grpc.channelz.v1.Channelz/GetTopChannels': grpclib.const.Handler(
                self.GetTopChannels,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc.channelz.channelz_pb2.GetTopChannelsRequest,
                grpc.channelz.channelz_pb2.GetTopChannelsResponse,
            ),
            '/grpc.channelz.v1.Channelz/GetServers': grpclib.const.Handler(
                self.GetServers,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc.channelz.channelz_pb2.GetServersRequest,
                grpc.channelz.channelz_pb2.GetServersResponse,
            ),
            '/grpc.channelz.v1.Channelz/GetServer': grpclib.const.Handler(
                self.GetServer,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc.channelz.channelz_pb2.GetServerRequest,
                grpc.channelz.channelz_pb2.GetServerResponse,
            ),
            '/grpc.channelz.v1.Channelz/GetServerSockets': grpclib.const.Handler(
                self.GetServerSockets,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc.channelz.channelz_pb2.GetServerSocketsRequest,
                grpc.channelz.channelz_pb2.GetServerSocketsResponse,
            ),
            '/grpc.channelz.v1.Channelz/GetChannel': grpclib.const.Handler(
                self.GetChannel,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc.channelz.channelz_pb2.GetChannelRequest,
                grpc.channelz.channelz_pb2.GetChannelResponse,
            ),
            '/grpc.channelz.v1.Channelz/GetSubchannel': grpclib.const.Handler(
                self.GetSubchannel,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc.channelz.channelz_pb2.GetSubchannelRequest,
                grpc.channelz.channelz_pb2.GetSubchannelResponse,
            ),
            '/grpc.channelz.v1.Channelz/GetSocket': grpclib.const.Handler(
                self.GetSocket,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpc.channelz.channelz_pb2.GetSocketRequest,
                grpc.channelz.channelz_pb2.GetSocketResponse,
            ),
        }


class ChannelzStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetTopChannels = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc.channelz.v1.Channelz/GetTopChannels',
            grpc.channelz.channelz_pb2.GetTopChannelsRequest,
            grpc.channelz.channelz_pb2.GetTopChannelsResponse,
        )
        self.GetServers = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc.channelz.v1.Channelz/GetServers',
            grpc.channelz.channelz_pb2.GetServersRequest,
            grpc.channelz.channelz_pb2.GetServersResponse,
        )
        self.GetServer = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc.channelz.v1.Channelz/GetServer',
            grpc.channelz.channelz_pb2.GetServerRequest,
            grpc.channelz.channelz_pb2.GetServerResponse,
        )
        self.GetServerSockets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc.channelz.v1.Channelz/GetServerSockets',
            grpc.channelz.channelz_pb2.GetServerSocketsRequest,
            grpc.channelz.channelz_pb2.GetServerSocketsResponse,
        )
        self.GetChannel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc.channelz.v1.Channelz/GetChannel',
            grpc.channelz.channelz_pb2.GetChannelRequest,
            grpc.channelz.channelz_pb2.GetChannelResponse,
        )
        self.GetSubchannel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc.channelz.v1.Channelz/GetSubchannel',
            grpc.channelz.channelz_pb2.GetSubchannelRequest,
            grpc.channelz.channelz_pb2.GetSubchannelResponse,
        )
        self.GetSocket = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc.channelz.v1.Channelz/GetSocket',
            grpc.channelz.channelz_pb2.GetSocketRequest,
            grpc.channelz.channelz_pb2.GetSocketResponse,
        )