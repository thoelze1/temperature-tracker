const int sensorPin = A0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int sensorVal = analogRead(sensorPin);
  
  float voltage = (sensorVal/1024.0) * 5.0;
  float celsius = (voltage - 0.5) * 100.0;
  float farenheit = (celsius * 9.0/5.0) + 32.0;

  Serial.println(farenheit);

  delay(1000);
}
