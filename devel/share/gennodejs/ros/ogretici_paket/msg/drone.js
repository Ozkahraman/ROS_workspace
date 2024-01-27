// Auto-generated. Do not edit!

// (in-package ogretici_paket.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class drone {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.hiz = null;
      this.isim = null;
      this.batarya = null;
    }
    else {
      if (initObj.hasOwnProperty('hiz')) {
        this.hiz = initObj.hiz
      }
      else {
        this.hiz = 0;
      }
      if (initObj.hasOwnProperty('isim')) {
        this.isim = initObj.isim
      }
      else {
        this.isim = '';
      }
      if (initObj.hasOwnProperty('batarya')) {
        this.batarya = initObj.batarya
      }
      else {
        this.batarya = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type drone
    // Serialize message field [hiz]
    bufferOffset = _serializer.int32(obj.hiz, buffer, bufferOffset);
    // Serialize message field [isim]
    bufferOffset = _serializer.string(obj.isim, buffer, bufferOffset);
    // Serialize message field [batarya]
    bufferOffset = _serializer.int32(obj.batarya, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type drone
    let len;
    let data = new drone(null);
    // Deserialize message field [hiz]
    data.hiz = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [isim]
    data.isim = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [batarya]
    data.batarya = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.isim.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ogretici_paket/drone';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ab3da279a675c6dfa18bb8afc332a0ab';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 hiz
    string isim
    int32 batarya
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new drone(null);
    if (msg.hiz !== undefined) {
      resolved.hiz = msg.hiz;
    }
    else {
      resolved.hiz = 0
    }

    if (msg.isim !== undefined) {
      resolved.isim = msg.isim;
    }
    else {
      resolved.isim = ''
    }

    if (msg.batarya !== undefined) {
      resolved.batarya = msg.batarya;
    }
    else {
      resolved.batarya = 0
    }

    return resolved;
    }
};

module.exports = drone;
