/**********************************************************************
  Filename    : Alertor
  Description : Control passive buzzer by button.
  Auther      : www.freenove.com
  Modification: 2022/05/10
**********************************************************************/
#define PIN_BUZZER 5
#define PIN_BUTTON 4
void setup() {
  pinMode(PIN_BUTTON, INPUT);
  pinMode(PIN_BUZZER, OUTPUT); // Set Buzzer pin to output mode
  Serial.begin(115200);
}

void loop() {
  if (digitalRead(PIN_BUTTON) == LOW) {
    alert();
  } else {
    analogWrite(PIN_BUZZER, 0);
  }
}

void alert() {
  float sinVal;         // Define a variable to{ save sine value
  int toneVal;          // Define a variable to save sound frequency
  for (int x = 0; x < 360; x++) {        // X from 0 degree->360 degree
    sinVal = sin(x * (PI / 180));        // Calculate the sine of x
    toneVal = 500 + sinVal * 500;        // Calculate sound frequency according to the sine of x
    tone(PIN_BUZZER, toneVal);           // Output sound frequency to buzzerPin
    delay(1);
    noTone(PIN_BUZZER);
    delay(1);
    Serial.printf("Running  %d \n",toneVal);
  }
}
