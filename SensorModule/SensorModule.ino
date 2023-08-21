#include "DHT.h"

String command;

#define DHTPIN 2
#define DHTTYPE DHT11


//Sensor Pins
#define sensor1 A0
#define sensor2 A1

const int pumpPin = 8;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  dht.begin();
  Serial.begin(9600);

}

void loop() {
  //read sensor 1
  int sensor1Value = analogRead(sensor1);
     
  //read sensor 2
  int sensor2Value = analogRead(sensor2);
  
  //Calc the average
  int avgSensorValue = (sensor1Value + sensor2Value)/2;

  Serial.println("Average Moisture Content = " + String(avgSensorValue));
  Serial.println("Temperature = " + String(dht.readTemperature())+" °C");
  Serial.println("Humidity = " + String(dht.readHumidity())+" %");

  
  delay(3000);

}
