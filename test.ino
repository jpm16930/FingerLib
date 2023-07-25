void setup() {
  Serial.begin(38400);  // Make sure to set the correct baud rate.
}

void loop() {
  // Send the command 'G0' to the hand.
  Serial.println("G1");
  delay(500);  // Add a delay if needed before sending the next command.
}
