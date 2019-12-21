# Install script for directory: /scratch/shared/baxter_ws/src/intera_common/intera_core_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/scratch/shared/baxter_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_core_msgs/msg" TYPE FILE FILES
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/NavigatorStates.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/SEAJointState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/CollisionAvoidanceState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/NavigatorStates.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/HeadState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/AnalogIOStates.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/CameraControl.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/AnalogOutputCommand.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/EndpointNamesArray.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/EndpointState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/DigitalIOStates.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/HeadPanCommand.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/AnalogIOState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/DigitalOutputCommand.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/AssemblyStates.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/CameraSettings.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/AssemblyState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/NavigatorState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/JointCommand.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/JointLimits.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/NavigatorState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/EndpointStates.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/DigitalIOState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/CollisionDetectionState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/HomingCommand.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/HomingState.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IOComponentCommand.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IOComponentConfiguration.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IOComponentStatus.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IODataStatus.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IODeviceConfiguration.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IODeviceStatus.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IONodeConfiguration.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IOStatus.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/IONodeStatus.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/URDFConfiguration.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/InteractionControlCommand.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/msg/InteractionControlState.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_core_msgs/srv" TYPE FILE FILES
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/srv/SolvePositionIK.srv"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/srv/SolvePositionFK.srv"
    "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/srv/IOComponentCommandSrv.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_core_msgs/action" TYPE FILE FILES "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/action/CalibrationCommand.action")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_core_msgs/msg" TYPE FILE FILES
    "/scratch/shared/baxter_ws/devel/share/intera_core_msgs/msg/CalibrationCommandAction.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_core_msgs/msg/CalibrationCommandActionGoal.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_core_msgs/msg/CalibrationCommandActionResult.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_core_msgs/msg/CalibrationCommandActionFeedback.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_core_msgs/msg/CalibrationCommandGoal.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_core_msgs/msg/CalibrationCommandResult.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_core_msgs/msg/CalibrationCommandFeedback.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_core_msgs/cmake" TYPE FILE FILES "/scratch/shared/baxter_ws/build/intera_common/intera_core_msgs/catkin_generated/installspace/intera_core_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/include/intera_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/share/roseus/ros/intera_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/share/common-lisp/ros/intera_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/share/gennodejs/ros/intera_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/scratch/shared/baxter_ws/devel/lib/python2.7/dist-packages/intera_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/lib/python2.7/dist-packages/intera_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/scratch/shared/baxter_ws/build/intera_common/intera_core_msgs/catkin_generated/installspace/intera_core_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_core_msgs/cmake" TYPE FILE FILES "/scratch/shared/baxter_ws/build/intera_common/intera_core_msgs/catkin_generated/installspace/intera_core_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_core_msgs/cmake" TYPE FILE FILES
    "/scratch/shared/baxter_ws/build/intera_common/intera_core_msgs/catkin_generated/installspace/intera_core_msgsConfig.cmake"
    "/scratch/shared/baxter_ws/build/intera_common/intera_core_msgs/catkin_generated/installspace/intera_core_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_core_msgs" TYPE FILE FILES "/scratch/shared/baxter_ws/src/intera_common/intera_core_msgs/package.xml")
endif()

