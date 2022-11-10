#!/usr/bin/env python3

import rospy

# publishing to /cmd_vel with msg type: Twist
from geometry_msgs.msg import Twist, PoseArray
# subscribing to /odom with msg type: Odometry
from nav_msgs.msg import Odometry

import math

# Odometry is given as a quaternion, but for the controller we'll need to find the orientaion theta by converting to euler angle
from tf.transformations import euler_from_quaternion


hola_x = 0
hola_y = 0
hola_theta = 0
x_goals = []
y_goals = []
theta_goals = []

def odometryCb(msg):
	global hola_x, hola_y, hola_theta
	position=msg.pose.pose.position
	o=msg.pose.pose.orientation

	quaternion=[ o.x, o.y, o.z, o.w ]
	hola_x, hola_y= position.x, position.y

	hola_theta=euler_from_quaternion(quaternion)[2]

def task1_goals_Cb(msg):
	global x_goals, y_goals, theta_goals

	x_goals.clear()
	y_goals.clear()
	theta_goals.clear()

	for waypoint_pose in msg.poses:
		x_goals.append(waypoint_pose.position.x)
		y_goals.append(waypoint_pose.position.y)

		orientation_q = waypoint_pose.orientation
		orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
		theta_goal = euler_from_quaternion (orientation_list)[2]
		theta_goals.append(theta_goal)

#Helper functions:
def sgn(x):
	if x>=0:
		return 1
	else:
		return -1

def rotate(theta, vel, pub):
	global hola_theta
	theta_err = theta-hola_theta
	vel.angular.z = min(abs(theta_err), 1) * sgn(theta_err)
	while abs(theta_err)>0.03:
		theta_err=theta-hola_theta
		vel.linear.x, vel.linear.y = 0, 0
		vel.angular.z = min(abs(theta_err), 1) * sgn(theta_err)
		
		print("vel.linear.x: ", vel.linear.x, "vel.linear.y: ", vel.linear.y, "vel.angular.z: ", vel.angular.z)
		print("hola_x: ", hola_x, "hola_y: ", hola_y, "hola_theta: ", hola_theta)
		print(x_d, y_d, theta_d)

		pub.publish(vel)
		rate.sleep()

	vel.angular.z=0
	pub.publish(vel)
	return

#Main
def main():
	rospy.init_node('controller',anonymous=True)

	pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
	rospy.Subscriber('/odom', Odometry, odometryCb)
	# declare that the node subscribes to task1_goals along with the other declarations of publishing and subscribing
	rospy.Subscriber('task1_goals', PoseArray, task1_goals_Cb)

	vel = Twist()

	rate = rospy.Rate(100)
	pi=3.1415926536

	

	#Control LOOOOOOP
	i=0
	while not rospy.is_shutdown():
		while i<len(x_goals):
			x_d, y_d, theta_d = x_goals[i], y_goals[i], theta_goals[i]

			if abs(x_d)<0.01:
				if x_d>=0:
					x_d=-0.01
				else:
					x_d=0.01
			if abs(y_d)<0.01:
				if y_d>=0:
					y_d=-0.01
				else:
					y_d=0.01

			while not rospy.is_shutdown():
				x_err = x_d - hola_x
				y_err = y_d - hola_y
				theta_err = theta_d - hola_theta

				vx = min( max(1, abs(x_err)) ,5) * sgn(x_err)
				vy = min( max(1, abs(y_err)) ,5) * sgn(y_err)
				vel.linear.x, vel.linear.y = vx*math.cos(hola_theta) + vy*math.sin(hola_theta), -vx*math.sin(hola_theta) + vy*math.cos(hola_theta)
				vel.angular.z = min( max(1, abs(theta_err)) ,5) * sgn(theta_err)
				
				pub.publish(vel)
				rate.sleep()
				print("vel.linear.x: ", vel.linear.x, "vel.linear.y: ", vel.linear.y, "vel.angular.z: ", vel.angular.z)
				print("hola_x: ", hola_x, "hola_y: ", hola_y, "hola_theta: ", hola_theta)
				print(x_d, y_d, theta_d)

				if(abs(x_err) < 0.03 and abs(y_err) < 0.03 and abs(theta_err) < 0.03):
					vel.linear.x, vel.linear.y, vel.angular.z = 0, 0, 0
					print("Goal Reached")
					pub.publish(vel)
					break
			rospy.sleep(2.)
			i+=1


if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass