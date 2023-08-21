import serial
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.emqx.io", 1883, 60)

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            #print(f"Read from serial: {line}")
            client.publish('topic/sensorModule', payload=line, qos=0, retain=False)
            print(f"Published to topic/sensorModule: {line}")
            print("\n")


if __name__ == '__main__':
    main()
