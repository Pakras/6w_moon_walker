# 6w_moon_walker
dependencies

`sudo apt install ros-kinetic-effort-controllers`

`sudo chmod +x moon_controller/src/keyboard_control.py`

start world and launch ROKAD

`roslaunch moon main.launch` 

start plugin 

`roslaunch MYROBOT_control moon_control.launch`

start keyboard controll

`rosrun moon_controller keyboard_control.py`

"w"-forward

"x"-backward

"s"-stop

"a"-left

"d"-right

"f" and "r"- angle in mid

"t" and "g" distance between mid and forepart

"y" and "h" distance between mid and aftpart

spawn husky bot(http://wiki.ros.org/husky_gazebo/Tutorials/Simulating%20Husky)

`roslaunch husky_gazebo spawn_husky.launch


spawn hector_quadrotor(http://wiki.ros.org/hector_quadrotor)

`roslaunch hector_quadrotor_gazebo spawn_quadrotor.launch`

to send messages in topics

`rosservice call quad/enable_motors "enable: true"`

to control quadrotor use quad/cmd_vel topic

to control husky use /twist_marker_server/cmd_vel topic and get pose from /husky_velocity_controller/odom

to read data from quadrotor use /sonar_height/range and position from /quadrotor/ground_truth/state

to read pose of moon use /moon/odom



