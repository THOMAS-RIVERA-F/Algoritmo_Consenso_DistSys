# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: raft.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'raft.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\"*\n\x0cWriteMessage\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\" \n\rWriteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1a\n\x0bReadMessage\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1d\n\x0cReadResponse\x12\r\n\x05value\x18\x01 \x01(\t\"4\n\x08LogEntry\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"!\n\x0e\x41ppendResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x95\x01\n\x0bRaftService\x12-\n\x0cWriteRequest\x12\r.WriteMessage\x1a\x0e.WriteResponse\x12*\n\x0bReadRequest\x12\x0c.ReadMessage\x1a\r.ReadResponse\x12+\n\rAppendEntries\x12\t.LogEntry\x1a\x0f.AppendResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WRITEMESSAGE']._serialized_start=14
  _globals['_WRITEMESSAGE']._serialized_end=56
  _globals['_WRITERESPONSE']._serialized_start=58
  _globals['_WRITERESPONSE']._serialized_end=90
  _globals['_READMESSAGE']._serialized_start=92
  _globals['_READMESSAGE']._serialized_end=118
  _globals['_READRESPONSE']._serialized_start=120
  _globals['_READRESPONSE']._serialized_end=149
  _globals['_LOGENTRY']._serialized_start=151
  _globals['_LOGENTRY']._serialized_end=203
  _globals['_APPENDRESPONSE']._serialized_start=205
  _globals['_APPENDRESPONSE']._serialized_end=238
  _globals['_RAFTSERVICE']._serialized_start=241
  _globals['_RAFTSERVICE']._serialized_end=390
# @@protoc_insertion_point(module_scope)
