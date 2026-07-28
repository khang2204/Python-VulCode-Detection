""" Navigation and localization
    
Author:
    Annaleah Ernst
"""
import tf
import rospy
import numpy as np
from copy import deepcopy
from geometry_msgs.msg import Pose, Point, Quaternion
from math import sin, cos, pi
from time import time
from localization import Localization
from logger import Logger
from navigation import Navigation
""" Navigate and localize on a map.
    
    Args:
        point_ids (set): Unique identifier for each waypoint in the graph.
        locations (dict): Point_ids mapped to tuples representing locations.
        neighbors (dict): Point_ids mapped to lists containing other point_ids representing 
            the current node's neighbors.
        landmark_ids (set): Unique identifier for each landmark in the graph.
        landmark_positions (dict): Map AprilTag landmark ids to their absolute
            position on the floorplan.
        landmark_angles (dict): Map AprilTag landmark ids to their absolute
            position on the floorplan. This specifies the angle of rotation of the landmark in the 
            xy plane; ie, how much has its horizontal vector deviated from the x axis.
        jerky (bool, optional): If true, robot will not decelerate, but stop abruptly.
            Defaults to False.
        walking_speed (float, optional): Percentage of maximum speed, magnitude between 0 and 1.
                Values with magnitude greater than 1 will be ignored.
    
    Attributes:
        tags (geometry_msgs.msg.PoseStamped dict): A dict of all the AprilTags currently in view in 
            their raw form.
        tags_odom (geometry_msgs.msg.PoseStamped dict): Same as above, but in the odometry frame.
        floorplan (FloorPlan): The map of the current space as a floorplan.
        p (geometry_msgs.msg.Point): The position of the robot in the ekf odometry frame according to
            the robot_pose_ekf package.
        q (geometry_msgs.msg.Quaternion): The orientation of the robot in the ekf odometry frame
            according the the robot_pose_ekf package.
        angle (float): The angle (in radians) that the robot is from 0 in the ekf odometry frame. 
            Between -pi and pi
        map_pos (geometry_msgs.msg.Point): The position of the robot in the map frame.
        map_angle (float): The angle (in radians) of the robot in the map frame.
    """
def __init__(self, point_ids, locations, neighbors, landmark_ids,...
self.map_pos = Point()
self.map_angle = 0
self._path = None
Localization.__init__(self, point_ids, locations, neighbors, landmark_ids,
    landmark_positions, landmark_angles)
Navigation.__init__(self, jerky=jerky, walking_speed=walking_speed)
self._logger = Logger('NavLoc')
timer = time()
while time() - timer < 0.5:
def _ekfCallback(self, data):...
"""docstring"""
Navigation._ekfCallback(self, data)
self.map_pos = self.transformPoint(self.p, 'odom', 'map')
self.map_angle = self.transformAngle(self.angle, 'odom', 'map')
def _handleObstacle(self, turn_delta):...
"""docstring"""
if Navigation._handleObstacle(self, turn_delta):
self._path = None
return False
return True
