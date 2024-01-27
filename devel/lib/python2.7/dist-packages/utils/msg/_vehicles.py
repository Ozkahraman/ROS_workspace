# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from utils/vehicles.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class vehicles(genpy.Message):
  _md5sum = "de73bb5b781774cb3107d20c52b302aa"
  _type = "utils/vehicles"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 ID
float32 timestamp
float32 posA
float32 posB
float32 rotA
float32 rotB"""
  __slots__ = ['ID','timestamp','posA','posB','rotA','rotB']
  _slot_types = ['uint8','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ID,timestamp,posA,posB,rotA,rotB

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(vehicles, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ID is None:
        self.ID = 0
      if self.timestamp is None:
        self.timestamp = 0.
      if self.posA is None:
        self.posA = 0.
      if self.posB is None:
        self.posB = 0.
      if self.rotA is None:
        self.rotA = 0.
      if self.rotB is None:
        self.rotB = 0.
    else:
      self.ID = 0
      self.timestamp = 0.
      self.posA = 0.
      self.posB = 0.
      self.rotA = 0.
      self.rotB = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B5f().pack(_x.ID, _x.timestamp, _x.posA, _x.posB, _x.rotA, _x.rotB))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 21
      (_x.ID, _x.timestamp, _x.posA, _x.posB, _x.rotA, _x.rotB,) = _get_struct_B5f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B5f().pack(_x.ID, _x.timestamp, _x.posA, _x.posB, _x.rotA, _x.rotB))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 21
      (_x.ID, _x.timestamp, _x.posA, _x.posB, _x.rotA, _x.rotB,) = _get_struct_B5f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B5f = None
def _get_struct_B5f():
    global _struct_B5f
    if _struct_B5f is None:
        _struct_B5f = struct.Struct("<B5f")
    return _struct_B5f