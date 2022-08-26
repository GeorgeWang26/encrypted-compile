import rospy

def hi():
    rospy.init_node("test")
    rospy.loginfo("im in")
    print("hello world")

if __name__ == '__main__':
    hi()
