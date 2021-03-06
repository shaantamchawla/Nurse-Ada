// Auto-generated. Do not edit!

// (in-package intera_motion_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let TrajectoryAnalysis = require('./TrajectoryAnalysis.js');

//-----------------------------------------------------------

class MotionCommandResult {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
      this.errorId = null;
      this.trajectory_analysis = null;
      this.last_successful_waypoint = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = false;
      }
      if (initObj.hasOwnProperty('errorId')) {
        this.errorId = initObj.errorId
      }
      else {
        this.errorId = '';
      }
      if (initObj.hasOwnProperty('trajectory_analysis')) {
        this.trajectory_analysis = initObj.trajectory_analysis
      }
      else {
        this.trajectory_analysis = new TrajectoryAnalysis();
      }
      if (initObj.hasOwnProperty('last_successful_waypoint')) {
        this.last_successful_waypoint = initObj.last_successful_waypoint
      }
      else {
        this.last_successful_waypoint = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotionCommandResult
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    // Serialize message field [errorId]
    bufferOffset = _serializer.string(obj.errorId, buffer, bufferOffset);
    // Serialize message field [trajectory_analysis]
    bufferOffset = TrajectoryAnalysis.serialize(obj.trajectory_analysis, buffer, bufferOffset);
    // Serialize message field [last_successful_waypoint]
    bufferOffset = _serializer.int32(obj.last_successful_waypoint, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotionCommandResult
    let len;
    let data = new MotionCommandResult(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [errorId]
    data.errorId = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [trajectory_analysis]
    data.trajectory_analysis = TrajectoryAnalysis.deserialize(buffer, bufferOffset);
    // Deserialize message field [last_successful_waypoint]
    data.last_successful_waypoint = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.errorId.length;
    length += TrajectoryAnalysis.getMessageSize(object.trajectory_analysis);
    return length + 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'intera_motion_msgs/MotionCommandResult';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0f7a03b4d34d1c7f003ca02ce0099e3c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # result
    bool result
    string errorId
    TrajectoryAnalysis trajectory_analysis
    
    int32 last_successful_waypoint
    int32 HAVE_NOT_REACHED_FIRST_WAYPOINT=-1
    int32 GENERAL_TRAJECTORY_FAILURE=-2
    
    
    ================================================================================
    MSG: intera_motion_msgs/TrajectoryAnalysis
    # The duration of the reference trajectory, as originally planned
    float64 planned_duration
    
    # The measured duration of the trajectory, as executed
    float64 measured_duration
    
    # Minimum commanded angle during trajectory for each joint
    float64[] min_angle_command
    
    # Maximum commanded angle during trajectory for each joint
    float64[] max_angle_command
    
    # Peak speed command = max(abs(reference velocity)) for each joint
    float64[] peak_speed_command
    
    # Peak accel command = max(abs(reference acceleration)) for each joint
    float64[] peak_accel_command
    
    # Peak jerk command = max(abs(reference jerk)) for each joint
    float64[] peak_jerk_command
    
    # Minimum trajectory time rate observed
    float64 min_time_rate
    
    # Maximium trajectory time rate observed
    float64 max_time_rate
    
    # Max joint position error = max(abs(position error)) for each joint
    float64[] max_position_error
    
    # Max joint velocity error = max(abs(velocity error)) for each joint
    float64[] max_velocity_error
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MotionCommandResult(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = false
    }

    if (msg.errorId !== undefined) {
      resolved.errorId = msg.errorId;
    }
    else {
      resolved.errorId = ''
    }

    if (msg.trajectory_analysis !== undefined) {
      resolved.trajectory_analysis = TrajectoryAnalysis.Resolve(msg.trajectory_analysis)
    }
    else {
      resolved.trajectory_analysis = new TrajectoryAnalysis()
    }

    if (msg.last_successful_waypoint !== undefined) {
      resolved.last_successful_waypoint = msg.last_successful_waypoint;
    }
    else {
      resolved.last_successful_waypoint = 0
    }

    return resolved;
    }
};

// Constants for message
MotionCommandResult.Constants = {
  HAVE_NOT_REACHED_FIRST_WAYPOINT: -1,
  GENERAL_TRAJECTORY_FAILURE: -2,
}

module.exports = MotionCommandResult;
