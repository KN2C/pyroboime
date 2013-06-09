# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import referee_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='savestate.proto',
  package='',
  serialized_pb='\n\x0fsavestate.proto\x1a\rreferee.proto\"\xa5\x03\n\tSaveState\x12\x1d\n\x07referee\x18\x01 \x02(\x0b\x32\x0c.SSL_Referee\x12\x1c\n\x14yellow_penalty_goals\x18\x02 \x02(\r\x12\x1a\n\x12\x62lue_penalty_goals\x18\x03 \x02(\r\x12\x12\n\ntime_taken\x18\x04 \x02(\x04\x12&\n\tlast_card\x18\x05 \x01(\x0b\x32\x13.SaveState.CardInfo\x12\'\n\x07timeout\x18\x06 \x01(\x0b\x32\x16.SaveState.TimeoutInfo\x1aH\n\x08\x43\x61rdInfo\x12\x1d\n\x04team\x18\x01 \x02(\x0e\x32\x0f.SaveState.Team\x12\x1d\n\x04\x63\x61rd\x18\x02 \x02(\x0e\x32\x0f.SaveState.Card\x1a\x41\n\x0bTimeoutInfo\x12\x1d\n\x04team\x18\x01 \x02(\x0e\x32\x0f.SaveState.Team\x12\x13\n\x0bleft_before\x18\x02 \x02(\r\"&\n\x04Team\x12\x0f\n\x0bTEAM_YELLOW\x10\x00\x12\r\n\tTEAM_BLUE\x10\x01\"%\n\x04\x43\x61rd\x12\x0f\n\x0b\x43\x41RD_YELLOW\x10\x00\x12\x0c\n\x08\x43\x41RD_RED\x10\x01')



_SAVESTATE_TEAM = descriptor.EnumDescriptor(
  name='Team',
  full_name='SaveState.Team',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='TEAM_YELLOW', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TEAM_BLUE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=379,
  serialized_end=417,
)

_SAVESTATE_CARD = descriptor.EnumDescriptor(
  name='Card',
  full_name='SaveState.Card',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CARD_YELLOW', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CARD_RED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=419,
  serialized_end=456,
)


_SAVESTATE_CARDINFO = descriptor.Descriptor(
  name='CardInfo',
  full_name='SaveState.CardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='team', full_name='SaveState.CardInfo.team', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='card', full_name='SaveState.CardInfo.card', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=238,
  serialized_end=310,
)

_SAVESTATE_TIMEOUTINFO = descriptor.Descriptor(
  name='TimeoutInfo',
  full_name='SaveState.TimeoutInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='team', full_name='SaveState.TimeoutInfo.team', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='left_before', full_name='SaveState.TimeoutInfo.left_before', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=312,
  serialized_end=377,
)

_SAVESTATE = descriptor.Descriptor(
  name='SaveState',
  full_name='SaveState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='referee', full_name='SaveState.referee', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='yellow_penalty_goals', full_name='SaveState.yellow_penalty_goals', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='blue_penalty_goals', full_name='SaveState.blue_penalty_goals', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_taken', full_name='SaveState.time_taken', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_card', full_name='SaveState.last_card', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeout', full_name='SaveState.timeout', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SAVESTATE_CARDINFO, _SAVESTATE_TIMEOUTINFO, ],
  enum_types=[
    _SAVESTATE_TEAM,
    _SAVESTATE_CARD,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=35,
  serialized_end=456,
)

_SAVESTATE_CARDINFO.fields_by_name['team'].enum_type = _SAVESTATE_TEAM
_SAVESTATE_CARDINFO.fields_by_name['card'].enum_type = _SAVESTATE_CARD
_SAVESTATE_CARDINFO.containing_type = _SAVESTATE;
_SAVESTATE_TIMEOUTINFO.fields_by_name['team'].enum_type = _SAVESTATE_TEAM
_SAVESTATE_TIMEOUTINFO.containing_type = _SAVESTATE;
_SAVESTATE.fields_by_name['referee'].message_type = referee_pb2._SSL_REFEREE
_SAVESTATE.fields_by_name['last_card'].message_type = _SAVESTATE_CARDINFO
_SAVESTATE.fields_by_name['timeout'].message_type = _SAVESTATE_TIMEOUTINFO
_SAVESTATE_TEAM.containing_type = _SAVESTATE;
_SAVESTATE_CARD.containing_type = _SAVESTATE;
DESCRIPTOR.message_types_by_name['SaveState'] = _SAVESTATE

class SaveState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class CardInfo(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SAVESTATE_CARDINFO
    
    # @@protoc_insertion_point(class_scope:SaveState.CardInfo)
  
  class TimeoutInfo(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SAVESTATE_TIMEOUTINFO
    
    # @@protoc_insertion_point(class_scope:SaveState.TimeoutInfo)
  DESCRIPTOR = _SAVESTATE
  
  # @@protoc_insertion_point(class_scope:SaveState)

# @@protoc_insertion_point(module_scope)
