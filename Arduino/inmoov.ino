/* HAND DETECTION WITH INMOOV + MEDIAPIPE */
#include <Servo.h>
#include <Adafruit_PWMServoDriver.h> //https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  150 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // This is the 'maximum' pulse length count (out of 4096)
#define USMIN  600 // This is the rounded 'minimum' microsecond length based on the minimum pulse of 150
#define USMAX  2400 // This is the rounded 'maximum' microsecond length based on the maximum pulse of 600
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates

//Define servo pins for each finger

Servo thumb, index, middle, ring, pinky;
Servo fingers[] = {thumb, index, middle, ring, pinky};
const int fingerPins[] = {11,10,9,6,5};
const int range[] = {180,180,180,180,180};

////////////////////////////////////////////

//Define data array
#define DATA_LENGTH 256
#define QUIT '#'

bool receiving = false, cleared = false;
int rxData;
char data[DATA_LENGTH];
int nextIndex = 0;
int elapsedTime;


//Define data array methods
void clearData(){
  for(int i = 0; i < DATA_LENGTH; i++){
    nextIndex = 0;
  	data[i] = 0;
  }
  cleared = true;
}


//Check if data buffer is a specified string
bool isDataString(char* target){
  bool val = false;
  int len = strLen(target);
  for(int i = 0; i < len; i++){
    if(data[i] == target[i]) val = true;
    else if(data[i] != target[i]){
      val = false;
      break;
    }
  } 
  return val;
}

//Get string length
int strLen(char* str){
  int length = 0;
  while (str[length] != '\0') {
    length++;
  }
  
  return length;
}


void setup()
{
  Serial.begin(9600);
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates


  //Initialize servos
  for(int i = 0; i < 5; i++){
    fingers[i].attach(fingerPins[i]);
  }
  
}

//Read serial if any input is found, store on the data array
void loop()
{
  elapsedTime = millis();

  //Get received data, check if input is detected
  rxData = Serial.read();
  if(rxData < 0){
    delay(50);
  }
  else{
    //Pass to data array, move index if full
    if(data[nextIndex] > 0) nextIndex++;
    data[nextIndex] = (char)lowByte(rxData);
  }
  
  for(int i = 0; i < 5; i++){
    pwm.setPWM(i,0, map(((int)data[i] - 48) * range[i]), 0, 180, SERVOMIN, SERVOMAX);
  }
}