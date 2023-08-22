# SMART IRRIGATION SYSTEM USING MQTT PROTOCOL
A full-stack IoT Smart Irrigation System using Raspberry Pi (Decision Hub), Arduino Uno (Sensor Hub), and MQTT Protocol (Communication).

# Hardware Setup

![Hardware Setup](https://github.com/SpandanBanerjeeLM10/SmartIrrigationSystem/assets/40685462/dda412ce-7583-4f2c-b9c4-6c98e8cbbc70)

The hardware setup showcases the physical components and sensors used in the system. These components work in tandem to collect data and control the irrigation process. 
Arduino Uno is central to the sensor hub, all the sensors are connected to the Arduino where data is collected and transmitted serially using USB to Raspberry Pi. 
Raspberry Pi is central to the decision hub, where the data is processed and the decision is made regarding watering the plant.
MQTT protocol is used to control the water pump, a subscriber application constantly reads the moisture values published by the Pi and switches on/off the pump.

# Software Setup

![Software Setup](https://github.com/SpandanBanerjeeLM10/SmartIrrigationSystem/assets/40685462/90becf69-7bb6-44b5-b974-bc867c61c159)

The software setup provides a glimpse into the backend and frontend interfaces. It plays a crucial role in processing the data from the hardware components and making informed decisions.

# Test Setup with LED (LED being the pump)

![LED setup](https://github.com/SpandanBanerjeeLM10/SmartIrrigationSystem/assets/40685462/5512c50c-8cdd-4953-b335-6815c1fd9486)


# Complete Physical Setup 

![Full Physical Setup](https://github.com/SpandanBanerjeeLM10/SmartIrrigationSystem/assets/40685462/555c73bd-4b67-4a11-a6e6-1d8820c1716c)
