/**********************************************************************
  Filename    : NightLamp
  Description : Controlling the brightness of LED by photoresistor.
  Auther      : www.freenove.com
  Modification: 2022/05/11
**********************************************************************/
#define PIN_ANALOG_IN   A0
#define PIN_LED         5
#define LIGHT_MIN       301
#define LIGHT_MAX       924
void setup() {
    pinMode(PIN_LED, OUTPUT);
}

void loop() {
    int adcVal = analogRead(PIN_ANALOG_IN); //read adc
    int pwmVal = map(constrain(adcVal, LIGHT_MIN, LIGHT_MAX), LIGHT_MIN, LIGHT_MAX, 0, 1023);  // adcVal re-map to pwmVal
    analogWrite(PIN_LED, pwmVal);    // set the pulse width.
    delay(10);
}
