// Auto-generated. Do not edit!

// (in-package basit_uygulamalar.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class CemberHaraketRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.yaricap = null;
    }
    else {
      if (initObj.hasOwnProperty('yaricap')) {
        this.yaricap = initObj.yaricap
      }
      else {
        this.yaricap = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CemberHaraketRequest
    // Serialize message field [yaricap]
    bufferOffset = _serializer.float64(obj.yaricap, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CemberHaraketRequest
    let len;
    let data = new CemberHaraketRequest(null);
    // Deserialize message field [yaricap]
    data.yaricap = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'basit_uygulamalar/CemberHaraketRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '534fdc954659adaf837ecd56d547676d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 yaricap
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CemberHaraketRequest(null);
    if (msg.yaricap !== undefined) {
      resolved.yaricap = msg.yaricap;
    }
    else {
      resolved.yaricap = 0.0
    }

    return resolved;
    }
};

class CemberHaraketResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CemberHaraketResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CemberHaraketResponse
    let len;
    let data = new CemberHaraketResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'basit_uygulamalar/CemberHaraketResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CemberHaraketResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: CemberHaraketRequest,
  Response: CemberHaraketResponse,
  md5sum() { return '534fdc954659adaf837ecd56d547676d'; },
  datatype() { return 'basit_uygulamalar/CemberHaraket'; }
};
