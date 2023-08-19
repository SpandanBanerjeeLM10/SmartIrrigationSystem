#include "DHT.h"

String command;

#define DHTPIN 2
#define DHTTYPE DHT11

// Sensor pins
#define moistSensorPwr 7
#define moistSensor1Val A0
#define moistSensor2Val A1

DHT dht(DHTPIN, DHTTYPE);

void setup() {
	pinMode(moistSensorPwr, OUTPUT);
	
	// Initially keep the sensor OFF
	digitalWrite(moistSensorPwr, LOW);
  dht.begin();
	
	Serial.begin(9600);
}

void loop() {
	//get the reading from the function below and print it
	Serial.print("Analog Moisture Value: ");
	Serial.println(readSensor());
	

  Serial.println();

  Serial.println("Temperature = " + String(dht.readTemperature())+" °C");
  Serial.println("Humidity = " + String(dht.readHumidity())+" %");

  delay(2000);


}

//  This function returns the analog soil moisture measurement
int readSensor() {
	digitalWrite(moistSensorPwr, HIGH);	// Turn the sensor ON
	delay(10);							// Allow power to settle
	int val = analogRead(moistSensorVal);	// Read the analog value form sensor
	digitalWrite(moistSensorPwr, LOW);		// Turn the sensor OFF
	return val;							// Return analog moisture value
}
