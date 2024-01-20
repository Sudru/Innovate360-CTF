#include <stdio.h>
#include <string.h>

void innovate(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] >= 33 && str[i] <= 126) {
            str[i] = 33 + ((str[i] + 14) % 94);
        }
    }
}

int main() {
    char adsfagadfad[] = "465g65sq234#@#^s5#sfg3sFg4223r3$6";
    int pin;
    char secretMessage[] = ":\\be_L_90&09b?4J09c4<bCN";

    printf("Enter your 4-digit PIN: ");
    scanf("%d", &pin);

    if (pin == 8525-1234) {
        innovate(secretMessage);
        printf("Correct PIN!: %s\n", secretMessage);
    } else {
        printf("Incorrect PIN. Access denied.\n");
    }

    return 0;
}
