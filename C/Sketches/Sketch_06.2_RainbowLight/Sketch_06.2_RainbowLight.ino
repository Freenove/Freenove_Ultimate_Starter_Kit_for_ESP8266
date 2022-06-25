/**********************************************************************
  Filename    : RainbowLight
  Description : Make the strip light up in rainbow colors.
  Auther      : www.freenove.com
  Modification: 2022/05/10
**********************************************************************/
#include <Adafruit_NeoPixel.h>
#define LEDS_PIN       2 
#define LEDS_COUNT     8 // Popular NeoPixel ring size
Adafruit_NeoPixel pixels(LEDS_COUNT, LEDS_PIN, NEO_GRB + NEO_KHZ800);
void setup() {
 pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
 pixels.setBrightness(100);// set the brightness.
}
void loop(){
    for (int j = 0; j < 255; j += 2) {
        for (int i = 0; i < LEDS_COUNT; i++) {
            pixels.setPixelColor(i, Wheel((i * 256 / LEDS_COUNT + j) & 255));
        }
    pixels.show();
    delay(5);
    }
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
