/**********************************************************************
  Filename    : Ultrasonic Ranging
  Description : Use the ultrasonic module to measure the distance.
  Auther      : www.freenove.com
  Modification: 2020/07/11
**********************************************************************/
#include <UltrasonicSensor.h>
//Attach the trigger and echo pins to pins 13 and 14 of esp8266
UltrasonicSensor ultrasonic(13, 14);

void setup() {
  Serial.begin(115200);
  //set the speed of sound propagation according to the temperature to reduce errors
  int temperature = 22;  //Setting ambient temperature
  ultrasonic.setTemperature(temperature);
}

void loop() {
  int distance = ultrasonic.distanceInCentimeters();
  Serial.printf("Distance: %dcm\n",distance);
  delay(300);
}
