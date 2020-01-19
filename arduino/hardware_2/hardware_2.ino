/*
  State change detection (edge detection)

  Often, you don't need to know the state of a digital input all the time, but
  you just need to know when the input changes from one state to another.
  For example, you want to know when a button goes from OFF to ON. This is called
  state change detection, or edge detection.

  This example shows how to detect when a button or button changes from off to on
  and on to off.

  The circuit:
  - pushbutton attached to pin 2 from +5V
  - 10 kilohm resistor attached to pin 2 from ground
  - LED attached from pin 13 to ground (or use the built-in LED on most
    Arduino boards)

  created  27 Sep 2005
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/ButtonStateChange
*/

// this constant won't change:
const int  buttonPin = 4;    // the pin that the pushbutton is attached to
const int ledPin = 5;       // the pin that the LED is attached to
const int buzzer_pin = 7;
// Variables will change:
int buttonState = 0;         // current state of the button
int lastButtonState = 0;     // previous state of the button

#include <Servo.h>

Servo myservo;
int input;
void setup() {
  // initialize the button pin as a input:
  pinMode(buttonPin, INPUT);
  // initialize the LED as an output:
  pinMode(ledPin, OUTPUT);
  pinMode(buzzer_pin,OUTPUT);
  // initialize serial communication:
  Serial.begin(9600);
  myservo.attach(9);
  myservo.write(75);
  while (!Serial);
//  Serial.println("Started Arduino Scketch");
  
}


void loop() {
  // read the pushbutton input pin:
  read_move_servo();
  buttonState = digitalRead(buttonPin);

  // compare the buttonState to its previous state
  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button went from off to on:
      Serial.println("1");
      digitalWrite(ledPin, HIGH);
    } else {
      // if the current state is LOW then the button went from on to off:
//      Serial.println("0");
      digitalWrite(ledPin, LOW);
    }
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state, for next time through the loop
  lastButtonState = buttonState;


}

void move_to(int pos) {
  int offset = 0;
  if(pos == 0){
  offset == 300;
  }
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object

  myservo.write(pos);
  delay(300 + offset);
  myservo.detach();
  pinMode(9, INPUT);
  delay(3000);
}



void read_move_servo() {
  if (Serial.available() > 0) {
    input = Serial.parseInt();
    move_to(input);
    Serial.println(input);
    digitalWrite(buzzer_pin,HIGH);
    delay (100);
    digitalWrite(buzzer_pin,LOW);

    delay (1000);
    move_to(90);
  }
}
