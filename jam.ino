#define RELAY_PIN 7

String incString = "False";

void setup() {
  // initialize digital pin RELAY_PIN as an output.
  pinMode(RELAY_PIN, OUTPUT);
  Serial.begin(57600);
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available() > 0) {
    // read the incoming string:
    incString = Serial.readString();
  }
  if (incString == "True") {
    for (int x = 0; x < 80; x++) {
      digitalWrite(RELAY_PIN, HIGH);  // turn the RELAY on
      delay(15);                      // wait for 50 milliseconds
      digitalWrite(RELAY_PIN, LOW);   // turn the RELAY off
      delay(15);                      // wait for 50 milliseconds
    }
    Serial.write("False");
    incString = "False";
  }
}