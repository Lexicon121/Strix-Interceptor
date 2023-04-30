import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, SetMode
from nav_msgs.msg import Path
from std_msgs.msg import String

class StrixSwarmNode:
    def __init__(self):
        # Initialize ROS node and subscribers/publishers
        rospy.init_node('strix_swarm_node')
        self.state_sub = rospy.Subscriber('/mavros/state', State, self.state_callback)
        self.goal_sub = rospy.Subscriber('/strix_swarm/goal', PoseStamped, self.goal_callback)
        self.mode_service = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        self.arm_service = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        self.path_pub = rospy.Publisher('/strix_swarm/path', Path, queue_size=10)
        self.status_pub = rospy.Publisher('/strix_swarm/status', String, queue_size=10)

        # Set initial state variables
        self.current_state = State()
        self.current_goal = PoseStamped()
        self.is_armed = False
        self.current_mode = 'OFFBOARD'

    def state_callback(self, state):
        self.current_state = state

    def goal_callback(self, goal):
        self.current_goal = goal

    def set_mode(self, mode):
        rospy.loginfo('Setting mode: %s', mode)
        response = self.mode_service(0, mode)
        return response.mode_sent

    def arm(self):
        rospy.loginfo('Arming...')
        response = self.arm_service(True)
        return response.success

    def run(self):
        # Main loop
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            # Check if we're armed and in the correct mode
            if not self.is_armed and self.current_state.mode != self.current_mode:
                self.set_mode(self.current_mode)

            if not self.is_armed and self.current_state.mode == self.current_mode:
                self.arm()

            # Publish the current goal and status
            self.path_pub.publish(self.current_goal)
            self.status_pub.publish('Flying to goal...')

            # Wait for the next iteration
            rate.sleep()

if __name__ == '__main__':
    node = StrixSwarmNode()
    node.run()
