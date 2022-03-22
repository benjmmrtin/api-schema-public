# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc/lb/v1/load_reporter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egrpc/lb/v1/load_reporter.proto\x12\ngrpc.lb.v1\x1a\x1egoogle/protobuf/duration.proto\"R\n\x11LoadReportRequest\x12=\n\x0finitial_request\x18\x01 \x01(\x0b\x32$.grpc.lb.v1.InitialLoadReportRequest\"\x85\x01\n\x18InitialLoadReportRequest\x12\x1e\n\x16load_balanced_hostname\x18\x01 \x01(\t\x12\x10\n\x08load_key\x18\x02 \x01(\x0c\x12\x37\n\x14load_report_interval\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xb9\x01\n\x12LoadReportResponse\x12?\n\x10initial_response\x18\x01 \x01(\x0b\x32%.grpc.lb.v1.InitialLoadReportResponse\x12\x42\n\x17load_balancing_feedback\x18\x02 \x01(\x0b\x32!.grpc.lb.v1.LoadBalancingFeedback\x12\x1e\n\x04load\x18\x03 \x03(\x0b\x32\x10.grpc.lb.v1.Load\"\xf5\x01\n\x19InitialLoadReportResponse\x12\x18\n\x10load_balancer_id\x18\x01 \x01(\t\x12Y\n\x11implementation_id\x18\x02 \x01(\x0e\x32>.grpc.lb.v1.InitialLoadReportResponse.ImplementationIdentifier\x12\x16\n\x0eserver_version\x18\x03 \x01(\x03\"K\n\x18ImplementationIdentifier\x12\x14\n\x10IMPL_UNSPECIFIED\x10\x00\x12\x07\n\x03\x43PP\x10\x01\x12\x08\n\x04JAVA\x10\x02\x12\x06\n\x02GO\x10\x03\"h\n\x15LoadBalancingFeedback\x12\x1a\n\x12server_utilization\x18\x01 \x01(\x02\x12\x18\n\x10\x63\x61lls_per_second\x18\x02 \x01(\x02\x12\x19\n\x11\x65rrors_per_second\x18\x03 \x01(\x02\"\xcb\x04\n\x04Load\x12\x18\n\x10load_balance_tag\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x19\n\x11\x63lient_ip_address\x18\x0f \x01(\x0c\x12\x19\n\x11num_calls_started\x18\x04 \x01(\x03\x12\x1f\n\x15num_calls_in_progress\x18\x05 \x01(\x03H\x00\x12(\n num_calls_finished_without_error\x18\x06 \x01(\x03\x12%\n\x1dnum_calls_finished_with_error\x18\x07 \x01(\x03\x12,\n$num_calls_finished_with_server_error\x18\x10 \x01(\x03\x12\x18\n\x10total_bytes_sent\x18\x08 \x01(\x03\x12\x1c\n\x14total_bytes_received\x18\t \x01(\x03\x12\x30\n\rtotal_latency\x18\n \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0bmetric_data\x18\x0b \x03(\x0b\x32\x1a.grpc.lb.v1.CallMetricData\x12\x16\n\x08load_key\x18\x0c \x01(\x0c\x42\x02\x18\x01H\x01\x12\x1a\n\x10load_key_unknown\x18\r \x01(\x08H\x01\x12\x46\n\x18orphaned_load_identifier\x18\x0e \x01(\x0b\x32\".grpc.lb.v1.OrphanedLoadIdentifierH\x01\x42\x14\n\x12in_progress_reportB\x0f\n\rorphaned_loadJ\x04\x08\x02\x10\x03\"i\n\x0e\x43\x61llMetricData\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t\x12&\n\x1enum_calls_finished_with_metric\x18\x02 \x01(\x03\x12\x1a\n\x12total_metric_value\x18\x03 \x01(\x01\"D\n\x16OrphanedLoadIdentifier\x12\x10\n\x08load_key\x18\x01 \x01(\x0c\x12\x18\n\x10load_balancer_id\x18\x02 \x01(\t2a\n\x0cLoadReporter\x12Q\n\nReportLoad\x12\x1d.grpc.lb.v1.LoadReportRequest\x1a\x1e.grpc.lb.v1.LoadReportResponse\"\x00(\x01\x30\x01\x62\x06proto3')



_LOADREPORTREQUEST = DESCRIPTOR.message_types_by_name['LoadReportRequest']
_INITIALLOADREPORTREQUEST = DESCRIPTOR.message_types_by_name['InitialLoadReportRequest']
_LOADREPORTRESPONSE = DESCRIPTOR.message_types_by_name['LoadReportResponse']
_INITIALLOADREPORTRESPONSE = DESCRIPTOR.message_types_by_name['InitialLoadReportResponse']
_LOADBALANCINGFEEDBACK = DESCRIPTOR.message_types_by_name['LoadBalancingFeedback']
_LOAD = DESCRIPTOR.message_types_by_name['Load']
_CALLMETRICDATA = DESCRIPTOR.message_types_by_name['CallMetricData']
_ORPHANEDLOADIDENTIFIER = DESCRIPTOR.message_types_by_name['OrphanedLoadIdentifier']
_INITIALLOADREPORTRESPONSE_IMPLEMENTATIONIDENTIFIER = _INITIALLOADREPORTRESPONSE.enum_types_by_name['ImplementationIdentifier']
LoadReportRequest = _reflection.GeneratedProtocolMessageType('LoadReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOADREPORTREQUEST,
  '__module__' : 'grpc.lb.v1.load_reporter_pb2'
  # @@protoc_insertion_point(class_scope:grpc.lb.v1.LoadReportRequest)
  })
_sym_db.RegisterMessage(LoadReportRequest)

InitialLoadReportRequest = _reflection.GeneratedProtocolMessageType('InitialLoadReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _INITIALLOADREPORTREQUEST,
  '__module__' : 'grpc.lb.v1.load_reporter_pb2'
  # @@protoc_insertion_point(class_scope:grpc.lb.v1.InitialLoadReportRequest)
  })
_sym_db.RegisterMessage(InitialLoadReportRequest)

LoadReportResponse = _reflection.GeneratedProtocolMessageType('LoadReportResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOADREPORTRESPONSE,
  '__module__' : 'grpc.lb.v1.load_reporter_pb2'
  # @@protoc_insertion_point(class_scope:grpc.lb.v1.LoadReportResponse)
  })
_sym_db.RegisterMessage(LoadReportResponse)

InitialLoadReportResponse = _reflection.GeneratedProtocolMessageType('InitialLoadReportResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITIALLOADREPORTRESPONSE,
  '__module__' : 'grpc.lb.v1.load_reporter_pb2'
  # @@protoc_insertion_point(class_scope:grpc.lb.v1.InitialLoadReportResponse)
  })
_sym_db.RegisterMessage(InitialLoadReportResponse)

LoadBalancingFeedback = _reflection.GeneratedProtocolMessageType('LoadBalancingFeedback', (_message.Message,), {
  'DESCRIPTOR' : _LOADBALANCINGFEEDBACK,
  '__module__' : 'grpc.lb.v1.load_reporter_pb2'
  # @@protoc_insertion_point(class_scope:grpc.lb.v1.LoadBalancingFeedback)
  })
_sym_db.RegisterMessage(LoadBalancingFeedback)

Load = _reflection.GeneratedProtocolMessageType('Load', (_message.Message,), {
  'DESCRIPTOR' : _LOAD,
  '__module__' : 'grpc.lb.v1.load_reporter_pb2'
  # @@protoc_insertion_point(class_scope:grpc.lb.v1.Load)
  })
_sym_db.RegisterMessage(Load)

CallMetricData = _reflection.GeneratedProtocolMessageType('CallMetricData', (_message.Message,), {
  'DESCRIPTOR' : _CALLMETRICDATA,
  '__module__' : 'grpc.lb.v1.load_reporter_pb2'
  # @@protoc_insertion_point(class_scope:grpc.lb.v1.CallMetricData)
  })
_sym_db.RegisterMessage(CallMetricData)

OrphanedLoadIdentifier = _reflection.GeneratedProtocolMessageType('OrphanedLoadIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _ORPHANEDLOADIDENTIFIER,
  '__module__' : 'grpc.lb.v1.load_reporter_pb2'
  # @@protoc_insertion_point(class_scope:grpc.lb.v1.OrphanedLoadIdentifier)
  })
_sym_db.RegisterMessage(OrphanedLoadIdentifier)

_LOADREPORTER = DESCRIPTOR.services_by_name['LoadReporter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOAD.fields_by_name['load_key']._options = None
  _LOAD.fields_by_name['load_key']._serialized_options = b'\030\001'
  _LOADREPORTREQUEST._serialized_start=78
  _LOADREPORTREQUEST._serialized_end=160
  _INITIALLOADREPORTREQUEST._serialized_start=163
  _INITIALLOADREPORTREQUEST._serialized_end=296
  _LOADREPORTRESPONSE._serialized_start=299
  _LOADREPORTRESPONSE._serialized_end=484
  _INITIALLOADREPORTRESPONSE._serialized_start=487
  _INITIALLOADREPORTRESPONSE._serialized_end=732
  _INITIALLOADREPORTRESPONSE_IMPLEMENTATIONIDENTIFIER._serialized_start=657
  _INITIALLOADREPORTRESPONSE_IMPLEMENTATIONIDENTIFIER._serialized_end=732
  _LOADBALANCINGFEEDBACK._serialized_start=734
  _LOADBALANCINGFEEDBACK._serialized_end=838
  _LOAD._serialized_start=841
  _LOAD._serialized_end=1428
  _CALLMETRICDATA._serialized_start=1430
  _CALLMETRICDATA._serialized_end=1535
  _ORPHANEDLOADIDENTIFIER._serialized_start=1537
  _ORPHANEDLOADIDENTIFIER._serialized_end=1605
  _LOADREPORTER._serialized_start=1607
  _LOADREPORTER._serialized_end=1704
# @@protoc_insertion_point(module_scope)
