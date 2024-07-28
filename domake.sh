#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-wstool python3-rosdep ninja-build stow

cd catkin_ws
wstool init src
wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall
wstool update -t src

sudo rosdep init
rosdep update

cd src/cartographer
sed -i '/<depend>libabsl-dev<\/depend>/d' package.xml
cd ../../

rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
src/cartographer/scripts/install_abseil.sh
sudo apt-get remove ros-${ROS_DISTRO}-abseil-cpp

catkin_make_isolated

echo "Cartographer setup and build complete."
