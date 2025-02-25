# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caffe2/proto/caffe2_legacy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='caffe2/proto/caffe2_legacy.proto',
  package='caffe2',
  serialized_pb=_b('\n caffe2/proto/caffe2_legacy.proto\x12\x06\x63\x61\x66\x66\x65\x32\"\x86\x01\n\nCaffeDatum\x12\x10\n\x08\x63hannels\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\r\n\x05label\x18\x05 \x01(\x05\x12\x12\n\nfloat_data\x18\x06 \x03(\x02\x12\x16\n\x07\x65ncoded\x18\x07 \x01(\x08:\x05\x66\x61lse*J\n\rLegacyPadding\x12\n\n\x06NOTSET\x10\x00\x12\t\n\x05VALID\x10\x01\x12\x08\n\x04SAME\x10\x02\x12\x18\n\x14\x43\x41\x46\x46\x45_LEGACY_POOLING\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LEGACYPADDING = _descriptor.EnumDescriptor(
  name='LegacyPadding',
  full_name='caffe2.LegacyPadding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOTSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAME', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAFFE_LEGACY_POOLING', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=181,
  serialized_end=255,
)
_sym_db.RegisterEnumDescriptor(_LEGACYPADDING)

LegacyPadding = enum_type_wrapper.EnumTypeWrapper(_LEGACYPADDING)
NOTSET = 0
VALID = 1
SAME = 2
CAFFE_LEGACY_POOLING = 3



_CAFFEDATUM = _descriptor.Descriptor(
  name='CaffeDatum',
  full_name='caffe2.CaffeDatum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='caffe2.CaffeDatum.channels', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='caffe2.CaffeDatum.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='caffe2.CaffeDatum.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='caffe2.CaffeDatum.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='caffe2.CaffeDatum.label', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_data', full_name='caffe2.CaffeDatum.float_data', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encoded', full_name='caffe2.CaffeDatum.encoded', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=45,
  serialized_end=179,
)

DESCRIPTOR.message_types_by_name['CaffeDatum'] = _CAFFEDATUM
DESCRIPTOR.enum_types_by_name['LegacyPadding'] = _LEGACYPADDING

CaffeDatum = _reflection.GeneratedProtocolMessageType('CaffeDatum', (_message.Message,), dict(
  DESCRIPTOR = _CAFFEDATUM,
  __module__ = 'caffe2.proto.caffe2_legacy_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.CaffeDatum)
  ))
_sym_db.RegisterMessage(CaffeDatum)


# @@protoc_insertion_point(module_scope)
