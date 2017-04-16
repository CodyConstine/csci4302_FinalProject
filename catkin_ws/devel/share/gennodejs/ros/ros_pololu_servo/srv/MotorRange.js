// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class MotorRangeRequest {
  constructor() {
    this.motor_name = '';
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type MotorRangeRequest
    // Serialize message field [motor_name]
    bufferInfo = _serializer.string(obj.motor_name, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type MotorRangeRequest
    let tmp;
    let len;
    let data = new MotorRangeRequest();
    // Deserialize message field [motor_name]
    tmp = _deserializer.string(buffer);
    data.motor_name = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_pololu_servo/MotorRangeRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ea6f8ac7c07fc33a72a46dab1cefc8d1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string motor_name
    
    `;
  }

};

class MotorRangeResponse {
  constructor() {
    this.min = 0.0;
    this.max = 0.0;
    this.direction = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type MotorRangeResponse
    // Serialize message field [min]
    bufferInfo = _serializer.float32(obj.min, bufferInfo);
    // Serialize message field [max]
    bufferInfo = _serializer.float32(obj.max, bufferInfo);
    // Serialize message field [direction]
    bufferInfo = _serializer.float32(obj.direction, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type MotorRangeResponse
    let tmp;
    let len;
    let data = new MotorRangeResponse();
    // Deserialize message field [min]
    tmp = _deserializer.float32(buffer);
    data.min = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [max]
    tmp = _deserializer.float32(buffer);
    data.max = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [direction]
    tmp = _deserializer.float32(buffer);
    data.direction = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_pololu_servo/MotorRangeResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5892eecaa7e34e1c77e0bea237d5e235';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 min
    float32 max
    float32 direction
    
    `;
  }

};

module.exports = {
  Request: MotorRangeRequest,
  Response: MotorRangeResponse
};
