# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Balancer.proto

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
  name='Balancer.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x42\x61lancer.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xcb\x01\n\x08\x42\x61lancer\x12\x38\n\x07\x63lients\x18\x01 \x03(\x0b\x32\x1f.blox.Balancer.BalancedActuatorB\x06\x8a\xb5\x18\x02(\x01\x1a}\n\x10\x42\x61lancedActuator\x12\x1d\n\x02id\x18\x01 \x01(\rB\x11\x8a\xb5\x18\x02\x18\x05\x92?\x02\x38\x10\x8a\xb5\x18\x02(\x01\x12%\n\trequested\x18\x02 \x01(\x11\x42\x12\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12#\n\x07granted\x18\x03 \x01(\x11\x42\x12\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01:\x06\x92?\x03H\xb5\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_BALANCER_BALANCEDACTUATOR = _descriptor.Descriptor(
  name='BalancedActuator',
  full_name='blox.Balancer.BalancedActuator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='blox.Balancer.BalancedActuator.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\005\222?\0028\020\212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requested', full_name='blox.Balancer.BalancedActuator.requested', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granted', full_name='blox.Balancer.BalancedActuator.granted', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=250,
)

_BALANCER = _descriptor.Descriptor(
  name='Balancer',
  full_name='blox.Balancer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clients', full_name='blox.Balancer.clients', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BALANCER_BALANCEDACTUATOR, ],
  enum_types=[
  ],
  serialized_options=_b('\222?\003H\265\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=258,
)

_BALANCER_BALANCEDACTUATOR.containing_type = _BALANCER
_BALANCER.fields_by_name['clients'].message_type = _BALANCER_BALANCEDACTUATOR
DESCRIPTOR.message_types_by_name['Balancer'] = _BALANCER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Balancer = _reflection.GeneratedProtocolMessageType('Balancer', (_message.Message,), dict(

  BalancedActuator = _reflection.GeneratedProtocolMessageType('BalancedActuator', (_message.Message,), dict(
    DESCRIPTOR = _BALANCER_BALANCEDACTUATOR,
    __module__ = 'Balancer_pb2'
    # @@protoc_insertion_point(class_scope:blox.Balancer.BalancedActuator)
    ))
  ,
  DESCRIPTOR = _BALANCER,
  __module__ = 'Balancer_pb2'
  # @@protoc_insertion_point(class_scope:blox.Balancer)
  ))
_sym_db.RegisterMessage(Balancer)
_sym_db.RegisterMessage(Balancer.BalancedActuator)


_BALANCER_BALANCEDACTUATOR.fields_by_name['id']._options = None
_BALANCER_BALANCEDACTUATOR.fields_by_name['requested']._options = None
_BALANCER_BALANCEDACTUATOR.fields_by_name['granted']._options = None
_BALANCER.fields_by_name['clients']._options = None
_BALANCER._options = None
# @@protoc_insertion_point(module_scope)
