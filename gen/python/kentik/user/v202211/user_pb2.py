# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kentik/user/v202211/user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from kentik.core.v202012alpha1 import annotations_pb2 as kentik_dot_core_dot_v202012alpha1_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ekentik/user/v202211/user.proto\x12\x13kentik.user.v202211\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a+kentik/core/v202012alpha1/annotations.proto\"\xc4\x01\n\x0fPermissionEntry\x12`\n\ncapability\x18\x01 \x01(\tB@\x92\x41\x39\x32\x37String identifying capability that is granted of denied\xe2\x41\x01\x02R\ncapability\x12O\n\x07\x61llowed\x18\x02 \x01(\x08\x42\x35\x92\x41.2,Flag indicating whether operation is allowed\xe2\x41\x01\x02R\x07\x61llowed\"\xb4\x06\n\x04User\x12;\n\x02id\x18\x01 \x01(\tB+\x92\x41$2\"System generated unique identifier\xe2\x41\x01\x03R\x02id\x12U\n\nuser_email\x18\x02 \x01(\tB6\x92\x41/2-User e-mail address (serves also as username)\xe2\x41\x01\x02R\tuserEmail\x12\x38\n\x0euser_full_name\x18\x04 \x01(\tB\x12\x92\x41\x0b\x32\tFull name\xe2\x41\x01\x02R\x0cuserFullName\x12Y\n\x04role\x18\x05 \x01(\x0e\x32\x19.kentik.user.v202211.RoleB*\x92\x41#2!User role (in Kentik application)\xe2\x41\x01\x02R\x04role\x12}\n\x0bpermissions\x18\x06 \x03(\x0b\x32$.kentik.user.v202211.PermissionEntryB5\x92\x41\x32\x32\x30Optional list of permissions granted to the userR\x0bpermissions\x12\x61\n\x06\x66ilter\x18\x07 \x01(\tBI\x92\x41\x46\x32\x44Optional JSON string defining filter for objects visible to the userR\x06\x66ilter\x12n\n\nlast_login\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB3\x92\x41,2*UTC Timestamp of user\'s last login session\xe2\x41\x01\x03R\tlastLogin\x12S\n\x05\x63\x64\x61te\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB!\x92\x41\x1a\x32\x18\x43reation timestamp (UTC)\xe2\x41\x01\x03R\x05\x63\x64\x61te\x12\\\n\x05\x65\x64\x61te\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB*\x92\x41#2!Last modification timestamp (UTC)\xe2\x41\x01\x03R\x05\x65\x64\x61te\"\x12\n\x10ListUsersRequest\"\xd2\x01\n\x11ListUsersResponse\x12V\n\x05users\x18\x01 \x03(\x0b\x32\x19.kentik.user.v202211.UserB%\x92\x41\x1e\x32\x1cLast of users in the account\xe2\x41\x01\x03R\x05users\x12\x65\n\rinvalid_count\x18\x02 \x01(\rB@\x92\x41=2;Number of invalid entries encountered while collecting dataR\x0cinvalidCount\"C\n\x0eGetUserRequest\x12\x31\n\x02id\x18\x01 \x01(\tB!\x92\x41\x1a\x32\x18ID of the requested user\xe2\x41\x01\x02R\x02id\"k\n\x0fGetUserResponse\x12X\n\x04user\x18\x01 \x01(\x0b\x32\x19.kentik.user.v202211.UserB)\x92\x41&2$Information about the requested userR\x04user\"z\n\x11\x43reateUserRequest\x12\x65\n\x04user\x18\x01 \x01(\x0b\x32\x19.kentik.user.v202211.UserB6\x92\x41/2-Attributes for the user account to be created\xe2\x41\x01\x02R\x04user\"w\n\x12\x43reateUserResponse\x12\x61\n\x04user\x18\x01 \x01(\x0b\x32\x19.kentik.user.v202211.UserB2\x92\x41/2-Attributes for the newly created user accountR\x04user\"p\n\x11UpdateUserRequest\x12[\n\x04user\x18\x01 \x01(\x0b\x32\x19.kentik.user.v202211.UserB,\x92\x41%2#New attributes for the user account\xe2\x41\x01\x02R\x04user\"i\n\x12UpdateUserResponse\x12S\n\x04user\x18\x01 \x01(\x0b\x32\x19.kentik.user.v202211.UserB$\x92\x41!2\x1fUpdated user account attributesR\x04user\"V\n\x11\x44\x65leteUserRequest\x12\x41\n\x02id\x18\x01 \x01(\tB1\x92\x41*2(ID of the the user account to be deleted\xe2\x41\x01\x02R\x02id\"\x14\n\x12\x44\x65leteUserResponse\"c\n\x14ResetApiTokenRequest\x12K\n\x02id\x18\x01 \x01(\tB;\x92\x41\x34\x32\x32ID of the the user whose API token should be reset\xe2\x41\x01\x02R\x02id\"\x17\n\x15ResetApiTokenResponse\"h\n\x1aResetActiveSessionsRequest\x12J\n\x02id\x18\x01 \x01(\tB:\x92\x41\x33\x32\x31ID of the the user whose sessions should be reset\xe2\x41\x01\x02R\x02id\"\x1d\n\x1bResetActiveSessionsResponse*c\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bROLE_MEMBER\x10\x01\x12\x16\n\x12ROLE_ADMINISTRATOR\x10\x02\x12\x1c\n\x18ROLE_SUPER_ADMINISTRATOR\x10\x03\x32\xac\x0f\n\x0bUserService\x12\xdf\x01\n\tListUsers\x12%.kentik.user.v202211.ListUsersRequest\x1a&.kentik.user.v202211.ListUsersResponse\"\x82\x01\x92\x41Q\x12\x0fList all users.\x1a\x33Returns a list of all user accounts in the company.*\tListUsers\xf2\xd7\x02\x0f\x61\x64min.user:read\x82\xd3\xe4\x93\x02\x15\x12\x13/user/v202211/users\x12\xf0\x01\n\x07GetUser\x12#.kentik.user.v202211.GetUserRequest\x1a$.kentik.user.v202211.GetUserResponse\"\x99\x01\x92\x41\x63\x12!Get attributes of a user account.\x1a\x35Returns attributes of a user account specified by ID.*\x07GetUser\xf2\xd7\x02\x0f\x61\x64min.user:read\x82\xd3\xe4\x93\x02\x1a\x12\x18/user/v202211/users/{id}\x12\xab\x02\n\nCreateUser\x12&.kentik.user.v202211.CreateUserRequest\x1a\'.kentik.user.v202211.CreateUserResponse\"\xcb\x01\x92\x41\x95\x01\x12\x18\x43reate new user account.\x1amCreates new user account based on attributes in the request. Returns attributes of the newly created account.*\nCreateUser\xf2\xd7\x02\x10\x61\x64min.user:write\x82\xd3\xe4\x93\x02\x18\"\x13/user/v202211/users:\x01*\x12\xc9\x02\n\nUpdateUser\x12&.kentik.user.v202211.UpdateUserRequest\x1a\'.kentik.user.v202211.UpdateUserResponse\"\xe9\x01\x92\x41\xa9\x01\x12$Update attributes of a user account.\x1auReplaces all attributes of a user account specified by ID with attributes in the request. Returns updated attributes.*\nUpdateUser\xf2\xd7\x02\x10\x61\x64min.user:write\x82\xd3\xe4\x93\x02\"\x1a\x1d/user/v202211/users/{user.id}:\x01*\x12\xe2\x01\n\nDeleteUser\x12&.kentik.user.v202211.DeleteUserRequest\x1a\'.kentik.user.v202211.DeleteUserResponse\"\x82\x01\x92\x41K\x12\x16\x44\x65lete a user account.\x1a%Deletes user account specified by ID.*\nDeleteUser\xf2\xd7\x02\x10\x61\x64min.user:write\x82\xd3\xe4\x93\x02\x1a*\x18/user/v202211/users/{id}\x12\x8a\x02\n\rResetApiToken\x12).kentik.user.v202211.ResetApiTokenRequest\x1a*.kentik.user.v202211.ResetApiTokenResponse\"\xa1\x01\x92\x41Z\x12\x1bReset API token for a user.\x1a,Resets API token for a user specified by ID.*\rResetApiToken\xf2\xd7\x02\x10\x61\x64min.user:write\x82\xd3\xe4\x93\x02*\x1a(/user/v202211/users/{id}/reset_api_token\x12\xb5\x02\n\x13ResetActiveSessions\x12/.kentik.user.v202211.ResetActiveSessionsRequest\x1a\x30.kentik.user.v202211.ResetActiveSessionsResponse\"\xba\x01\x92\x41m\x12\"Resets active sessions for a user.\x1a\x32Resets active sessions for a user specified by ID.*\x13ResetActiveSessions\xf2\xd7\x02\x10\x61\x64min.user:write\x82\xd3\xe4\x93\x02\x30\x1a./user/v202211/users/{id}/reset_active_sessions\x1a$\xca\x41\x13grpc.api.kentik.com\xea\xd7\x02\nadmin.userB\xe9\x19Z<github.com/kentik/api-schema/gen/go/kentik/user/v202211;user\x92\x41\xa7\x19\x12\xc0\x17\n\x13User Management API\x12\xd8\x16# Overview\nThe User Management API enables programmatic administration of users within your organization. The API may be used to grant permissions to users at two levels: \n* **User role**: Permissions based on the level assigned to the Kentik user, either Member, Administrator, or Super Administrator (see [About Users](https://kb.kentik.com/v4/Cb02.htm#Cb02-About_Users)).\n* **User permissions**: Permissions granting access to specific capabilities of the Kentik platform (see [User Permissions](https://kb.kentik.com/v4/Cb02.htm#Cb02-User_Permissions)).\n\nBoth REST endpoint and gRPC RPCs are provided.\n\n***Note:*** The legacy REST-only [User API](https://kb.kentik.com/v0/Ec06.htm#Ec06-User_API) provides a subset of the functionality of this API.\n\n# User Permission Identifiers\n\nIndividual user permissions are represented in this API by string-based identifiers. The table below shows the identifier used in the API for each permission that can be enabled/disabled with the checkboxes on the Permissions tab of the Edit User dialog in the Kentik portal\'s Manage Users module (Settings \xc2\xbb Manage Users).\n| Portal setting  | API identifier |\n|-----------------|----------------|\n| Cancel Queries in Forensic Viewer | forensic_viewer.cancel_queries |\n| Synthetics Permissions: Create tests | synthetics.tests.create |\n| Synthetics Permissions: Edit tests | synthetics.tests.edit |\n| Synthetics Permissions: Delete tests | synthetics.tests.delete |\n| Synthetics Permissions: Create agents | synthetics.agents.create |\n| Synthetics Permissions: Edit agents | synthetics.agents.edit |\n| Synthetics Permissions: Delete agents | synthetics.agents.delete |\n| Connectivity Costs Permissions: View Costs | connectivity_costs.read |\n| Connectivity Costs Permissions: Configure Costs | connectivity_costs.edit |\n\n**_Note:_** The API returns an error if the same permission is both granted and denied in the same request.\n\n### Default Permissions\n\nThe permissions above that are enabled/disabled by default depend on the role (level) of the user:\n* **Member**: All permissions in the table above are denied by default.\n* **Administrator** or **Super Administrator**: All permissions are granted. \n\n# User Filter Attribute\n\nUser filters enable Administrators to apply filters that restrict the data that can be returned from queries by a given user (see [User Filters](https://kb.kentik.com/v4/Cb02.htm#Cb02-User_Filters)). In the Kentik portal these filters are set on the Filters tab of the Edit User dialog in the Manage Users module. In this API the filters are set in the `user` object with the `filter` attribute, whose type is string. The value of the attribute is given in JSON notation. The recommended way to construct the JSON string is to configure the desired filter for one user in the Kentik portal and then copy the value of the `user.filter` attribute returned for that user by the `GetUser` RPC.\"E\n\x16Kentik API Engineering\x12+https://github.com/kentik/api-schema-public2\x07v202211*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZD\n\x1e\n\x05\x65mail\x12\x15\x08\x02\x1a\x0fX-CH-Auth-Email \x02\n\"\n\x05token\x12\x19\x08\x02\x1a\x13X-CH-Auth-API-Token \x02\x62\x16\n\t\n\x05\x65mail\x12\x00\n\t\n\x05token\x12\x00r]\n%General information about Kentik APIs\x12\x34https://kb.kentik.com/v0/Ab09.htm#Ab09-APIs_Overviewb\x06proto3')

_ROLE = DESCRIPTOR.enum_types_by_name['Role']
Role = enum_type_wrapper.EnumTypeWrapper(_ROLE)
ROLE_UNSPECIFIED = 0
ROLE_MEMBER = 1
ROLE_ADMINISTRATOR = 2
ROLE_SUPER_ADMINISTRATOR = 3


_PERMISSIONENTRY = DESCRIPTOR.message_types_by_name['PermissionEntry']
_USER = DESCRIPTOR.message_types_by_name['User']
_LISTUSERSREQUEST = DESCRIPTOR.message_types_by_name['ListUsersRequest']
_LISTUSERSRESPONSE = DESCRIPTOR.message_types_by_name['ListUsersResponse']
_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_GETUSERRESPONSE = DESCRIPTOR.message_types_by_name['GetUserResponse']
_CREATEUSERREQUEST = DESCRIPTOR.message_types_by_name['CreateUserRequest']
_CREATEUSERRESPONSE = DESCRIPTOR.message_types_by_name['CreateUserResponse']
_UPDATEUSERREQUEST = DESCRIPTOR.message_types_by_name['UpdateUserRequest']
_UPDATEUSERRESPONSE = DESCRIPTOR.message_types_by_name['UpdateUserResponse']
_DELETEUSERREQUEST = DESCRIPTOR.message_types_by_name['DeleteUserRequest']
_DELETEUSERRESPONSE = DESCRIPTOR.message_types_by_name['DeleteUserResponse']
_RESETAPITOKENREQUEST = DESCRIPTOR.message_types_by_name['ResetApiTokenRequest']
_RESETAPITOKENRESPONSE = DESCRIPTOR.message_types_by_name['ResetApiTokenResponse']
_RESETACTIVESESSIONSREQUEST = DESCRIPTOR.message_types_by_name['ResetActiveSessionsRequest']
_RESETACTIVESESSIONSRESPONSE = DESCRIPTOR.message_types_by_name['ResetActiveSessionsResponse']
PermissionEntry = _reflection.GeneratedProtocolMessageType('PermissionEntry', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONENTRY,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.PermissionEntry)
  })
_sym_db.RegisterMessage(PermissionEntry)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.User)
  })
_sym_db.RegisterMessage(User)

ListUsersRequest = _reflection.GeneratedProtocolMessageType('ListUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSREQUEST,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.ListUsersRequest)
  })
_sym_db.RegisterMessage(ListUsersRequest)

ListUsersResponse = _reflection.GeneratedProtocolMessageType('ListUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSRESPONSE,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.ListUsersResponse)
  })
_sym_db.RegisterMessage(ListUsersResponse)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserResponse = _reflection.GeneratedProtocolMessageType('CreateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESPONSE,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.CreateUserResponse)
  })
_sym_db.RegisterMessage(CreateUserResponse)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

UpdateUserResponse = _reflection.GeneratedProtocolMessageType('UpdateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERRESPONSE,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.UpdateUserResponse)
  })
_sym_db.RegisterMessage(UpdateUserResponse)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREQUEST,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.DeleteUserRequest)
  })
_sym_db.RegisterMessage(DeleteUserRequest)

DeleteUserResponse = _reflection.GeneratedProtocolMessageType('DeleteUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERRESPONSE,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.DeleteUserResponse)
  })
_sym_db.RegisterMessage(DeleteUserResponse)

ResetApiTokenRequest = _reflection.GeneratedProtocolMessageType('ResetApiTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETAPITOKENREQUEST,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.ResetApiTokenRequest)
  })
_sym_db.RegisterMessage(ResetApiTokenRequest)

ResetApiTokenResponse = _reflection.GeneratedProtocolMessageType('ResetApiTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETAPITOKENRESPONSE,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.ResetApiTokenResponse)
  })
_sym_db.RegisterMessage(ResetApiTokenResponse)

ResetActiveSessionsRequest = _reflection.GeneratedProtocolMessageType('ResetActiveSessionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETACTIVESESSIONSREQUEST,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.ResetActiveSessionsRequest)
  })
_sym_db.RegisterMessage(ResetActiveSessionsRequest)

ResetActiveSessionsResponse = _reflection.GeneratedProtocolMessageType('ResetActiveSessionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETACTIVESESSIONSRESPONSE,
  '__module__' : 'kentik.user.v202211.user_pb2'
  # @@protoc_insertion_point(class_scope:kentik.user.v202211.ResetActiveSessionsResponse)
  })
_sym_db.RegisterMessage(ResetActiveSessionsResponse)

_USERSERVICE = DESCRIPTOR.services_by_name['UserService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z<github.com/kentik/api-schema/gen/go/kentik/user/v202211;user\222A\247\031\022\300\027\n\023User Management API\022\330\026# Overview\nThe User Management API enables programmatic administration of users within your organization. The API may be used to grant permissions to users at two levels: \n* **User role**: Permissions based on the level assigned to the Kentik user, either Member, Administrator, or Super Administrator (see [About Users](https://kb.kentik.com/v4/Cb02.htm#Cb02-About_Users)).\n* **User permissions**: Permissions granting access to specific capabilities of the Kentik platform (see [User Permissions](https://kb.kentik.com/v4/Cb02.htm#Cb02-User_Permissions)).\n\nBoth REST endpoint and gRPC RPCs are provided.\n\n***Note:*** The legacy REST-only [User API](https://kb.kentik.com/v0/Ec06.htm#Ec06-User_API) provides a subset of the functionality of this API.\n\n# User Permission Identifiers\n\nIndividual user permissions are represented in this API by string-based identifiers. The table below shows the identifier used in the API for each permission that can be enabled/disabled with the checkboxes on the Permissions tab of the Edit User dialog in the Kentik portal\'s Manage Users module (Settings \302\273 Manage Users).\n| Portal setting  | API identifier |\n|-----------------|----------------|\n| Cancel Queries in Forensic Viewer | forensic_viewer.cancel_queries |\n| Synthetics Permissions: Create tests | synthetics.tests.create |\n| Synthetics Permissions: Edit tests | synthetics.tests.edit |\n| Synthetics Permissions: Delete tests | synthetics.tests.delete |\n| Synthetics Permissions: Create agents | synthetics.agents.create |\n| Synthetics Permissions: Edit agents | synthetics.agents.edit |\n| Synthetics Permissions: Delete agents | synthetics.agents.delete |\n| Connectivity Costs Permissions: View Costs | connectivity_costs.read |\n| Connectivity Costs Permissions: Configure Costs | connectivity_costs.edit |\n\n**_Note:_** The API returns an error if the same permission is both granted and denied in the same request.\n\n### Default Permissions\n\nThe permissions above that are enabled/disabled by default depend on the role (level) of the user:\n* **Member**: All permissions in the table above are denied by default.\n* **Administrator** or **Super Administrator**: All permissions are granted. \n\n# User Filter Attribute\n\nUser filters enable Administrators to apply filters that restrict the data that can be returned from queries by a given user (see [User Filters](https://kb.kentik.com/v4/Cb02.htm#Cb02-User_Filters)). In the Kentik portal these filters are set on the Filters tab of the Edit User dialog in the Manage Users module. In this API the filters are set in the `user` object with the `filter` attribute, whose type is string. The value of the attribute is given in JSON notation. The recommended way to construct the JSON string is to configure the desired filter for one user in the Kentik portal and then copy the value of the `user.filter` attribute returned for that user by the `GetUser` RPC.\"E\n\026Kentik API Engineering\022+https://github.com/kentik/api-schema-public2\007v202211*\001\0022\020application/json:\020application/jsonZD\n\036\n\005email\022\025\010\002\032\017X-CH-Auth-Email \002\n\"\n\005token\022\031\010\002\032\023X-CH-Auth-API-Token \002b\026\n\t\n\005email\022\000\n\t\n\005token\022\000r]\n%General information about Kentik APIs\0224https://kb.kentik.com/v0/Ab09.htm#Ab09-APIs_Overview'
  _PERMISSIONENTRY.fields_by_name['capability']._options = None
  _PERMISSIONENTRY.fields_by_name['capability']._serialized_options = b'\222A927String identifying capability that is granted of denied\342A\001\002'
  _PERMISSIONENTRY.fields_by_name['allowed']._options = None
  _PERMISSIONENTRY.fields_by_name['allowed']._serialized_options = b'\222A.2,Flag indicating whether operation is allowed\342A\001\002'
  _USER.fields_by_name['id']._options = None
  _USER.fields_by_name['id']._serialized_options = b'\222A$2\"System generated unique identifier\342A\001\003'
  _USER.fields_by_name['user_email']._options = None
  _USER.fields_by_name['user_email']._serialized_options = b'\222A/2-User e-mail address (serves also as username)\342A\001\002'
  _USER.fields_by_name['user_full_name']._options = None
  _USER.fields_by_name['user_full_name']._serialized_options = b'\222A\0132\tFull name\342A\001\002'
  _USER.fields_by_name['role']._options = None
  _USER.fields_by_name['role']._serialized_options = b'\222A#2!User role (in Kentik application)\342A\001\002'
  _USER.fields_by_name['permissions']._options = None
  _USER.fields_by_name['permissions']._serialized_options = b'\222A220Optional list of permissions granted to the user'
  _USER.fields_by_name['filter']._options = None
  _USER.fields_by_name['filter']._serialized_options = b'\222AF2DOptional JSON string defining filter for objects visible to the user'
  _USER.fields_by_name['last_login']._options = None
  _USER.fields_by_name['last_login']._serialized_options = b'\222A,2*UTC Timestamp of user\'s last login session\342A\001\003'
  _USER.fields_by_name['cdate']._options = None
  _USER.fields_by_name['cdate']._serialized_options = b'\222A\0322\030Creation timestamp (UTC)\342A\001\003'
  _USER.fields_by_name['edate']._options = None
  _USER.fields_by_name['edate']._serialized_options = b'\222A#2!Last modification timestamp (UTC)\342A\001\003'
  _LISTUSERSRESPONSE.fields_by_name['users']._options = None
  _LISTUSERSRESPONSE.fields_by_name['users']._serialized_options = b'\222A\0362\034Last of users in the account\342A\001\003'
  _LISTUSERSRESPONSE.fields_by_name['invalid_count']._options = None
  _LISTUSERSRESPONSE.fields_by_name['invalid_count']._serialized_options = b'\222A=2;Number of invalid entries encountered while collecting data'
  _GETUSERREQUEST.fields_by_name['id']._options = None
  _GETUSERREQUEST.fields_by_name['id']._serialized_options = b'\222A\0322\030ID of the requested user\342A\001\002'
  _GETUSERRESPONSE.fields_by_name['user']._options = None
  _GETUSERRESPONSE.fields_by_name['user']._serialized_options = b'\222A&2$Information about the requested user'
  _CREATEUSERREQUEST.fields_by_name['user']._options = None
  _CREATEUSERREQUEST.fields_by_name['user']._serialized_options = b'\222A/2-Attributes for the user account to be created\342A\001\002'
  _CREATEUSERRESPONSE.fields_by_name['user']._options = None
  _CREATEUSERRESPONSE.fields_by_name['user']._serialized_options = b'\222A/2-Attributes for the newly created user account'
  _UPDATEUSERREQUEST.fields_by_name['user']._options = None
  _UPDATEUSERREQUEST.fields_by_name['user']._serialized_options = b'\222A%2#New attributes for the user account\342A\001\002'
  _UPDATEUSERRESPONSE.fields_by_name['user']._options = None
  _UPDATEUSERRESPONSE.fields_by_name['user']._serialized_options = b'\222A!2\037Updated user account attributes'
  _DELETEUSERREQUEST.fields_by_name['id']._options = None
  _DELETEUSERREQUEST.fields_by_name['id']._serialized_options = b'\222A*2(ID of the the user account to be deleted\342A\001\002'
  _RESETAPITOKENREQUEST.fields_by_name['id']._options = None
  _RESETAPITOKENREQUEST.fields_by_name['id']._serialized_options = b'\222A422ID of the the user whose API token should be reset\342A\001\002'
  _RESETACTIVESESSIONSREQUEST.fields_by_name['id']._options = None
  _RESETACTIVESESSIONSREQUEST.fields_by_name['id']._serialized_options = b'\222A321ID of the the user whose sessions should be reset\342A\001\002'
  _USERSERVICE._options = None
  _USERSERVICE._serialized_options = b'\312A\023grpc.api.kentik.com\352\327\002\nadmin.user'
  _USERSERVICE.methods_by_name['ListUsers']._options = None
  _USERSERVICE.methods_by_name['ListUsers']._serialized_options = b'\222AQ\022\017List all users.\0323Returns a list of all user accounts in the company.*\tListUsers\362\327\002\017admin.user:read\202\323\344\223\002\025\022\023/user/v202211/users'
  _USERSERVICE.methods_by_name['GetUser']._options = None
  _USERSERVICE.methods_by_name['GetUser']._serialized_options = b'\222Ac\022!Get attributes of a user account.\0325Returns attributes of a user account specified by ID.*\007GetUser\362\327\002\017admin.user:read\202\323\344\223\002\032\022\030/user/v202211/users/{id}'
  _USERSERVICE.methods_by_name['CreateUser']._options = None
  _USERSERVICE.methods_by_name['CreateUser']._serialized_options = b'\222A\225\001\022\030Create new user account.\032mCreates new user account based on attributes in the request. Returns attributes of the newly created account.*\nCreateUser\362\327\002\020admin.user:write\202\323\344\223\002\030\"\023/user/v202211/users:\001*'
  _USERSERVICE.methods_by_name['UpdateUser']._options = None
  _USERSERVICE.methods_by_name['UpdateUser']._serialized_options = b'\222A\251\001\022$Update attributes of a user account.\032uReplaces all attributes of a user account specified by ID with attributes in the request. Returns updated attributes.*\nUpdateUser\362\327\002\020admin.user:write\202\323\344\223\002\"\032\035/user/v202211/users/{user.id}:\001*'
  _USERSERVICE.methods_by_name['DeleteUser']._options = None
  _USERSERVICE.methods_by_name['DeleteUser']._serialized_options = b'\222AK\022\026Delete a user account.\032%Deletes user account specified by ID.*\nDeleteUser\362\327\002\020admin.user:write\202\323\344\223\002\032*\030/user/v202211/users/{id}'
  _USERSERVICE.methods_by_name['ResetApiToken']._options = None
  _USERSERVICE.methods_by_name['ResetApiToken']._serialized_options = b'\222AZ\022\033Reset API token for a user.\032,Resets API token for a user specified by ID.*\rResetApiToken\362\327\002\020admin.user:write\202\323\344\223\002*\032(/user/v202211/users/{id}/reset_api_token'
  _USERSERVICE.methods_by_name['ResetActiveSessions']._options = None
  _USERSERVICE.methods_by_name['ResetActiveSessions']._serialized_options = b'\222Am\022\"Resets active sessions for a user.\0322Resets active sessions for a user specified by ID.*\023ResetActiveSessions\362\327\002\020admin.user:write\202\323\344\223\0020\032./user/v202211/users/{id}/reset_active_sessions'
  _ROLE._serialized_start=2541
  _ROLE._serialized_end=2640
  _PERMISSIONENTRY._serialized_start=270
  _PERMISSIONENTRY._serialized_end=466
  _USER._serialized_start=469
  _USER._serialized_end=1289
  _LISTUSERSREQUEST._serialized_start=1291
  _LISTUSERSREQUEST._serialized_end=1309
  _LISTUSERSRESPONSE._serialized_start=1312
  _LISTUSERSRESPONSE._serialized_end=1522
  _GETUSERREQUEST._serialized_start=1524
  _GETUSERREQUEST._serialized_end=1591
  _GETUSERRESPONSE._serialized_start=1593
  _GETUSERRESPONSE._serialized_end=1700
  _CREATEUSERREQUEST._serialized_start=1702
  _CREATEUSERREQUEST._serialized_end=1824
  _CREATEUSERRESPONSE._serialized_start=1826
  _CREATEUSERRESPONSE._serialized_end=1945
  _UPDATEUSERREQUEST._serialized_start=1947
  _UPDATEUSERREQUEST._serialized_end=2059
  _UPDATEUSERRESPONSE._serialized_start=2061
  _UPDATEUSERRESPONSE._serialized_end=2166
  _DELETEUSERREQUEST._serialized_start=2168
  _DELETEUSERREQUEST._serialized_end=2254
  _DELETEUSERRESPONSE._serialized_start=2256
  _DELETEUSERRESPONSE._serialized_end=2276
  _RESETAPITOKENREQUEST._serialized_start=2278
  _RESETAPITOKENREQUEST._serialized_end=2377
  _RESETAPITOKENRESPONSE._serialized_start=2379
  _RESETAPITOKENRESPONSE._serialized_end=2402
  _RESETACTIVESESSIONSREQUEST._serialized_start=2404
  _RESETACTIVESESSIONSREQUEST._serialized_end=2508
  _RESETACTIVESESSIONSRESPONSE._serialized_start=2510
  _RESETACTIVESESSIONSRESPONSE._serialized_end=2539
  _USERSERVICE._serialized_start=2643
  _USERSERVICE._serialized_end=4607
# @@protoc_insertion_point(module_scope)