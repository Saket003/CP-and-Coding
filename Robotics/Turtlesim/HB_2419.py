#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		    HolA Bot (HB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of HolA Bot (KB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			HB_2419
# Author List:		Aditya Upadhyay, Saket Kandoi, Mohammad Faiz, Rishabh Barola
# Filename:			task_0.py
# Functions:
# 				callback, main
# Nodes:		    publishing node: '/turtle1/cmd_vel', subscriber node:'/turtle1/pose'


####################### IMPORT MODULES #######################
import sys, traceback, rospy, math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
##############################################################


def callback(msg):
	pass


def main():
	
	rospy.init_node('node_turtle_revolve', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel = Twist()
	pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, callback)
	global a,b,case, d, theta
	ti=rospy.Time.now().to_sec()
	curr_time = 0
	pi=math.pi
	while not rospy.is_shutdown():
		pub.publish(vel)
		
		if curr_time<=2*pi:
			a,b=factor,factor
			rospy.loginfo("My turtleBot is: Moving in circle!!")
		elif curr_time<=3*pi:
			a,b=0,factor
			rospy.loginfo("My turtleBot is: Rotating!")
		elif curr_time<3*pi + 4:
			a,b=factor,0
			rospy.loginfo("My turtleBot is: Moving straight!!!")
		else:
			vel.linear.x = 0
			pub.publish(vel)
			rospy.loginfo("Goal Reached")
			break
			
		vel.linear.x = a
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = b
		
		curr_time = rospy.Time.now().to_sec()-ti
		rate.sleep()

################# ADD GLOBAL VARIABLES HERE #################

factor = 0.5
a = factor	#linear
b = factor	#angular

##############################################################


################# ADD UTILITY FUNCTIONS HERE #################



##############################################################


######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS PART #########
if __name__ == "__main__":
    try:
        print("------------------------------------------")
        print("         Python Script Started!!          ")
        print("------------------------------------------")
        main()

    except:
        print("------------------------------------------")
        traceback.print_exc(file=sys.stdout)
        print("------------------------------------------")
        sys.exit()

    finally:
        print("------------------------------------------")
        print("    Python Script Executed Successfully   ")
        print("------------------------------------------")
