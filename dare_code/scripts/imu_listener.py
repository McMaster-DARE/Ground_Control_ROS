#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
import tf
from tf.transformations import euler_from_quaternion

def imu_callback(data):
    # Check if the frame_id is already set correctly
    if data.header.frame_id != 'imu_link':
        data.header.frame_id = 'imu_link'
        imu_pub.publish(data)
        rospy.loginfo("Re-publishing IMU data with frame_id set to 'imu_link'.")
    else:
        rospy.loginfo("IMU data already has correct frame_id 'imu_link'.")

    orientation_q = data.orientation
    br.sendTransform((0, 0, 0),  
                     (orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w),
                     rospy.Time.now(),
                     "base_link",  
                     "world") 

def imu_listener():
    rospy.init_node('imu_listener', anonymous=True)
    global br, imu_pub
    br = tf.TransformBroadcaster()
    imu_pub = rospy.Publisher('/imu', Imu, queue_size=10)  # Republish on the same /imu topic
    rospy.Subscriber('/imu', Imu, imu_callback) 
    rospy.spin()

if __name__ == '__main__':
    try:
        imu_listener()
    except rospy.ROSInterruptException:
        pass
