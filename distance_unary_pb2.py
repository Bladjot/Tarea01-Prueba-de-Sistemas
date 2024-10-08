from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x64istance_unary.proto\"S\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x15\n\x08\x61ltitude\x18\x03 \x01(\x02H\x00\x88\x01\x01\x42\x0b\n\t_altitude\"c\n\nSourceDest\x12\x19\n\x06source\x18\x01 \x01(\x0b\x32\t.Position\x12\x1e\n\x0b\x64\x65stination\x18\x02 \x01(\x0b\x32\t.Position\x12\x11\n\x04unit\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_unit\":\n\x08\x44istance\x12\x10\n\x08\x64istance\x18\x01 \x01(\x02\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t2@\n\x0f\x44istanceService\x12-\n\x11geodesic_distance\x12\x0b.SourceDest\x1a\t.Distance\"\x00\x62\x06proto3')



_POSITION = DESCRIPTOR.message_types_by_name['Position']
_SOURCEDEST = DESCRIPTOR.message_types_by_name['SourceDest']
_DISTANCE = DESCRIPTOR.message_types_by_name['Distance']
Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'distance_unary_pb2'
  })
_sym_db.RegisterMessage(Position)

SourceDest = _reflection.GeneratedProtocolMessageType('SourceDest', (_message.Message,), {
  'DESCRIPTOR' : _SOURCEDEST,
  '__module__' : 'distance_unary_pb2'
  })
_sym_db.RegisterMessage(SourceDest)

Distance = _reflection.GeneratedProtocolMessageType('Distance', (_message.Message,), {
  'DESCRIPTOR' : _DISTANCE,
  '__module__' : 'distance_unary_pb2'
  })
_sym_db.RegisterMessage(Distance)

_DISTANCESERVICE = DESCRIPTOR.services_by_name['DistanceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POSITION._serialized_start=24
  _POSITION._serialized_end=107
  _SOURCEDEST._serialized_start=109
  _SOURCEDEST._serialized_end=208
  _DISTANCE._serialized_start=210
  _DISTANCE._serialized_end=268
  _DISTANCESERVICE._serialized_start=270
  _DISTANCESERVICE._serialized_end=334
