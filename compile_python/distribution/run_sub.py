from gps_subscriber import gps_subscriber
import rospy

rospy.init_node("gps_subscriber")
sub = gps_subscriber("/gps/fix")