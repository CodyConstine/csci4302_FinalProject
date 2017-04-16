// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let MotorState = require('./MotorState.js');

//-----------------------------------------------------------

class MotorStateList {
  constructor() {
    this.motor_states = [];
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type MotorStateList
    // Serialize the length for message field [motor_states]
    bufferInfo = _serializer.uint32(obj.motor_states.length, bufferInfo);
    // Serialize message field [motor_states]
    obj.motor_states.forEach((val) => {
      bufferInfo = MotorState.serialize(val, bufferInfo);
    });
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type MotorStateList
    let tmp;
    let len;
    let data = new MotorStateList();
    // Deserialize array length for message field [motor_states]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [motor_states]
    data.motor_states = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = MotorState.deserialize(buffer);
      data.motor_states[i] = tmp.data;
      buffer = tmp.buffer;
    }
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_pololu_servo/MotorStateList';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f59501f919a1edaba3d8a1c194971202';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    ros_pololu_servo/MotorState[] motor_states
    
    ================================================================================
    MSG: ros_pololu_servo/MotorState
    string name                                     # Name of the servo (specified in the yaml file)
    int8 pololu_id                                  # id of the Pololu board (12 by default)
    int8 motor_id                                   # id of the servo on the Pololu board
    int32 pulse                                     # Pwm servo pulse
    float64 radians                                 # Current position of the servo in radians
    float64 degrees                                 # Current position of the servo in degrees
    ros_pololu_servo/MotorCalibration calibration   # Servo calibration
    ================================================================================
    MSG: ros_pololu_servo/MotorCalibration
    int32 min_pulse             # Minimum pwm pulse
    float64 min_radians         # Radians corresponding to min pwm pulse
    float64 min_degrees         # Degrees corresponding to min pwm pulse
    int32 max_pulse             # Maximum pwm pulse
    float64 max_radians         # Radians corresponding to max pwm pulse
    float64 max_degrees         # Degrees corresponding to max pwm pulse
    `;
  }

};

module.exports = MotorStateList;
