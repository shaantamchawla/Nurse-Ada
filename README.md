How to run this project in your workspace

After cloning this repo into your workspace:

- cd into ros_workspaces / your_workspace
- Open up 4 terminal windows. In each, run: ./baxter.sh ada.local. 
  Then run the following:
    - 1st window:
        First, run: rosrun intera_interface enable_robot.py -e
        Second, in this same window, run: rosrun intera_interface joint_trajectory_action_server.py
    - 2nd window: roslaunch sawyer_moveit_config sawyer_moveit.launch electric_gripper:= true
    - 3rd window: rosrun segmentation image_segmentation.py sawyer
    - 4th window: rosrun planning path_test_ours.py sawyer
