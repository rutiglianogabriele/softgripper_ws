#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def change_gripper_status():
    pub = rospy.Publisher('gripper_command', Int32, queue_size=2)
    rospy.init_node('softgripper_control', anonymous=True)

        #rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        status = 1
        pub.publish(status)
        rospy.sleep(3.)
        status = 0
        pub.publish(status)
        rospy.sleep(3.)
    
if __name__ == '__main__':
    try:
        change_gripper_status()
    except rospy.ROSInterruptException:
        pass