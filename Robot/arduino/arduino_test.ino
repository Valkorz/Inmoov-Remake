#include <Servo.h>

Servo servo1; //servo object
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servoW;

int dedos[5]; // Array to hold servo positions
int pulso = 0;

void setup() {
    servo1.attach(3);
    servo2.attach(5);
    servo3.attach(6);
    servo4.attach(9);
    servo5.attach(10);
    servoW.attach(11);
    Serial.begin(115200); 
}

void loop() {
    if (Serial.available() > 0) {
        
        String data = Serial.readStringUntil('\n');
        
        
        for (int i = 0; i < 5; i++) {
            dedos[i] = data.charAt(i) - '0';
        }

        
        if (dedos[0] == 1) {
            servo1.write(90);
        }
        if (dedos[1] == 1) {
            servo2.write(90);
        }
        if (dedos[2] == 1) {
            servo3.write(90);
        }
        if (dedos[3] == 1) {
            servo4.write(90);
        }
        if (dedos[4] == 1) {
            servo5.write(90);
        }
        
        // Control pulse servo
        if (pulso == 1) {
            servoW.write(90);
        }
    }
}
