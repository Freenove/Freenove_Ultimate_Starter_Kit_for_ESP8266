/**********************************************************************
  Filename    : SoftColorfulLight
  Description : Controlling the color of RGBLED by potentiometer.
  Auther      : www.freenove.com
  Modification: 2022/05/11
**********************************************************************/
int adcValue;     // Define a variable to save the ADC value
int ledPin = 4;   
const byte ledPins[] = {13, 14, 12};    //define red, green, blue led pins
int red, green, blue;
void setColor(byte r, byte g, byte b) {
  analogWrite(ledPins[0], r); //Common anode LED, low level to turn on the led.
  analogWrite(ledPins[1], g);
  analogWrite(ledPins[2], b);
}
void setup() {
    pinMode(ledPin, OUTPUT);             // Initialize the LED pin as an output
}
void loop() {
    adcValue = analogRead(A0);          // Convert the analog of A0 port to digital
    // Map analog to the 0-255 range, and works as PWM duty cycle of ledPin port
    if(adcValue>=0&&adcValue<=345){
         setColor(255, 0, 255);
      }
    else if(adcValue>345&&adcValue<680){
         setColor(0, 255, 255);
      }
    else if(adcValue>=680&&adcValue<=1024){
         setColor(255, 255, 0);
      }
}
