// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class MotorCalibration {
  constructor() {
    this.min_pulse = 0;
    this.min_radians = 0.0;
    this.min_degrees = 0.0;
    this.max_pulse = 0;
    this.max_radians = 0.0;
    this.max_degrees = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type MotorCalibration
    // Serialize message field [min_pulse]
    bufferInfo = _serializer.int32(obj.min_pulse, bufferInfo);
    // Serialize message field [min_radians]
    bufferInfo = _serializer.float64(obj.min_radians, bufferInfo);
    // Serialize message field [min_degrees]
    bufferInfo = _serializer.float64(obj.min_degrees, bufferInfo);
    // Serialize message field [max_pulse]
    bufferInfo = _serializer.int32(obj.max_pulse, bufferInfo);
    // Serialize message field [max_radians]
    bufferInfo = _serializer.float64(obj.max_radians, bufferInfo);
    // Serialize message field [max_degrees]
    bufferInfo = _serializer.float64(obj.max_degrees, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type MotorCalibration
    let tmp;
    let len;
    let data = new MotorCalibration();
    // Deserialize message field [min_pulse]
    tmp = _deserializer.int32(buffer);
    data.min_pulse = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [min_radians]
    tmp = _deserializer.float64(buffer);
    data.min_radians = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [min_degrees]
    tmp = _deserializer.float64(buffer);
    data.min_degrees = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [max_pulse]
    tmp = _deserializer.int32(buffer);
    data.max_pulse = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [max_radians]
    tmp = _deserializer.float64(buffer);
    data.max_radians = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [max_degrees]
    tmp = _deserializer.float64(buffer);
    data.max_degrees = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_pololu_servo/MotorCalibration';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '243cff09419a3549991196c6e5684b74';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 min_pulse             # Minimum pwm pulse
    float64 min_radians         # Radians corresponding to min pwm pulse
    float64 min_degrees         # Degrees corresponding to min pwm pulse
    int32 max_pulse             # Maximum pwm pulse
    float64 max_radians         # Radians corresponding to max pwm pulse
    float64 max_degrees         # Degrees corresponding to max pwm pulse
    `;
  }

};

module.exports = MotorCalibration;
