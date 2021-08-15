#!/usr/bin/env python

#File for generating n_robot_list.launch

import xml.etree.cElementTree as ET

import sys

import random

if (len(sys.argv)<2):
    print('Usage: python3 generate_n_robots.py <number of robots>')
    sys.exit()

n = int(sys.argv[-1])



launch = ET.Element('launch')

ET.SubElement(launch,'arg',name='col_tolerance',default='0.5')

ET.SubElement(launch,'param',name='number_of_robots',value=str(n),type='int')
ET.SubElement(launch,'param',name='collision_tolerance',value='$(arg col_tolerance)',type='double')

ET.SubElement(launch,'arg',name='task_controller',default='one_robot_rwp.launch')

mid_point = (1+n)/2

for robot in range(1,n+1):
    #generating each robot
    robot_name_space = 'R' + str(robot)

    group = ET.SubElement(launch,'group',ns=robot_name_space)

    ET.SubElement(group,'param',name='tf_prefix',value=('robot'+str(robot)+'_tf'))

    robot_include = ET.SubElement(group,'include',file='$(find random_control)/launch/$(arg task_controller)')

    ET.SubElement(robot_include,'arg',name='id',value=str(robot))
    ET.SubElement(robot_include,'arg',name='robot_name',value=robot_name_space)
    ET.SubElement(robot_include,'arg',name='robot_model',value='waffle')
    ET.SubElement(robot_include,'arg',name='rnd_seed',value=str(random.randint(1,10000)))
    ET.SubElement(robot_include,'arg',name='yaw0',value=str(random.random()*2-1))
    ET.SubElement(robot_include,'arg',name='x0',value=str(robot-mid_point))
    ET.SubElement(robot_include,'arg',name='y0',value=str(robot-mid_point))





tree = ET.ElementTree(launch)
tree.write('n_robots_list.launch')