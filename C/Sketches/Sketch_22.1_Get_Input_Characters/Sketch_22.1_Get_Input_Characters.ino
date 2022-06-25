/**********************************************************************
  Filename    : Get Input Characters
  Description : Call the Keypad function to set the matrix keyboard and get the value for the matrix keyboard
  Auther      : www.freenove.com
  Modification: 2022/05/11
**********************************************************************/
#include <Keypad.h>

// define the symbols on the buttons of the keypad
char keys[4][4] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

char keys2[4][4]= {};
int i = 0;
int j = 0;
byte rowPins[4] = {5, 14, 12, 13}; // connect to the row pinouts of the keypad
byte colPins[4] = {15, 2, 0, 4};   // connect to the column pinouts of the keypad

// initialize an instance of class NewKeypad
Keypad myKeypad = Keypad(makeKeymap(keys2), rowPins, colPins, 4, 4);

void setup() {
  Serial.begin(115200); // Initialize the serial port and set the baud rate to 115200
  Serial.println("ESP8266 is ready!");  // Print the string "UNO is ready!"
}
void transpose(){
    for(i = 0; i < 4; i++){
       for(j = 0; j < 4; j++){
          keys2[i][j] = keys[j][i];
        }
 }
}

void loop() {
  // Get the character input
   transpose();
  char keyPressed = myKeypad.getKey();
  // If there is a character input, sent it to the serial port
  if (keyPressed) {
    Serial.println(keyPressed);
  }
}
