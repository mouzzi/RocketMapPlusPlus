# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/use_item_stardust_boost_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/use_item_stardust_boost_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nMpogoprotos/networking/requests/messages/use_item_stardust_boost_message.proto\x12\'pogoprotos.networking.requests.messages\x1a\'pogoprotos/inventory/item/item_id.proto\"N\n\x1bUseItemStardustBoostMessage\x12/\n\x04item\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemIdb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])




_USEITEMSTARDUSTBOOSTMESSAGE = _descriptor.Descriptor(
  name='UseItemStardustBoostMessage',
  full_name='pogoprotos.networking.requests.messages.UseItemStardustBoostMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.networking.requests.messages.UseItemStardustBoostMessage.item', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=163,
  serialized_end=241,
)

_USEITEMSTARDUSTBOOSTMESSAGE.fields_by_name['item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
DESCRIPTOR.message_types_by_name['UseItemStardustBoostMessage'] = _USEITEMSTARDUSTBOOSTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UseItemStardustBoostMessage = _reflection.GeneratedProtocolMessageType('UseItemStardustBoostMessage', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMSTARDUSTBOOSTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.use_item_stardust_boost_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.UseItemStardustBoostMessage)
  ))
_sym_db.RegisterMessage(UseItemStardustBoostMessage)


# @@protoc_insertion_point(module_scope)