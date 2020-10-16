
// Handel root handles output to the user


int led = 5;
int button = 1;

pinmode(button, INPUT);
pinmode(led, OUTPUT);


void loop(void) {
    server.handleClient();
    delay(500);
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
}