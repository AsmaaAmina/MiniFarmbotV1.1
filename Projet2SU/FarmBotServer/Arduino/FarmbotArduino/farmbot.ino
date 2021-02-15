/*Example sketch to control a stepper motor with A4988 stepper motor driver and Arduino without a library. More info: https://www.makerguides.com */

// Define stepper motor connections and steps per revolution:
#define dirPin 3
#define stepPin 4
#define stepsPerRevolution 200
#define SensorPin A0 
float sensorValue = 0; 
void setup() {
  // Declare pins as output:
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);  // start serial communication at 9600 baud
}

void loop() {
  // Set the spinning direction clockwise:
  // Read and execute commands from serial port
   if (Serial.available()) {  // check for incoming serial data
      String command = Serial.readString();  // read command from serial port
       if (command == "yu") {
         digitalWrite(dirPin, HIGH);// Spin the stepper motor 1 revolution slowly
         for (int i = 0; i < stepsPerRevolution; i++) {
	// These four lines result in 1 step:
	 digitalWrite(stepPin, HIGH);
	 delayMicroseconds(1000);
	 digitalWrite(stepPin, LOW);
	 delayMicroseconds(1000);
         }
       }
       else if (command == "yd"){
         digitalWrite(dirPin, LOW);

  // Spin the stepper motor 1 revolution quickly:
         for (int i = 0; i < stepsPerRevolution; i++) {
    	// These four lines result in 1 step:
    	  digitalWrite(stepPin, HIGH);
    	  delayMicroseconds(1000);
    	  digitalWrite(stepPin, LOW);
    	  delayMicroseconds(1000);
      }

       }
       else if (command == "h") {
         // read and send A0 analog value
            Serial.println(analogRead(SensorPin));
       }
   }
}


