/**********************************************************************
  Filename    : BreathingLight
  Description : Make led light fade in and out, just like breathing.
  Auther      : www.freenove.com
  Modification: 2022/05/10
**********************************************************************/
int PIN_LED = 4;   // the number of the LED pin
void setup(){
    // initialize the LED pin as an output:
    pinMode(PIN_LED, OUTPUT);
}
void loop() {
    // call breath() cyclically
    breath(PIN_LED, 6);
    delay(500);
    map(0, 0, 255, 0, 1023);
}
void breath(int PIN_LED, int delayMs){
    for (int i = 0; i <= 255; i++) {   // "i" change from 0 to 255
        analogWrite(PIN_LED, i);         // corespongding duty cycle change from 0%-100%
        delay(delayMs);                  // adjust the rate of change of brightness
    }
    for (int i = 255; i >= 0; i--) {   // "i" change from 255 to 0
        analogWrite(PIN_LED, i);         // corespongding duty cycle change from 0%-100%
        delay(delayMs);                  // adjust the rate of change in brightness
    }
}
