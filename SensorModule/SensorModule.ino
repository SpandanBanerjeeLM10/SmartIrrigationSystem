#include "DHT.h"

String command;

#define DHTPIN 2
#define DHTTYPE DHT11


//Sensor Pins
#define sensor1 A0
#define sensor2 A1

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  dht.begin();
  Serial.begin(9600);

}

void loop() {
  //read sensor 1
  int sensor1Value = analogRead(sensor1);
  Serial.print("Sensor 1: ");
  Serial.println(sensor1Value);
  
  //read sensor 2
  int sensor2Value = analogRead(sensor2);
  Serial.print("Sensor 2: ");
  Serial.println(sensor2Value);
  
  Serial.println();

  Serial.println("Temperature = " + String(dht.readTemperature())+" °C");
  Serial.println("Humidity = " + String(dht.readHumidity())+" %");

  delay(3000);

}
