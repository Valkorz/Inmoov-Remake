#include <PCA9685.h>

/* HAND DETECTION WITH INMOOV + MEDIAPIPE */
PCA9685 servoController;
PCA9685_ServoEval pwmServo;
//Define servo pins for each finger

const int range[] = {180,180,180,180,180};

////////////////////////////////////////////
//Define data array
#define DATA_LENGTH 5
#define QUIT '#'

bool receiving = false, cleared = false;
int rxData;
char data[DATA_LENGTH];
int nextIndex = 0;
int elapsedTime;

char targetMessage[] = "pisca";

//Define data array methods
void clearData(){
  Serial.println("clearing...");
  for(int i = 0; i < DATA_LENGTH; i++){
    nextIndex = 0;
  	data[i] = '0';
  }
  cleared = true;
}

//Read data and choose action
void readData(){
  for(int i = 0; i < DATA_LENGTH; i++){
    doAction(data[i]);   
  }
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

//Add different actions for different character readings
bool blink = false;

void doAction(char c){
  switch(c){
   	case QUIT:
    	clearData();
    	break;
  }
}

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  servoController.resetDevices();
  servoController.init();
  servoController.setPWMFrequency(100);

  clearData();
  
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
  else if(rxData == 48 || rxData == 49){
    //Pass to data array, move index if full 
    Serial.println("Received: ");
    Serial.println(rxData);
    if(nextIndex > DATA_LENGTH - 1) clearData();
    else{
    	data[nextIndex] = (char)lowByte(rxData);
      nextIndex++;
    }  
  }
  else if((char)lowByte(rxData) == QUIT){
    clearData();
  }
  
  Serial.println(data);
  Serial.println("nextIndex: ");
  Serial.println(nextIndex);
  Serial.println("\n");
  for(int i = 0; i < 5; i++){
    Serial.print("Setting pwm for: ");
    Serial.print(i);
    Serial.print(" as: ");
    Serial.print(pwmServo.pwmForAngle(((int)data[i] - 48) * range[i]));
    Serial.println("\n");
    servoController.setChannelPWM(i,pwmServo.pwmForAngle(((int)data[i] - 48) * range[i]));
  }

  delay(1500);
}
