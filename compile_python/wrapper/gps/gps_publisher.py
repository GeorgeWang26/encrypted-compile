import rospy
from std_msgs.msg import String
import pynmea2
import serial


class gps_publisher():
    def __init__(self, topic_name):
        self.gps = serial.Serial("/dev/ttyACM0", baudrate = 9600, timeout = 0.5)
        self.rate = rospy.Rate(1)
        self.pub = rospy.Publisher(topic_name, String, queue_size = 1)

    def pub_msg(self):
        while not rospy.is_shutdown():
            s = self.gps.readlines()
            for i in range(len(s) - 1, -1, -1):
                gga = s[i].decode("utf-8")
                if gga[0:6] == "$GPGGA":
                    msg = pynmea2.parse(gga)
                    data = {"latitude": msg.latitude, "logitude": msg.longitude}
                    self.pub.publish(str(data))
                    break
            self.rate.sleep()


if __name__ == "__main__":
    rospy.init_node("gps_publisher")
    gps_pub = gps_publisher("/gps/fix")
    gps_pub.pub_msg()
