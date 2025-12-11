#include <stdio.h>
#include <string.h>

void lockDoor() {
    printf("Door Locked!\n");
}

void unlockDoor() {
    printf("Door Unlocked!\n");
}

int main() {
    char command[20];

    printf("IoT Smart Door Lock System\n");
    printf("Enter command (LOCK / UNLOCK / EXIT):\n");

    while (1) {
        printf("Command: ");
        scanf("%s", command);

        if (strcmp(command, "LOCK") == 0) {
            lockDoor();
        } else if (strcmp(command, "UNLOCK") == 0) {
            unlockDoor();
        } else if (strcmp(command, "EXIT") == 0) {
            printf("Exiting system.\n");
            break;
        } else {
            printf("Invalid command! Use LOCK, UNLOCK, or EXIT.\n");
        }
    }

    return 0;
}
