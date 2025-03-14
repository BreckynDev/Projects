#include <iostream>
#include <random>
#include <iomanip>
using namespace std;

const int COLS = 3;
const int ROWS = 3;
const int LENGHT = 30;

void currentBoardDisplay(const int, char[][COLS]);
void referanceBoardDisplay(const int, const int, const int LENGHT);
int checkMove(int, char[][COLS]);
char checkWin(char[ROWS][COLS]);
void introPromt(const int LENGHT);
void dashDisplay(const int LENGHT);

int main()
{
    const int PLAYER_COUNT = 2;
    int playerNum;
    int userInput;
    char player[PLAYER_COUNT] = {'X', 'O'};
    char gameBoard[ROWS][COLS];
    char winCondition;
    bool gameLoop = true;

    introPromt(LENGHT);
    cout << endl;

    referanceBoardDisplay(ROWS, COLS, LENGHT);

    for (int row = 0; row < ROWS; row++)
        for (int col = 0; col < COLS; col++)
            gameBoard[row][col] = ' ';

    cout << "Press ENTER to start game: ";
    cin.get();

    while (gameLoop == true)
    {
        for (int index = 0; index < PLAYER_COUNT; index++)
        {
            currentBoardDisplay(ROWS, gameBoard);

            if (index == 0)
                playerNum = 1;
            else if (index == 1)
                playerNum = 2;

            cout << "Player " << playerNum << " -> " << player[index] << endl;
            cout << "Enter move [0-8]: ";
            cin >> userInput;
            userInput = checkMove(userInput, gameBoard);

            int row = userInput / 3;
            int col = userInput % 3;

            gameBoard[row][col] = player[index];

            winCondition = checkWin(gameBoard);
            if (winCondition == 'X')
            {
                cout << "Player " << playerNum << " (" << player[index] << ") has won" << endl;
                gameLoop = false;
                index++;
            }
            else if (winCondition == 'O')
            {
                cout << "Player " << playerNum << " (" << player[index] << ") has won" << endl;
                gameLoop = false;
                index++;
            }
        }
    }
    currentBoardDisplay(ROWS, gameBoard);
    cout << "Game Over!";
    cout << endl;
}

void currentBoardDisplay(const int ROWS, char gameBoard[][COLS])
{
    for (int row = 0; row < ROWS; row++)
    {
        if (row > 0)
            for (int count = 0; count < COLS; count++)
            {
                cout << "-";
                cout << " ";
            }
        cout << endl;

        for (int col = 0; col < COLS; col++)
        {
            cout << gameBoard[row][col];
            if (col < 2)
                cout << "|";
        }
        cout << endl;
    }
    cout << endl;
}
void referanceBoardDisplay(const int ROWS, const int COLS, const int LENGHT)
{
    int gameBoardDisplay[ROWS][COLS];
    int count = 0;

    cout << "Enter number from board to make move";

    cout << endl;
    dashDisplay(LENGHT);

    for (int row = 0; row < ROWS; row++)
        for (int col = 0; col < COLS; col++)
        {
            gameBoardDisplay[row][col] = count;
            count++;
        }

    for (int row = 0; row < ROWS; row++)
    {
        if (row > 0)
            for (int count = 0; count < COLS; count++)
            {
                cout << "-";
                cout << " ";
            }
        cout << endl;

        for (int col = 0; col < COLS; col++)
        {
            cout << gameBoardDisplay[row][col];
            if (col < 2)
                cout << "|";
        }
        cout << endl;
    }

    cout << endl;
    dashDisplay(LENGHT);
}

int checkMove(int userInput, char gameBoard[][COLS])
{
    int row = userInput / 3;
    int col = userInput % 3;

    while (userInput < 0 || userInput > 8)
    {
        cout << "Enter move: ";
        cin >> userInput;
    }
    while (gameBoard[row][col] == 'X' || gameBoard[row][col] == 'O')
    {
        cout << "Enter move: ";
        cin >> userInput;

        row = userInput / 3;
        col = userInput % 3;
    }

    return userInput;
}

char checkWin(char gameBoard[ROWS][COLS])
{
    for (int row = 0; row < ROWS; row++)
        if (gameBoard[row][0] != ' ' && gameBoard[row][0] == gameBoard[row][1] && gameBoard[row][1] == gameBoard[row][2])
            return gameBoard[row][0];

    for (int col = 0; col < COLS; col++)
        if (gameBoard[0][col] != ' ' && gameBoard[0][col] == gameBoard[1][col] && gameBoard[1][col] == gameBoard[2][col])
            return gameBoard[0][col];

    if (gameBoard[0][0] != ' ' && gameBoard[0][0] == gameBoard[1][1] && gameBoard[1][1] == gameBoard[2][2])
        return gameBoard[0][0];

    else if (gameBoard[0][2] != ' ' && gameBoard[0][2] == gameBoard[1][1] && gameBoard[1][1] == gameBoard[2][0])
        return gameBoard[0][2];

    return ' ';
}

void introPromt(const int LENGHT)
{
    cout << endl;
    cout << "   ";
    dashDisplay(LENGHT);
    cout << "   Welcome to Tic-Tac-Toe the Game   " << endl;
    cout << "   ";
    dashDisplay(LENGHT);
}

void dashDisplay(const int LENGHT)
{
    for (int count = 0; count <= LENGHT; count++)
        cout << "-";
    cout << endl;
}