/**********************************************************************
  Filename    : SoftLight
  Description : Controlling the brightness of LED by potentiometer.
  Auther      : www.freenove.com
  Modification: 2022/05/11
**********************************************************************/
int adcValue;     // Define a variable to save the ADC value
int ledPin = 4;   
void setup() {
    pinMode(ledPin, OUTPUT);             // Initialize the LED pin as an output
}
void loop() {
    adcValue = analogRead(A0);          // Convert the analog of A0 port to digital
    // Map analog to the 0-255 range, and works as PWM duty cycle of ledPin port
    analogWrite(ledPin, map(adcValue, 0, 1024, 0, 255));
}
