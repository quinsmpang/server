# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UnitProto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UnitProto.proto',
  package='Base',
  serialized_pb=_b('\n\x0fUnitProto.proto\x12\x04\x42\x61se\"*\n\tUnitProto\x12\r\n\x02id\x18\x01 \x02(\x05:\x01\x30\x12\x0e\n\x04name\x18\x02 \x02(\t:\x00\"1\n\x0fUnitProto_ARRAY\x12\x1e\n\x05items\x18\x01 \x03(\x0b\x32\x0f.Base.UnitProto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UNITPROTO = _descriptor.Descriptor(
  name='UnitProto',
  full_name='Base.UnitProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Base.UnitProto.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Base.UnitProto.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=67,
)


_UNITPROTO_ARRAY = _descriptor.Descriptor(
  name='UnitProto_ARRAY',
  full_name='Base.UnitProto_ARRAY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='Base.UnitProto_ARRAY.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=118,
)

_UNITPROTO_ARRAY.fields_by_name['items'].message_type = _UNITPROTO
DESCRIPTOR.message_types_by_name['UnitProto'] = _UNITPROTO
DESCRIPTOR.message_types_by_name['UnitProto_ARRAY'] = _UNITPROTO_ARRAY

UnitProto = _reflection.GeneratedProtocolMessageType('UnitProto', (_message.Message,), dict(
  DESCRIPTOR = _UNITPROTO,
  __module__ = 'UnitProto_pb2'
  # @@protoc_insertion_point(class_scope:Base.UnitProto)
  ))
_sym_db.RegisterMessage(UnitProto)

UnitProto_ARRAY = _reflection.GeneratedProtocolMessageType('UnitProto_ARRAY', (_message.Message,), dict(
  DESCRIPTOR = _UNITPROTO_ARRAY,
  __module__ = 'UnitProto_pb2'
  # @@protoc_insertion_point(class_scope:Base.UnitProto_ARRAY)
  ))
_sym_db.RegisterMessage(UnitProto_ARRAY)


# @@protoc_insertion_point(module_scope)