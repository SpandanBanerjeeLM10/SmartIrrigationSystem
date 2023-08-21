import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

# GPIO pins for the water pump
PUMP_PIN = 17

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.output(PUMP_PIN, GPIO.LOW)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("topic/sensorModule")

def extract_value(line):
    return line.split("=")[-1].strip()

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
   # print(f"{msg.topic} {payload}")

    if "Temperature" in payload:
        temperature = extract_value(payload)
        print(f"Temperature: {temperature}")
    if "Humidity" in payload:
        humidity = extract_value(payload)
        print(f"Humidity: {humidity}")
    if "Average Moisture Content" in payload:
        avg_moisture = int(extract_value(payload))
        print(f"Average Moisture Content: {avg_moisture}")
        if avg_moisture > 450:
            print("Starting water pump")
            GPIO.output(PUMP_PIN, GPIO.HIGH)
            print("\n")
        elif avg_moisture <= 380:
            print("Stopping water pump")
            GPIO.output(PUMP_PIN, GPIO.LOW)
            print("\n")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()
