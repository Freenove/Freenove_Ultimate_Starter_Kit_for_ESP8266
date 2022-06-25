/**********************************************************************
  Filename    : ADC
  Description : Basic usage of ADC  for esp8266.
  Auther      : www.freenove.com
  Modification: 2022/05/11
**********************************************************************/
int adcValue;     // Define a variable to save ADC value
float voltage;    // Define a variable to save the calculated voltage value
void setup() {
    Serial.begin(115200);      // Initialize the serial port and set the baud rate to 115200
    Serial.println("ESP8266 is ready!");    // Print the string "ESP8266 is ready!"
}
void loop() {
    adcValue = analogRead(A0);          // Convert analog of A0 port to digital
    voltage = adcValue * (3.3 / 1023.0);// Calculate voltage according to digital
    // Send the result to computer through serial
    Serial.print("convertValue:");
    Serial.println(adcValue);
    Serial.print("Voltage:");
    Serial.println(voltage);
    delay(500);
}
