# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SetpointSensorPair.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SetpointSensorPair.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18SetpointSensorPair.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\x80\x02\n\x12SetpointSensorPair\x12\x1f\n\nsetpointId\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x03\x92?\x02\x38\x10\x12\x1d\n\x08sensorId\x18\x02 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x02\x92?\x02\x38\x10\x12\x1d\n\rsetpointValid\x18\x03 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12\x1b\n\x0bsensorValid\x18\x04 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12\x33\n\rsetpointValue\x18\x05 \x01(\x11\x42\x1c\x8a\xb5\x18\x06\n\x04\x64\x65gC\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x31\n\x0bsensorValue\x18\x06 \x01(\x11\x42\x1c\x8a\xb5\x18\x06\n\x04\x64\x65gC\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01:\x06\x92?\x03H\xaf\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_SETPOINTSENSORPAIR = _descriptor.Descriptor(
  name='SetpointSensorPair',
  full_name='blox.SetpointSensorPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setpointId', full_name='blox.SetpointSensorPair.setpointId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\003\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorId', full_name='blox.SetpointSensorPair.sensorId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\002\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setpointValid', full_name='blox.SetpointSensorPair.setpointValid', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorValid', full_name='blox.SetpointSensorPair.sensorValid', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setpointValue', full_name='blox.SetpointSensorPair.setpointValue', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\006\n\004degC\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorValue', full_name='blox.SetpointSensorPair.sensorValue', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\006\n\004degC\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\222?\003H\257\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=321,
)

DESCRIPTOR.message_types_by_name['SetpointSensorPair'] = _SETPOINTSENSORPAIR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetpointSensorPair = _reflection.GeneratedProtocolMessageType('SetpointSensorPair', (_message.Message,), dict(
  DESCRIPTOR = _SETPOINTSENSORPAIR,
  __module__ = 'SetpointSensorPair_pb2'
  # @@protoc_insertion_point(class_scope:blox.SetpointSensorPair)
  ))
_sym_db.RegisterMessage(SetpointSensorPair)


_SETPOINTSENSORPAIR.fields_by_name['setpointId']._options = None
_SETPOINTSENSORPAIR.fields_by_name['sensorId']._options = None
_SETPOINTSENSORPAIR.fields_by_name['setpointValid']._options = None
_SETPOINTSENSORPAIR.fields_by_name['sensorValid']._options = None
_SETPOINTSENSORPAIR.fields_by_name['setpointValue']._options = None
_SETPOINTSENSORPAIR.fields_by_name['sensorValue']._options = None
_SETPOINTSENSORPAIR._options = None
# @@protoc_insertion_point(module_scope)
