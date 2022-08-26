#cython: language_level=3

import rospy
import numpy as np

def hi():
    rospy.init_node("test")
    rospy.loginfo("im in")
    print("hello world")
    print(np.sin(1) * np.cos(1))

if __name__ == '__main__':
    hi()
