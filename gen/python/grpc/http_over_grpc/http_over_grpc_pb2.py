# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc/http_over_grpc/http_over_grpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(grpc/http_over_grpc/http_over_grpc.proto\x12\x13grpc.http_over_grpc\"2\n\x06Header\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x16\n\x06values\x18\x02 \x03(\tR\x06values\"\x8a\x01\n\x13HTTPOverGRPCRequest\x12\x16\n\x06method\x18\x01 \x01(\tR\x06method\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12\x35\n\x07headers\x18\x03 \x03(\x0b\x32\x1b.grpc.http_over_grpc.HeaderR\x07headers\x12\x12\n\x04\x62ody\x18\x04 \x01(\x0cR\x04\x62ody\"v\n\x11HTTPOverGRPCReply\x12\x16\n\x06status\x18\x01 \x01(\x05R\x06status\x12\x35\n\x07headers\x18\x02 \x03(\x0b\x32\x1b.grpc.http_over_grpc.HeaderR\x07headers\x12\x12\n\x04\x62ody\x18\x03 \x01(\x0cR\x04\x62ody2q\n\x0cHTTPOverGRPC\x12\x61\n\x0bHTTPRequest\x12(.grpc.http_over_grpc.HTTPOverGRPCRequest\x1a&.grpc.http_over_grpc.HTTPOverGRPCReply\"\x00\x62\x06proto3')



_HEADER = DESCRIPTOR.message_types_by_name['Header']
_HTTPOVERGRPCREQUEST = DESCRIPTOR.message_types_by_name['HTTPOverGRPCRequest']
_HTTPOVERGRPCREPLY = DESCRIPTOR.message_types_by_name['HTTPOverGRPCReply']
Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'grpc.http_over_grpc.http_over_grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc.http_over_grpc.Header)
  })
_sym_db.RegisterMessage(Header)

HTTPOverGRPCRequest = _reflection.GeneratedProtocolMessageType('HTTPOverGRPCRequest', (_message.Message,), {
  'DESCRIPTOR' : _HTTPOVERGRPCREQUEST,
  '__module__' : 'grpc.http_over_grpc.http_over_grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc.http_over_grpc.HTTPOverGRPCRequest)
  })
_sym_db.RegisterMessage(HTTPOverGRPCRequest)

HTTPOverGRPCReply = _reflection.GeneratedProtocolMessageType('HTTPOverGRPCReply', (_message.Message,), {
  'DESCRIPTOR' : _HTTPOVERGRPCREPLY,
  '__module__' : 'grpc.http_over_grpc.http_over_grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpc.http_over_grpc.HTTPOverGRPCReply)
  })
_sym_db.RegisterMessage(HTTPOverGRPCReply)

_HTTPOVERGRPC = DESCRIPTOR.services_by_name['HTTPOverGRPC']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEADER._serialized_start=65
  _HEADER._serialized_end=115
  _HTTPOVERGRPCREQUEST._serialized_start=118
  _HTTPOVERGRPCREQUEST._serialized_end=256
  _HTTPOVERGRPCREPLY._serialized_start=258
  _HTTPOVERGRPCREPLY._serialized_end=376
  _HTTPOVERGRPC._serialized_start=378
  _HTTPOVERGRPC._serialized_end=491
# @@protoc_insertion_point(module_scope)
