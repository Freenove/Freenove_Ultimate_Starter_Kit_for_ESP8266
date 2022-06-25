/**********************************************************************
  Filename    : Control Servo by Potentiometer
  Description : Use potentiometer to control the rotation of servo motor.
  Auther      : www.freenove.com
  Modification: 2022/05/11
**********************************************************************/
#include <Servo.h> 
#define ADC_Max 1023    // This is the default ADC max value on the ESP32 (12 bits ADC width); 

Servo myservo;  // create servo object to control a servo

int servoPin = 15;      // GPIO pin used to connect the servo control (digital out)
int potPin = A0;        // GPIO pin used to connect the potentiometer (analog in)
int potVal;             //variable to read the value from the analog pin

void setup()
{
    myservo.attach(servoPin, 500, 2500); // attaches the servo on servoPin to the servo object
    Serial.begin(115200);
}

void loop() {
    potVal = analogRead(potPin);  // read the value of the potentiometer (value between 0 and 1023)
    Serial.printf("potVal_1: %d\t",potVal);
    potVal = map(potVal, 0, ADC_Max, 0, 180);// scale it to use it with the servo (value between 0 and 180)
    myservo.write(potVal);                   // set the servo position according to the scaled value
    Serial.printf("potVal_2: %d\n",potVal);
    delay(15);                               // wait for the servo to get there
}
