# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='example/example.proto',
  package='foo.bar',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x65xample/example.proto\x12\x07\x66oo.bar\x1a\x1bgoogle/protobuf/empty.proto\"\xe2\x04\n\x0bTestMessage\x12\x0e\n\x06\x64ouble\x18\x01 \x01(\x01\x12\r\n\x05\x66loat\x18\x02 \x01(\x02\x12\r\n\x05int64\x18\x03 \x01(\x03\x12\x0e\n\x06uint64\x18\x04 \x01(\x04\x12\r\n\x05int32\x18\x05 \x01(\x05\x12\x0f\n\x07\x66ixed64\x18\x06 \x01(\x06\x12\x0f\n\x07\x66ixed32\x18\x07 \x01(\x07\x12\x0c\n\x04\x62ool\x18\x08 \x01(\x08\x12\x0e\n\x06string\x18\t \x01(\t\x12\x43\n\x13test_nested_message\x18\x0b \x01(\x0b\x32&.foo.bar.TestMessage.TestNestedMessage\x12\r\n\x05\x62ytes\x18\x0c \x01(\x0c\x12\x0e\n\x06uint32\x18\r \x01(\r\x12=\n\x10test_nested_enum\x18\x0e \x01(\x0e\x32#.foo.bar.TestMessage.TestNestedEnum\x12\x10\n\x08sfixed32\x18\x0f \x01(\x0f\x12\x10\n\x08sfixed64\x18\x10 \x01(\x10\x12\x0e\n\x06sint32\x18\x11 \x01(\x11\x12\x0e\n\x06sint64\x18\x12 \x01(\x12\x12@\n\x0fpbt_message_map\x18\x13 \x03(\x0b\x32\'.foo.bar.TestMessage.PbtMessageMapEntry\x1a \n\x11TestNestedMessage\x12\x0b\n\x03\x62\x61r\x18\x01 \x01(\t\x1a\\\n\x12PbtMessageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.foo.bar.TestMessage.TestNestedMessage:\x02\x38\x01\"\x1d\n\x0eTestNestedEnum\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00*\x17\n\x08TestEnum\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x32\xab\x03\n\x0bTestService\x12J\n\nTestMethod\x12\x14.foo.bar.TestMessage\x1a&.foo.bar.TestMessage.TestNestedMessage\x12Q\n\x0f\x43lientStreaming\x12\x14.foo.bar.TestMessage\x1a&.foo.bar.TestMessage.TestNestedMessage(\x01\x12Q\n\x0fServerStreaming\x12\x14.foo.bar.TestMessage\x1a&.foo.bar.TestMessage.TestNestedMessage0\x01\x12k\n\x15\x43lientServerStreaming\x12&.foo.bar.TestMessage.TestNestedMessage\x1a&.foo.bar.TestMessage.TestNestedMessage(\x01\x30\x01\x12=\n\x0b\x45mptyMethod\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_TESTENUM = _descriptor.EnumDescriptor(
  name='TestEnum',
  full_name='foo.bar.TestEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=676,
  serialized_end=699,
)
_sym_db.RegisterEnumDescriptor(_TESTENUM)

TestEnum = enum_type_wrapper.EnumTypeWrapper(_TESTENUM)
DEFAULT = 0


_TESTMESSAGE_TESTNESTEDENUM = _descriptor.EnumDescriptor(
  name='TestNestedEnum',
  full_name='foo.bar.TestMessage.TestNestedEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=645,
  serialized_end=674,
)
_sym_db.RegisterEnumDescriptor(_TESTMESSAGE_TESTNESTEDENUM)


_TESTMESSAGE_TESTNESTEDMESSAGE = _descriptor.Descriptor(
  name='TestNestedMessage',
  full_name='foo.bar.TestMessage.TestNestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bar', full_name='foo.bar.TestMessage.TestNestedMessage.bar', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=517,
  serialized_end=549,
)

_TESTMESSAGE_PBTMESSAGEMAPENTRY = _descriptor.Descriptor(
  name='PbtMessageMapEntry',
  full_name='foo.bar.TestMessage.PbtMessageMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='foo.bar.TestMessage.PbtMessageMapEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='foo.bar.TestMessage.PbtMessageMapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=643,
)

_TESTMESSAGE = _descriptor.Descriptor(
  name='TestMessage',
  full_name='foo.bar.TestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='double', full_name='foo.bar.TestMessage.double', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float', full_name='foo.bar.TestMessage.float', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64', full_name='foo.bar.TestMessage.int64', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64', full_name='foo.bar.TestMessage.uint64', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32', full_name='foo.bar.TestMessage.int32', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed64', full_name='foo.bar.TestMessage.fixed64', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed32', full_name='foo.bar.TestMessage.fixed32', index=6,
      number=7, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool', full_name='foo.bar.TestMessage.bool', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string', full_name='foo.bar.TestMessage.string', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_nested_message', full_name='foo.bar.TestMessage.test_nested_message', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='foo.bar.TestMessage.bytes', index=10,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32', full_name='foo.bar.TestMessage.uint32', index=11,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_nested_enum', full_name='foo.bar.TestMessage.test_nested_enum', index=12,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sfixed32', full_name='foo.bar.TestMessage.sfixed32', index=13,
      number=15, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sfixed64', full_name='foo.bar.TestMessage.sfixed64', index=14,
      number=16, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sint32', full_name='foo.bar.TestMessage.sint32', index=15,
      number=17, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sint64', full_name='foo.bar.TestMessage.sint64', index=16,
      number=18, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pbt_message_map', full_name='foo.bar.TestMessage.pbt_message_map', index=17,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TESTMESSAGE_TESTNESTEDMESSAGE, _TESTMESSAGE_PBTMESSAGEMAPENTRY, ],
  enum_types=[
    _TESTMESSAGE_TESTNESTEDENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=674,
)

_TESTMESSAGE_TESTNESTEDMESSAGE.containing_type = _TESTMESSAGE
_TESTMESSAGE_PBTMESSAGEMAPENTRY.fields_by_name['value'].message_type = _TESTMESSAGE_TESTNESTEDMESSAGE
_TESTMESSAGE_PBTMESSAGEMAPENTRY.containing_type = _TESTMESSAGE
_TESTMESSAGE.fields_by_name['test_nested_message'].message_type = _TESTMESSAGE_TESTNESTEDMESSAGE
_TESTMESSAGE.fields_by_name['test_nested_enum'].enum_type = _TESTMESSAGE_TESTNESTEDENUM
_TESTMESSAGE.fields_by_name['pbt_message_map'].message_type = _TESTMESSAGE_PBTMESSAGEMAPENTRY
_TESTMESSAGE_TESTNESTEDENUM.containing_type = _TESTMESSAGE
DESCRIPTOR.message_types_by_name['TestMessage'] = _TESTMESSAGE
DESCRIPTOR.enum_types_by_name['TestEnum'] = _TESTENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMessage = _reflection.GeneratedProtocolMessageType('TestMessage', (_message.Message,), {

  'TestNestedMessage' : _reflection.GeneratedProtocolMessageType('TestNestedMessage', (_message.Message,), {
    'DESCRIPTOR' : _TESTMESSAGE_TESTNESTEDMESSAGE,
    '__module__' : 'example.example_pb2'
    # @@protoc_insertion_point(class_scope:foo.bar.TestMessage.TestNestedMessage)
    })
  ,

  'PbtMessageMapEntry' : _reflection.GeneratedProtocolMessageType('PbtMessageMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _TESTMESSAGE_PBTMESSAGEMAPENTRY,
    '__module__' : 'example.example_pb2'
    # @@protoc_insertion_point(class_scope:foo.bar.TestMessage.PbtMessageMapEntry)
    })
  ,
  'DESCRIPTOR' : _TESTMESSAGE,
  '__module__' : 'example.example_pb2'
  # @@protoc_insertion_point(class_scope:foo.bar.TestMessage)
  })
_sym_db.RegisterMessage(TestMessage)
_sym_db.RegisterMessage(TestMessage.TestNestedMessage)
_sym_db.RegisterMessage(TestMessage.PbtMessageMapEntry)


_TESTMESSAGE_PBTMESSAGEMAPENTRY._options = None

_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='foo.bar.TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=702,
  serialized_end=1129,
  methods=[
  _descriptor.MethodDescriptor(
    name='TestMethod',
    full_name='foo.bar.TestService.TestMethod',
    index=0,
    containing_service=None,
    input_type=_TESTMESSAGE,
    output_type=_TESTMESSAGE_TESTNESTEDMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClientStreaming',
    full_name='foo.bar.TestService.ClientStreaming',
    index=1,
    containing_service=None,
    input_type=_TESTMESSAGE,
    output_type=_TESTMESSAGE_TESTNESTEDMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ServerStreaming',
    full_name='foo.bar.TestService.ServerStreaming',
    index=2,
    containing_service=None,
    input_type=_TESTMESSAGE,
    output_type=_TESTMESSAGE_TESTNESTEDMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClientServerStreaming',
    full_name='foo.bar.TestService.ClientServerStreaming',
    index=3,
    containing_service=None,
    input_type=_TESTMESSAGE_TESTNESTEDMESSAGE,
    output_type=_TESTMESSAGE_TESTNESTEDMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EmptyMethod',
    full_name='foo.bar.TestService.EmptyMethod',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
