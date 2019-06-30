# BeagleBone-Blue

BeagleBone® Blue is an all-in-one Linux-based computer for robotics, integrating onto a single small (3.5" x 2.15") board the Octavo OSD3358 microprocessor together with wifi/bluetooth, IMU/barometer, power regulation and state-of-charge LEDs for a 2-cell LiPo, H-Bridges, and discrete connectors for 4 DC motors+encoders, 8 servos, and all of the commonly-needed buses for additional peripherals in embedded applications. 

## Repository Contents

**Bringup**   - Consist of Instructions to setup the BeagleBone Blue and Connect it to a Wifi 

**Datasheet** - Consist of the Datasheet of BeagleBone Blue and it Diagram discribing its various features 

**Scripts**   - This folder has python programs

## Scripts 

There are presently 3 Programs, the Bluetooth_Publisher_Ros.py and Motor_Test_GPIO.py , Bluetooth_BeagleBone_Blue.py.

To Run **Bluetooth_Publisher_Ros.py** , ROS has to be installed on the Board this program recieves the data throgh a mobile App ( Say: Blueterm), and then publishes this data as a ROS topic.

The **Motor_Test_GPIO.py** , enables you to control the motor through an external motor driver and GPIO pins on BeagleBone Blue

The **Bluetooth_BeagleBone_Blue.py**, just recieves the data from Blueterm and prints the recieved data (Ros is not necessary for this program).


