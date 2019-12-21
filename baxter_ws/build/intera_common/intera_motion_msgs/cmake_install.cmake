# Install script for directory: /scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_motion_msgs/msg" TYPE FILE FILES
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/EndpointTrackingError.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/InterpolatedPath.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/JointTrackingError.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/MotionStatus.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/TrackingOptions.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/Trajectory.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/TrajectoryAnalysis.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/TrajectoryOptions.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/Waypoint.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/WaypointOptions.msg"
    "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/msg/WaypointSimple.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_motion_msgs/action" TYPE FILE FILES "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/action/MotionCommand.action")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_motion_msgs/msg" TYPE FILE FILES
    "/scratch/shared/baxter_ws/devel/share/intera_motion_msgs/msg/MotionCommandAction.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_motion_msgs/msg/MotionCommandActionGoal.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_motion_msgs/msg/MotionCommandActionResult.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_motion_msgs/msg/MotionCommandActionFeedback.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_motion_msgs/msg/MotionCommandGoal.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_motion_msgs/msg/MotionCommandResult.msg"
    "/scratch/shared/baxter_ws/devel/share/intera_motion_msgs/msg/MotionCommandFeedback.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_motion_msgs/cmake" TYPE FILE FILES "/scratch/shared/baxter_ws/build/intera_common/intera_motion_msgs/catkin_generated/installspace/intera_motion_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/include/intera_motion_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/share/roseus/ros/intera_motion_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/share/common-lisp/ros/intera_motion_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/share/gennodejs/ros/intera_motion_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/scratch/shared/baxter_ws/devel/lib/python2.7/dist-packages/intera_motion_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/scratch/shared/baxter_ws/devel/lib/python2.7/dist-packages/intera_motion_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/scratch/shared/baxter_ws/build/intera_common/intera_motion_msgs/catkin_generated/installspace/intera_motion_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_motion_msgs/cmake" TYPE FILE FILES "/scratch/shared/baxter_ws/build/intera_common/intera_motion_msgs/catkin_generated/installspace/intera_motion_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_motion_msgs/cmake" TYPE FILE FILES
    "/scratch/shared/baxter_ws/build/intera_common/intera_motion_msgs/catkin_generated/installspace/intera_motion_msgsConfig.cmake"
    "/scratch/shared/baxter_ws/build/intera_common/intera_motion_msgs/catkin_generated/installspace/intera_motion_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_motion_msgs" TYPE FILE FILES "/scratch/shared/baxter_ws/src/intera_common/intera_motion_msgs/package.xml")
endif()

