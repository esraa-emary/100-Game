// Purpose: 100 Game.
// Description: Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
// Author: Esraa Emary Abd Elsalam.
// version: 4.
//========================================================== 100 Game =====================================================// 

#include <bits/stdc++.h>
#include <iostream>
using namespace std;

//check the validity of the move from 1 to 10
int validity(string name,int& move) {
    while (true) {
        cout << name << " player: choose an integer number from 1 to 10: ";
        cin >> move;

        if (cin.fail() || cin.peek() != '\n' || move < 1 || move > 10) {
            // Invalid input, clear error flag and discard input
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Please enter a valid integer number" << endl;
        } else {
            // Valid input
            break;
        }
    }
    return move;
}
//check the validity of the move from 1 to (100 - sum)
int validity_end(int& move, string name,int sum)
{
    while (true) {
        cout << name << " player: choose an integer number from 1 to " << (100 - sum) << ": ";
        cin >> move;

        if (cin.fail() || cin.peek() != '\n' || move < 1 || move > (100 - sum)) {
            // Invalid input, clear error flag and discard input
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Please enter a valid integer number" << endl;
        } else {
            // Valid input
            break;
        }
    }
    return move;
}
//*******************************************THE GAME****************************************//
int main()
{
    //Set the value of sum
    int sum = 0;
    int move;

    //Welcome message and display status
    cout<<"#==========Welcome to 100 game==========#"<<endl;
    cout<<"Sum is equal to 0"<<endl;

    //Game playing
    while (sum < 100)
    {
        //first player
        if (sum < 90)
        {
            validity("First",move);
        }
        // add the first player move to the sum
        sum += move;

        //display status
        cout<<"Sum is equal  to "<<sum<<endl;

        //check if the second player won
        if (sum >= 90 && sum < 100)
        {
            cout<<"Second player is closed to win"<< endl;
            validity_end(move, "Second",sum);
            
            //check if second player won
            if (move == (100-sum))
            {
                cout<<"Sum is equal to 100"<<endl;
                cout<<"Second player is the winner";
                break;
            }
        }
        //second player
        if (sum < 90)
        {
            validity("Second",move); //check the validity of the number
        }
        // add the second player move to the sum
        sum += move;

        //display status
        cout<<"Sum is equal  to "<<sum<<endl;

        //check if the first player won
        if (sum >= 90 && sum < 100)
        {
            cout<<"First player is closed to win"<< endl;
            validity_end(move, "First",sum);
            
            //check if first player won
            if (move == (100-sum))
            {
                cout<<"Sum is equal to 100"<<endl;
                cout<<"First player is the winner";
                break;
            }
        }
    }
}
