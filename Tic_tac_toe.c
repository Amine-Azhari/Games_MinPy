#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>

typedef struct{
    int x;
    int y;
} coords;

coords location(char choice[2]){
    coords result;
    if (strcmp(choice, "A1") == 0) { result.x = 0; result.y = 0; }
    else if (strcmp(choice, "A2") == 0) { result.x = 1; result.y = 0; }
    else if (strcmp(choice, "A3") == 0) { result.x = 2; result.y = 0; }
    else if (strcmp(choice, "B1") == 0) { result.x = 0; result.y = 1; }
    else if (strcmp(choice, "B2") == 0) { result.x = 1; result.y = 1; }
    else if (strcmp(choice, "B3") == 0) { result.x = 2; result.y = 1; }
    else if (strcmp(choice, "C1") == 0) { result.x = 0; result.y = 2; }
    else if (strcmp(choice, "C2") == 0) { result.x = 1; result.y = 2; }
    else if (strcmp(choice, "C3") == 0) { result.x = 2; result.y = 2; }
    else {
        result.x = -1;
        result.y = -1;
    }
    return result;
}

char choices[3][3] = {{'A1','B1','C1'},{'A2','B2','C2'},{'A3','B3','C3'}};


bool win_func(char grid[3][3]){
    for (int i= 0; i<3; i++){
        if ( grid[i][0] != ' ' && grid[i][0] == grid[i][1] && grid[i][1] == grid[i][2]){
            return true;
        }
        else if ( grid[0][i] != ' ' && grid[0][i] == grid[1][i] && grid[1][i] == grid[2][i]){
            return true;
        }
    }
    if ( grid[0][0] != ' ' && grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2]){
        return true;
    }
    else if ( grid[2][0] != ' ' && grid[2][0] == grid[1][1] && grid[1][1] == grid[0][2]){
        return true;
    }
    else {
        return false;
    }
}


int main(void){
    int turn = 0;
    bool win = false;
    char grid[3][3] = {{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};
    printf("    |  A  |  B  |  C  \n");
    for (int i = 0; i<3; i++){
        printf("---- ----- ----- -----\n");
        printf(" %d  |  %c  |  %c  |  %c  \n", i+1, grid[i][0], grid[i][1], grid[i][2]);
    }

    while (!win && turn<8){
        if (turn%2 == 0){
            printf("your turn!\n");
            char choice[3];
            printf("enter your choice: ");
            scanf("%2s", &choice);
            coords loc = location(choice);
            grid[loc.x][loc.y] = 'X';
            system("cls");
            printf("    |  A  |  B  |  C  \n");
            for (int i = 0; i<3; i++){
            printf("---- ----- ----- -----\n");
            printf(" %d  |  %c  |  %c  |  %c  \n", i+1, grid[i][0], grid[i][1], grid[i][2]);
            }
        }
        else{
            srand(time(NULL));
            int index_x, index_y;
            do {
                index_x = rand() % 3;
                index_y = rand() % 3;
            } while (grid[index_x][index_y] != ' ');

            grid[index_x][index_y] = 'O';

        }

        win = win_func(grid);
        turn++;
    }
    if (turn == 8){
        printf("Tie!!!\n");
    }
    else{
        if (turn%2 == 0){
            printf("You lost\n");
        }
        else{
            printf("You win!!!\n");
        }
    }
    return 0;
}
