/**********************************************************************
  Filename    : FlowingLight2
  Description : More cool flowing light.
  Auther      : www.freenove.com
  Modification: 2022/05/10
**********************************************************************/
const byte ledPins[] = {13, 12, 14, 5, 4, 0, 2, 15};    //define led pins
const int dutys[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     1023, 512, 256, 128, 64, 32, 16, 8, 4, 2,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                    };      //define the pwm dutys
int ledCounts;              //led counts
int delayTimes = 50;        //flowing speed ,the smaller, the faster
void setup() {
  ledCounts = sizeof(ledPins);    //get the led counts
}

void loop() {
  for (int i = 0; i < 20; i++) {        //flowing one side to other side
    for (int j = 0; j < ledCounts; j++) {
      analogWrite(ledPins[j], dutys[i + j]);
    }
    delay(delayTimes);
  }
  for (int i = 0; i < 20; i++) {        //flowing one side to other side
    for (int j = ledCounts - 1; j > -1; j--) {
      analogWrite(ledPins[j], dutys[i + (ledCounts - 1 - j)]);
    }
    delay(delayTimes);
  }
}
