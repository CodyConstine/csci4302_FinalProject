// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let MotorCalibration = require('./MotorCalibration.js');

//-----------------------------------------------------------

class MotorState {
  constructor() {
    this.name = '';
    this.pololu_id = 0;
    this.motor_id = 0;
    this.pulse = 0;
    this.radians = 0.0;
    this.degrees = 0.0;
    this.calibration = new MotorCalibration();
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type MotorState
    // Serialize message field [name]
    bufferInfo = _serializer.string(obj.name, bufferInfo);
    // Serialize message field [pololu_id]
    bufferInfo = _serializer.int8(obj.pololu_id, bufferInfo);
    // Serialize message field [motor_id]
    bufferInfo = _serializer.int8(obj.motor_id, bufferInfo);
    // Serialize message field [pulse]
    bufferInfo = _serializer.int32(obj.pulse, bufferInfo);
    // Serialize message field [radians]
    bufferInfo = _serializer.float64(obj.radians, bufferInfo);
    // Serialize message field [degrees]
    bufferInfo = _serializer.float64(obj.degrees, bufferInfo);
    // Serialize message field [calibration]
    bufferInfo = MotorCalibration.serialize(obj.calibration, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type MotorState
    let tmp;
    let len;
    let data = new MotorState();
    // Deserialize message field [name]
    tmp = _deserializer.string(buffer);
    data.name = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [pololu_id]
    tmp = _deserializer.int8(buffer);
    data.pololu_id = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [motor_id]
    tmp = _deserializer.int8(buffer);
    data.motor_id = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [pulse]
    tmp = _deserializer.int32(buffer);
    data.pulse = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [radians]
    tmp = _deserializer.float64(buffer);
    data.radians = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [degrees]
    tmp = _deserializer.float64(buffer);
    data.degrees = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [calibration]
    tmp = MotorCalibration.deserialize(buffer);
    data.calibration = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_pololu_servo/MotorState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f1e998b21e02fc23ab5efad21cbedab1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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

module.exports = MotorState;
