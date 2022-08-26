from gps_publisher import gps_publisher
import rospy

rospy.init_node("gps_publisher")
gps_pub = gps_publisher("/gps/fix")
gps_pub.pub_msg()
