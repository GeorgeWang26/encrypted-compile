#cython: language_level = 3

import rospy
from std_msgs.msg import String


class gps_subscriber():
    def __init__(self, topic_name):
        self.sub = rospy.Subscriber(topic_name, String, lambda msg : print(msg.data))
        rospy.spin()


if __name__ == "__main__":
    rospy.init_node("gps_subscriber")
    sub = gps_subscriber("/gps/fix")
