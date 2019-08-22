# 6w_moon_walker
dependencies

`sudo apt install ros-kinetic-effort-controllers`

sudo chmod +x moon_controller/src/keyboard_control.py

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

`roslaunch moon husky.launch`

spawn hector_quadrotor(http://wiki.ros.org/hector_quadrotor)

`roslaunch moon quadrotor.launch`


