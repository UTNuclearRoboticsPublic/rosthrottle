import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('throttled_listener')

    rospy.Subscriber('chatter_throttle', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
