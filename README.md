# Ground_Control_ROS
Contains the essential packages for post-processing of the bagfile data after the expedition. This will run on a laptop or home computer, to visualize the cave data.

### Getting started

1. Clone this repo in the home directory `~/`

2. Change directory to the root of the cloned repo, so that your working directory in the terminal looks like this:
`~/Ground_Control_ROS`

3. Create cartographer workspace directory
`mkdir catkin_ws`

4. Change permission of shell scripts:
`chmod +x domake.sh`
`chmod +x docopy.sh`

5. Run the scripts in order:
`./domake.sh`
`./docopy.sh`

6. source the devel_isolated/setup.bash script within your basrc file
`nano ~/.bashrc` -> scroll all the way down and paste this command -> `source ~/Ground_Controls_ROS/catkin_ws/devel_isolated/setup.bash`
   
8. To test if everything worked, run the following, an rviz window should appear:
`roslaunch cartographer_ros cartographer.launch`
