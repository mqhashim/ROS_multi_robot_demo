#!/usr/bin/env python
import rospy
# Import the Odometry message
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32

class Sensor():
    def __init__(self):

        rospy.init_node('sensor_controller',anonymous=False)

        print('sensor: start!')

        self.ns = rospy.get_namespace()
        print('sensor namespace:', rospy.get_namespace())
        
        self.position_sub = rospy.Subscriber(self.ns + 'sensor',Odometry, self.callback_sensor)
        
        self.sensor_data_pub = rospy.Publisher(self.ns + 'sensor_data',Float32,queue_size=5)

    def callback_sensor(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        data = x*x + y*y

        print('X: {:.2f}, Y: {:.2f}, Data: {:.2f}'.format(x,y,data))

        self.sensor_data_pub.publish(data)
    

if __name__ == '__main__':
    try:
        Sensor()
        # keep doing until ctrl-c
        while not rospy.is_shutdown():
            rospy.spin()
    except:
        rospy.loginfo('pose_monitor terminated')
