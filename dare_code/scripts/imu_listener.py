#!/usr/bin/env python3
"""
imu_listener.py

ROS node that enhances robot's awareness by processing IMU data.
It listens to IMU data, republishes it with the correct frame_id, and broadcasts this information.
This enables the robot to adjust its actions based on how it is oriented in its environment.
"""
import rospy
from sensor_msgs.msg import Imu
import tf
from tf.transformations import quaternion_from_euler, euler_from_quaternion

def imu_callback(data):
    # Update frame_id directly
    data.header.frame_id = 'imu_link'
    imu_pub.publish(data)

    rospy.loginfo("Re-publishing IMU data with frame_id set to 'imu_link'.")

    # Broadcast transform from base_link to imu_link
    orientation_q = data.orientation
    br.sendTransform((0, 0, 0),
                     (orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w),
                     rospy.Time.now(),
                     "base_link",
                     "imu_link")

    # Optional: log roll, pitch, yaw for debugging
    euler = euler_from_quaternion([orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w])
    rospy.loginfo("IMU data: Roll: %f, Pitch: %f, Yaw: %f", euler[0], euler[1], euler[2])

def imu_listener():
    rospy.init_node('imu_listener', anonymous=True)
    global br, imu_pub
    br = tf.TransformBroadcaster()
    imu_pub = rospy.Publisher('/imu_corrected', Imu, queue_size=10)
    rospy.Subscriber('/imu', Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        imu_listener()
    except rospy.ROSInterruptException:
        pass
