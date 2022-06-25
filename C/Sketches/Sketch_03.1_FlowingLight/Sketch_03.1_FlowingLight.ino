/**********************************************************************
  Filename    : FlowingLight
  Description : Using ledbar to demonstrate flowing lamp.
  Auther      : www.freenove.com
  Modification: 2022/05/10
**********************************************************************/
byte ledPins[] = {13, 12, 14, 16, 3, 5, 4, 0, 2, 15};
int ledCounts;

void setup() {
  ledCounts = sizeof(ledPins);
  for (int i = 0; i < ledCounts; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < ledCounts; i++) {
    digitalWrite(ledPins[i], HIGH);
    delay(100);
    digitalWrite(ledPins[i], LOW);
  }
  for (int i = ledCounts - 1; i > -1; i--) {
    digitalWrite(ledPins[i], HIGH);
    delay(100);
    digitalWrite(ledPins[i], LOW);
  }
}
