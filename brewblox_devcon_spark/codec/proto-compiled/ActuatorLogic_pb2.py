# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorLogic.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import IoArray_pb2 as IoArray__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ActuatorLogic.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13\x41\x63tuatorLogic.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\rIoArray.proto\"\x94\x05\n\x07\x43ompare\"\xcb\x03\n\x06Result\x12\x10\n\x0cRESULT_FALSE\x10\x00\x12\x0f\n\x0bRESULT_TRUE\x10\x01\x12\x10\n\x0cRESULT_EMPTY\x10\x02\x12\x1a\n\x16RESULT_EMPTY_SUBSTRING\x10\x03\x12\x1a\n\x16RESULT_BLOCK_NOT_FOUND\x10\x04\x12\x1d\n\x19RESULT_INVALID_DIGITAL_OP\x10\x05\x12\x1c\n\x18RESULT_INVALID_ANALOG_OP\x10\x06\x12$\n RESULT_UNDEFINED_DIGITAL_COMPARE\x10\x08\x12#\n\x1fRESULT_UNDEFINED_ANALOG_COMPARE\x10\x07\x12\"\n\x1eRESULT_UNEXPECTED_OPEN_BRACKET\x10\x0b\x12#\n\x1fRESULT_UNEXPECTED_CLOSE_BRACKET\x10\t\x12\x1f\n\x1bRESULT_UNEXPECTED_CHARACTER\x10\x0c\x12 \n\x1cRESULT_UNEXPECTED_COMPARISON\x10\r\x12\x1e\n\x1aRESULT_UNEXPECTED_OPERATOR\x10\x0e\x12 \n\x1cRESULT_MISSING_CLOSE_BRACKET\x10\n\"a\n\x0f\x44igitalOperator\x12\x0f\n\x0bOP_VALUE_IS\x10\x00\x12\x13\n\x0fOP_VALUE_IS_NOT\x10\x01\x12\x11\n\rOP_DESIRED_IS\x10\n\x12\x15\n\x11OP_DESIRED_IS_NOT\x10\x0b\"X\n\x0e\x41nalogOperator\x12\x0f\n\x0bOP_VALUE_LE\x10\x00\x12\x0f\n\x0bOP_VALUE_GE\x10\x01\x12\x11\n\rOP_SETTING_LE\x10\n\x12\x11\n\rOP_SETTING_GE\x10\x0b\"\xa3\x01\n\x0e\x44igitalCompare\x12)\n\x02op\x18\x01 \x01(\x0e\x32\x1d.blox.Compare.DigitalOperator\x12,\n\x06result\x18\x02 \x01(\x0e\x32\x14.blox.Compare.ResultB\x06\x8a\xb5\x18\x02(\x01\x12\x17\n\x02id\x18\x03 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x06\x92?\x02\x38\x10\x12\x1f\n\x03rhs\x18\x04 \x01(\x0e\x32\x12.blox.DigitalState\"\x9b\x01\n\rAnalogCompare\x12(\n\x02op\x18\x01 \x01(\x0e\x32\x1c.blox.Compare.AnalogOperator\x12,\n\x06result\x18\x02 \x01(\x0e\x32\x14.blox.Compare.ResultB\x06\x8a\xb5\x18\x02(\x01\x12\x17\n\x02id\x18\x03 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x01\x92?\x02\x38\x10\x12\x19\n\x03rhs\x18\x04 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \"\xc1\x02\n\rActuatorLogic\x12\x1d\n\x08targetId\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x06\x92?\x02\x38\x10\x12/\n\x0e\x64rivenTargetId\x18\x02 \x01(\rB\x17\x8a\xb5\x18\x02\x18\x06\x92?\x02\x38\x10\x8a\xb5\x18\x02@\x01\x8a\xb5\x18\x02(\x01\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x32\n\x06result\x18\x04 \x01(\x0e\x32\x14.blox.Compare.ResultB\x0c\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x12\x19\n\nexpression\x18\x05 \x01(\tB\x05\x92?\x02p@\x12,\n\x07\x64igital\x18\x06 \x03(\x0b\x32\x14.blox.DigitalCompareB\x05\x92?\x02\x10\x10\x12*\n\x06\x61nalog\x18\x07 \x03(\x0b\x32\x13.blox.AnalogCompareB\x05\x92?\x02\x10\x10\x12\x1d\n\x08\x65rrorPos\x18\x08 \x01(\rB\x0b\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08:\x07\x8a\xb5\x18\x03\x18\xc2\x02\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,IoArray__pb2.DESCRIPTOR,])



_COMPARE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='blox.Compare.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_FALSE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TRUE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_EMPTY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_EMPTY_SUBSTRING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_BLOCK_NOT_FOUND', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_INVALID_DIGITAL_OP', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_INVALID_ANALOG_OP', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNDEFINED_DIGITAL_COMPARE', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNDEFINED_ANALOG_COMPARE', index=8, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNEXPECTED_OPEN_BRACKET', index=9, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNEXPECTED_CLOSE_BRACKET', index=10, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNEXPECTED_CHARACTER', index=11, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNEXPECTED_COMPARISON', index=12, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNEXPECTED_OPERATOR', index=13, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_MISSING_CLOSE_BRACKET', index=14, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=87,
  serialized_end=546,
)
_sym_db.RegisterEnumDescriptor(_COMPARE_RESULT)

_COMPARE_DIGITALOPERATOR = _descriptor.EnumDescriptor(
  name='DigitalOperator',
  full_name='blox.Compare.DigitalOperator',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OP_VALUE_IS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OP_VALUE_IS_NOT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OP_DESIRED_IS', index=2, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OP_DESIRED_IS_NOT', index=3, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=548,
  serialized_end=645,
)
_sym_db.RegisterEnumDescriptor(_COMPARE_DIGITALOPERATOR)

_COMPARE_ANALOGOPERATOR = _descriptor.EnumDescriptor(
  name='AnalogOperator',
  full_name='blox.Compare.AnalogOperator',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OP_VALUE_LE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OP_VALUE_GE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OP_SETTING_LE', index=2, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OP_SETTING_GE', index=3, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=647,
  serialized_end=735,
)
_sym_db.RegisterEnumDescriptor(_COMPARE_ANALOGOPERATOR)


_COMPARE = _descriptor.Descriptor(
  name='Compare',
  full_name='blox.Compare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMPARE_RESULT,
    _COMPARE_DIGITALOPERATOR,
    _COMPARE_ANALOGOPERATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=735,
)


_DIGITALCOMPARE = _descriptor.Descriptor(
  name='DigitalCompare',
  full_name='blox.DigitalCompare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='blox.DigitalCompare.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='blox.DigitalCompare.result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='blox.DigitalCompare.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\006\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rhs', full_name='blox.DigitalCompare.rhs', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=738,
  serialized_end=901,
)


_ANALOGCOMPARE = _descriptor.Descriptor(
  name='AnalogCompare',
  full_name='blox.AnalogCompare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='blox.AnalogCompare.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='blox.AnalogCompare.result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='blox.AnalogCompare.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\001\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rhs', full_name='blox.AnalogCompare.rhs', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
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
  serialized_start=904,
  serialized_end=1059,
)


_ACTUATORLOGIC = _descriptor.Descriptor(
  name='ActuatorLogic',
  full_name='blox.ActuatorLogic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='blox.ActuatorLogic.targetId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\006\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drivenTargetId', full_name='blox.ActuatorLogic.drivenTargetId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\006\222?\0028\020\212\265\030\002@\001\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='blox.ActuatorLogic.enabled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='blox.ActuatorLogic.result', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expression', full_name='blox.ActuatorLogic.expression', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002p@', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digital', full_name='blox.ActuatorLogic.digital', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\020\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='analog', full_name='blox.ActuatorLogic.analog', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\020\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorPos', full_name='blox.ActuatorLogic.errorPos', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\302\002',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1062,
  serialized_end=1383,
)

_COMPARE_RESULT.containing_type = _COMPARE
_COMPARE_DIGITALOPERATOR.containing_type = _COMPARE
_COMPARE_ANALOGOPERATOR.containing_type = _COMPARE
_DIGITALCOMPARE.fields_by_name['op'].enum_type = _COMPARE_DIGITALOPERATOR
_DIGITALCOMPARE.fields_by_name['result'].enum_type = _COMPARE_RESULT
_DIGITALCOMPARE.fields_by_name['rhs'].enum_type = IoArray__pb2._DIGITALSTATE
_ANALOGCOMPARE.fields_by_name['op'].enum_type = _COMPARE_ANALOGOPERATOR
_ANALOGCOMPARE.fields_by_name['result'].enum_type = _COMPARE_RESULT
_ACTUATORLOGIC.fields_by_name['result'].enum_type = _COMPARE_RESULT
_ACTUATORLOGIC.fields_by_name['digital'].message_type = _DIGITALCOMPARE
_ACTUATORLOGIC.fields_by_name['analog'].message_type = _ANALOGCOMPARE
DESCRIPTOR.message_types_by_name['Compare'] = _COMPARE
DESCRIPTOR.message_types_by_name['DigitalCompare'] = _DIGITALCOMPARE
DESCRIPTOR.message_types_by_name['AnalogCompare'] = _ANALOGCOMPARE
DESCRIPTOR.message_types_by_name['ActuatorLogic'] = _ACTUATORLOGIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Compare = _reflection.GeneratedProtocolMessageType('Compare', (_message.Message,), {
  'DESCRIPTOR' : _COMPARE,
  '__module__' : 'ActuatorLogic_pb2'
  # @@protoc_insertion_point(class_scope:blox.Compare)
  })
_sym_db.RegisterMessage(Compare)

DigitalCompare = _reflection.GeneratedProtocolMessageType('DigitalCompare', (_message.Message,), {
  'DESCRIPTOR' : _DIGITALCOMPARE,
  '__module__' : 'ActuatorLogic_pb2'
  # @@protoc_insertion_point(class_scope:blox.DigitalCompare)
  })
_sym_db.RegisterMessage(DigitalCompare)

AnalogCompare = _reflection.GeneratedProtocolMessageType('AnalogCompare', (_message.Message,), {
  'DESCRIPTOR' : _ANALOGCOMPARE,
  '__module__' : 'ActuatorLogic_pb2'
  # @@protoc_insertion_point(class_scope:blox.AnalogCompare)
  })
_sym_db.RegisterMessage(AnalogCompare)

ActuatorLogic = _reflection.GeneratedProtocolMessageType('ActuatorLogic', (_message.Message,), {
  'DESCRIPTOR' : _ACTUATORLOGIC,
  '__module__' : 'ActuatorLogic_pb2'
  # @@protoc_insertion_point(class_scope:blox.ActuatorLogic)
  })
_sym_db.RegisterMessage(ActuatorLogic)


_DIGITALCOMPARE.fields_by_name['result']._options = None
_DIGITALCOMPARE.fields_by_name['id']._options = None
_ANALOGCOMPARE.fields_by_name['result']._options = None
_ANALOGCOMPARE.fields_by_name['id']._options = None
_ANALOGCOMPARE.fields_by_name['rhs']._options = None
_ACTUATORLOGIC.fields_by_name['targetId']._options = None
_ACTUATORLOGIC.fields_by_name['drivenTargetId']._options = None
_ACTUATORLOGIC.fields_by_name['result']._options = None
_ACTUATORLOGIC.fields_by_name['expression']._options = None
_ACTUATORLOGIC.fields_by_name['digital']._options = None
_ACTUATORLOGIC.fields_by_name['analog']._options = None
_ACTUATORLOGIC.fields_by_name['errorPos']._options = None
_ACTUATORLOGIC._options = None
# @@protoc_insertion_point(module_scope)
