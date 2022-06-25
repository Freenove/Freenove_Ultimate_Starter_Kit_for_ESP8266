/**********************************************************************
  Filename    : Control_Motor_by_L293D
  Description : Use PWM to control the direction and speed of the motor.
  Auther      : www.freenove.com
  Modification: 2022/05/11
**********************************************************************/
int in1Pin = 12;      // Define L293D channel 1 pin
int in2Pin = 14;      // Define L293D channel 2 pin
int enable1Pin = 13;  // Define L293D enable 1 pin

boolean rotationDir;  // Define a variable to save the motor's rotation direction
int rotationSpeed;    // Define a variable to save the motor rotation speed

void setup() {
  // Initialize the pin into an output mode:
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(enable1Pin, OUTPUT);
}

void loop() {
  int potenVal = analogRead(A0);// Convert the voltage of rotary potentiometer into digital
  rotationSpeed = potenVal - 512;
  if (potenVal > 512)
    rotationDir = true;
  else
    rotationDir = false;
  // Calculate the motor speed
  rotationSpeed = abs(potenVal - 512);
  //Control the steering and speed of the motor
  driveMotor(rotationDir, constrain(rotationSpeed,0, 512));
}

void driveMotor(boolean dir, int spd) {
  if (dir) {// Control motor rotation direction
    digitalWrite(in1Pin, HIGH);  
    digitalWrite(in2Pin, LOW);
  }
  else {
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, HIGH);
  }
  analogWrite(enable1Pin, spd); // Control motor rotation speed
}
