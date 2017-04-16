// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class MotorCommand {
  constructor() {
    this.joint_name = '';
    this.position = 0.0;
    this.speed = 0.0;
    this.acceleration = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type MotorCommand
    // Serialize message field [joint_name]
    bufferInfo = _serializer.string(obj.joint_name, bufferInfo);
    // Serialize message field [position]
    bufferInfo = _serializer.float64(obj.position, bufferInfo);
    // Serialize message field [speed]
    bufferInfo = _serializer.float32(obj.speed, bufferInfo);
    // Serialize message field [acceleration]
    bufferInfo = _serializer.float32(obj.acceleration, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type MotorCommand
    let tmp;
    let len;
    let data = new MotorCommand();
    // Deserialize message field [joint_name]
    tmp = _deserializer.string(buffer);
    data.joint_name = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [position]
    tmp = _deserializer.float64(buffer);
    data.position = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [speed]
    tmp = _deserializer.float32(buffer);
    data.speed = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [acceleration]
    tmp = _deserializer.float32(buffer);
    data.acceleration = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_pololu_servo/MotorCommand';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c357daac337dac3f7e4bb73a055e6e8c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string joint_name       # Name of the joint (specified in the yaml file), or motor_id for default calibration
    float64 position        # Position to move to in radians
    float32 speed           # Speed to move at (0.0 - 1.0)
    float32 acceleration    # Acceleration to move at (0.0 - 1.0)
    
    `;
  }

};

module.exports = MotorCommand;
