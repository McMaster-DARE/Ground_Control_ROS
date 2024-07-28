#!/bin/bash

SOURCE_DIR="$HOME/Ground_Control_ROS/dare_code/"
DEST_DIR="$HOME/Ground_Control_ROS/cart_ws/src/cartographer_ros/cartographer_ros/"


rsync -av --progress "${SOURCE_DIR}configuration_files/" "${DEST_DIR}configuration_files/"
rsync -av --progress "${SOURCE_DIR}launch/" "${DEST_DIR}launch/"
rsync -av --progress "${SOURCE_DIR}robot_description/" "${DEST_DIR}robot_description/"
rsync -av --progress "${SOURCE_DIR}rosbag/" "${DEST_DIR}rosbag/"
rsync -av --progress "${SOURCE_DIR}scripts/" "${DEST_DIR}scripts/"

echo "Files have been copied successfully."
