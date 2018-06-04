#include <SPI.h>
#include <Pixy.h>

#define RDIR 2
#define RSPEED 3
#define LDIR 4
#define LSPEED 5
#define SOUND_TRANSMISSION 8
#define SOUND_ECHO 9
#define LINE_SENSORL 6
#define LINE_SENSORR 7
#define LINE_SENSORB 8 //TODO: CHECK PIN ASSIGNMENT!
#define GREEN_BUTTON A1
#define RED_BUTTON A2

int motor_base_speed = 205;

float dist = 0;
float duration;

int left_sen = 0;
int right_sen = 0;
int back_sen = 0;

String colour_chosen = "";

bool move_front = true;
bool align_first = true;

Pixy pixy;

void setup() {
  Serial.begin(9600);
  pixy.init();

  pinMode(RDIR, OUTPUT);
  pinMode(RSPEED, OUTPUT);
  pinMode(LDIR, OUTPUT);
  pinMode(LSPEED, OUTPUT);
  pinMode(SOUND_TRANSMISSION, OUTPUT);

  pinMode(SOUND_ECHO, INPUT);
  pinMode(LINE_SENSORL, INPUT);
  pinMode(LINE_SENSORR, INPUT);
  pinMode(A1, INPUT_PULLUP);
  pinMode(A2, INPUT_PULLUP);

  //  Read button
  //  boolean is_button_clicked = false;
  //  while (!is_button_clicked) {
  //    if (digitalRead(RED_BUTTON) == LOW || digitalRead(GREEN_BUTTON) == LOW){
  //      if (digitalRead(RED_BUTTON) == LOW){
  //        colour_chosen = "RED";
  //      } else {
  //        colour_chosen = "GREEN";
  //      }
  //      is_button_clicked = true;
  //    }
  //  }
  //
  //  Serial.println(colour_chosen);

  Serial.println("Setup DONE!");
}


//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//
//* //////////////////////////////////////// MAIN LOOP /////////////////////////////////////////////////// *//
//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//

void loop() {
    if (move_front) {
        int x_pos = pixyRead(1);
        track_object(x_pos);
        delay(30);
        measure_distance();
    } else {
        if (align_first) {
            rotate_robot();
        } else {
            move_backwards();
        }
    }
}

//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//
//* //////////////////////////////////////// MAIN LOOP /////////////////////////////////////////////////// *//
//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//

int pixyRead(int colour) {
  static int i = 0;
  int j;
  uint16_t blocks;
  char buf[32];
  int x_pos = 0;
  blocks = pixy.getBlocks();

  if (blocks) {
    sprintf(buf, "Detected %d:\n", blocks);
    Serial.print(buf);
    for (j = 0; j < blocks; j++) {
      //sprintf(buf, "  block %d: ", j);
      //Serial.print(buf);
      //pixy.blocks[j].print();
 
      if (pixy.blocks[j].signature == colour) {
        x_pos = pixy.blocks[j].x;
      }
    }
  }
  return x_pos;
}

//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//

void track_object(int x_pos) {
  Serial.println(x_pos);
  int error = 160 - x_pos;
  int output = 1.2 * error;
  int max_output = 50;

  if (output > max_output) {
    output = max_output;
  }else if (output < -1 * max_output){
    output = -1 * max_output;
  }

  //! If x_pos is zero, camera does not detect anything so output set to zero
  if (x_pos == 0){
    output = 0;
  }

  Serial.println("PID OUTPUT: " + (String) output);

  forward(motor_base_speed - output, motor_base_speed + output);
}

//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//

void measure_distance() {
  digitalWrite(SOUND_TRANSMISSION, LOW);
  delayMicroseconds(2);
  digitalWrite(SOUND_TRANSMISSION, HIGH);
  delayMicroseconds(10);
  digitalWrite(SOUND_TRANSMISSION, LOW);
  duration = pulseIn(SOUND_ECHO, HIGH);
  dist = duration * 0.034 / 2;
  //Serial.println(dist);
  delay(100);

  if (dist <= 5) {
      move_front = false;
      stop();
  }
}

//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//

void rotate_robot() {
    while (left_sen != 1 || right_sen != 1) { //TODO: CHECK 1 or 0 --> Assume that 0 is white and 1 is black
        left_sen = digitalRead(LINE_SENSORL);
        right_sen = digitalRead(LINE_SENSORR);
        backward(255, 255);
    }

    //TODO: Might need to check motor direction!!
    if (left_sen == 1 && right_sen == 0) { //* Means that we need to rotate LEFT wheel
        while (left_sen != 0) {
            left_sen = digitalRead(LINE_SENSORL);
            digitalWrite(LDIR, LOW);
            analogWrite(LSPEED, 255);
        }
    } else {                                //* Rotate RIGHT wheel
        while (right_sen != 0) {
            right_sen = digitalRead(LINE_SENSORR);
            digitalWrite(RDIR, LOW);
            analogWrite(RSPEED, 255);
        }
    }
    stop();
    align_first = false;
}

//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//

void move_backwards() {
    backward(255, 255);
}

//* ////////////////////////////////////////////////////////////////////////////////////////////////////// *//

void forward(int left_s, int right_s) {
  digitalWrite(RDIR, HIGH);
  digitalWrite(LDIR, HIGH);
  analogWrite(LSPEED, right_s);
  analogWrite(RSPEED, left_s);
  //Serial.println("Forward");
}

void backward(int left_s, int right_s) {
  digitalWrite(RDIR, LOW);
  digitalWrite(LDIR, LOW);
  analogWrite(RSPEED, right_s);
  analogWrite(LSPEED, left_s);
  //  Serial.println("Backward");
}

void right(int left_s, int right_s) {
  digitalWrite(RDIR, LOW);
  digitalWrite(LDIR, HIGH);
  analogWrite(RSPEED, right_s);
  analogWrite(LSPEED, left_s);
  //  Serial.println("Right");
}

void left(int left_s, int right_s) {
  digitalWrite(RDIR, HIGH);
  digitalWrite(LDIR, LOW);
  analogWrite(RSPEED, right_s);
  analogWrite(LSPEED, left_s);
  //  Serial.println("Left");
}

void stop() {
  digitalWrite(RDIR, LOW);
  digitalWrite(LDIR, LOW);
  analogWrite(RSPEED, 0);
  analogWrite(LSPEED, 0);
  //  Serial.println("Stop");
}

void line_detect(String linesensor) {
  if (linesensor == "L") {
    left_sen = digitalRead(LINE_SENSORL);
  }
  else {
    right_sen = digitalRead(LINE_SENSORR);
  }
}