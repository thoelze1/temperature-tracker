const int sensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorVal = analogRead(sensorPin);
  //Serial.print("Sensor value: ");
  //Serial.print(sensorVal);
  
  float voltage = (sensorVal/1024.0) * 5.0;
  //Serial.print(", Volts: ");
  //Serial.print(voltage);

  float temperature = (voltage - 0.5) * 100.0;
  //Serial.print(", Celsius: ");
  //Serial.println(temperature);

  Serial.print("T: ");
  Serial.println(temperature);

  delay(1000);
}
