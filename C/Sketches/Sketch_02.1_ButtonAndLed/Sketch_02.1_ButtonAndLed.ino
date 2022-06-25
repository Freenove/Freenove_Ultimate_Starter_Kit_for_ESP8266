/**********************************************************************
  Filename    : ButtonAndLed
  Description : Control led by button.
  Auther      : www.freenove.com
  Modification: 2022/05/10
**********************************************************************/
#define PIN_LED    4
#define PIN_BUTTON 5
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin PIN_LED as an output.
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_BUTTON, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(PIN_BUTTON) == LOW) {
    digitalWrite(PIN_LED,HIGH);
  }else{
    digitalWrite(PIN_LED,LOW);
  }
}
