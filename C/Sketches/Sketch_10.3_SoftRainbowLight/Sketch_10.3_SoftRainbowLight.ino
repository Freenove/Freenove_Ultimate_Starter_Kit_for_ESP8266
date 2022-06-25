#include <Adafruit_NeoPixel.h>

#define PIN_POT     A0 // Define analog input pins
#define LEDS_COUNT  8  // The number of led
#define LEDS_PIN    2  // define the pin connected to the Freenove 8 led strip
#define BRIGHTNESS  50   // breghtness, the value range is 0-255.
Adafruit_NeoPixel pixels(LEDS_COUNT, LEDS_PIN, NEO_GRB + NEO_KHZ800);
void setup() {
    pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
    pixels.setBrightness(BRIGHTNESS);// set the brightness.
}

void loop() {
    int colorPos = map(analogRead(PIN_POT), 0, 1023, 0, 255);
        for (int i = 0; i < LEDS_COUNT; i++) {
            pixels.setPixelColor(i,Wheel(colorPos + i * 255 / 8)); // Set color data.
        }
    pixels.show(); // Send color data to LED, and display.
    delay(10);
}

uint32_t Wheel(byte pos){
    u32 WheelPos = pos % 0xff;
    if (WheelPos < 85){
        return ((255 - WheelPos * 3) << 16) | ((WheelPos * 3) << 8);
    }
    if (WheelPos < 170){
        WheelPos -= 85;
        return (((255 - WheelPos * 3) << 8) | (WheelPos * 3));
    }
    WheelPos -= 170;
    return ((WheelPos * 3) << 16 | (255 - WheelPos * 3));
}
