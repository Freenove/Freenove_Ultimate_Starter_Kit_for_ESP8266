/**********************************************************************
  Filename    : ColorfulLight
  Description : Use RGBLED to show random color.
  Auther      : www.freenove.com
  Modification: 2022/05/10
**********************************************************************/
const byte ledPins[] = {14, 12, 13};    //define red, green, blue led pins
int red, green, blue;
void setup() {
}

void loop() {
  red   =   random(0, 256);
  green =   random(0, 256);
  blue  =   random(0, 256);
  setColor(red, green, blue);
  delay(200);
}

void setColor(byte r, byte g, byte b) { 
  analogWrite(ledPins[0], 255 - r); //Common anode LED, low level to turn on the led.
  analogWrite(ledPins[1], 255 - g);
  analogWrite(ledPins[2], 255 - b);
}
