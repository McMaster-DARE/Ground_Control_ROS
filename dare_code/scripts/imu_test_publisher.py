# #!/usr/bin/env python3
# import rospy
# from sensor_msgs.msg import Imu

# def imu_callback(data):
#     data.header.frame_id = 'imu_link'  # Ensure this is set
#     pub.publish(data)

# if __name__ == '__main__':
    # rospy.init_node('imu_test_publisher')
    # pub = rospy.Publisher('/imu_corrected', Imu, queue_size=10)
    # rospy.Subscriber('/imu', Imu, imu_callback)
    # rospy.spin()
