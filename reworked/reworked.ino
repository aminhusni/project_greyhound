
#include <Servo.h>

int URPWM = 5; 
int URTRIG = 6; 
int DISLIM = 150;
int dis = 999;
int SERVO = 12;
int ENERGYPAD = 1;
int energydone = 0;
long ranNumber;
Servo myservo;

const int sensor = A4;
const int threshold = 150;

int sensorReading = 0;

unsigned int Distance = 0;
uint8_t EnPwmCmd[4] = {
    0x44,
    0x02,
    0xbb,
    0x01
}; // distance measure command

char choice = 0;
char bypassser = 0;

int chargeCounter = 0;
int jumpCounter = 0;
int chargeflag = 0;
int serrsent = 0;

const int chargelim = 5; //How many bars here
int jumplim = 6; //How many jumps per bar

unsigned long timestart = 0;
unsigned long timetres = 10000; //Timeout 35 seconds for charging series
unsigned long timediff = 0;

int modeselect = 0;
int SELECT_ULTRA = 4;
int SELECT_BUTTON = 3;
int ULTRA_BYPASS = 2;

void setup() { // Serial initialization
    Serial.begin(9600); // Sets the baud rate to 9600
    PWM_Mode_Setup();
    pinMode(13, OUTPUT); //LED
    pinMode(SERVO, OUTPUT);
    pinMode(ENERGYPAD, INPUT);

    pinMode(SELECT_BUTTON, INPUT_PULLUP);
    pinMode(SELECT_ULTRA, INPUT_PULLUP);
    pinMode(ULTRA_BYPASS, INPUT_PULLUP);

    myservo.attach(2);

    myservo.write(0);
    delay(500);
    myservo.write(20);
    delay(500);
    myservo.write(0);

    int flag = 0;

    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);

    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);

    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);

    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);

    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);

    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);
}

void loop() {
        PWM_Mode();
        delay(100);
    } //PWM mode setup function

void PWM_Mode_Setup() {
    pinMode(URTRIG, OUTPUT); // A low pull on pin COMP/TRIG
    digitalWrite(URTRIG, HIGH); // Set to HIGH
    pinMode(URPWM, INPUT); // Sending Enable PWM mode command

}

void PWM_Mode() {
    bypassser = 0;
    while (modeselect == 0) {
        if (digitalRead(SELECT_BUTTON) == HIGH) {
            modeselect = 1;
            break;
        }
        if (digitalRead(SELECT_ULTRA) == HIGH) {
            modeselect = 2;
            break;
        }

    }

    if (modeselect == 1) { //BYPASS MODE
        if (ULTRA_BYPASS == HIGH) { //CHECK FOR OVERRIDE BUTTON
            dis = 1;
        }
        bypassser = Serial.read();
        if (bypassser == 8) {
            dis = 1;
        }
    }

    if (modeselect == 2) { //ULTRASONIC MODE
        digitalWrite(URTRIG, LOW);
        digitalWrite(URTRIG, HIGH); // reading Pin PWM will output pulses

        unsigned long DistanceMeasured = pulseIn(URPWM, LOW);

        if (DistanceMeasured >= 10200) { // the reading is invalid.
            dis = 999;
        } else {
            dis = DistanceMeasured / 50; // every 50us low level stands for 1cm
        }

    }

    if (dis < DISLIM) {

        Serial.print("ultra\n");
        Serial.flush();
        delay(1000);
        while (!Serial.available()) {}

        choice = Serial.read();
        switch (choice) {
        case '1':
            delay(2000);
            chargeflag = 1;
            timestart = millis();

            //This is where the jumping starts
            jumplim = random(1, 10); //generate random jumping numbers
            while (chargeCounter <= chargelim) {
                while (jumpCounter < jumplim) {
                    if (analogRead(sensor) > threshold) {
                        jumpCounter++;
                        delay(500);
                    }
                    timediff = millis() - timestart;
                    if (timediff >= timetres) {
                        chargeCounter = 90;
                        jumpCounter = 90;
                        chargeflag = 0;
                    }
                    delay(10);
                }
                chargeCounter++;
                jumpCounter = 0;
                Serial.print("yes\n");
                serrsent++;
                delay(500);
            }

            chargeCounter = 0;
            jumpCounter = 0;
            delay(1000);

            while (serrsent != 6) {
                Serial.print("no\n");
                serrsent++;
            }
            serrsent = 0;

            if (chargeflag == 1) {
                Serial.print("succ\n");
                delay(9000);
                myservo.write(180);
                delay(5000);
                myservo.write(0);
            } else if (chargeflag == 0) {
                Serial.print("fail\n");
            }

            Serial.flush();
            break;

        case 'r':
            delay(1000);
            myservo.write(0);
            Serial.flush();
            break;

        }
        dis = 999;
        delay(7000);

    }

}
