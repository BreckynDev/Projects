#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
    // Initilized and declared variables used in this program
    const int DATE_ROW = 3;
    const double MONTHLY_INTREST = (0.014 / 12); //Divided by 12 because there is 12 months in a year
    char    moreBankRecord, 
            transactionType;

    // Main loop to process multiple bank records.
    do
    {
        // Initilized and declared variables used in this program (Rests after reading another bank record)
        int     month, 
                previousMonth = 0, 
                count = 0, 
                depositCount = 0, 
                withdrawCount = 0, 
                line = 0;

        float   transactionAmount, 
                interestRate,
                totalInterest, 
                roundedTotal;

        double  accountBalance = 0.00, 
                depositTotal = 0.00, 
                withdrawTotal = 0.00;
        
        bool    ifOverDrafted = false;
        bool    running = true;

        ifstream inputFile;
        string text, fileName;

        // Prompts user for file name and checks if it opens successfully.
        do
        {
            cout << "What is the name of the file that holds the bank records? ";
            cin >> fileName; 

            inputFile.open(fileName);

            if (!inputFile)
                cout << "Error opening file: " << fileName << endl;
            else
                running = false;

        } while (running);

        // While loop to read data from the file until no more data is available.
        while (inputFile >> text && !ifOverDrafted)
        {

            count += 1; // Couts how many strings

            // Deposit and Withdraw
            if (count == 1)
            {
                if (text == "d")
                    transactionType = 'd';
                else
                    transactionType = 'w';
            }

            // Month
            else if (count == 2)
            {
                //Converts second string into int and stores it in month
                month = stoi(text);

                // Checks if the month has changed if so, applies monthly interest.
                if (!(month == previousMonth))
                {
                    interestRate = accountBalance * MONTHLY_INTREST;
                    totalInterest += interestRate;
                    accountBalance += interestRate;
                }
                previousMonth = month;
            }

            // Transation amount
            else if (count == 3)
            {
                //Converts last string into float and assigning it to transactionAmount
                transactionAmount = stof(text);

                /*
                If the transtion ammount is negitive then the account is overdrawn
                else do the transaction
                */ 
                if (accountBalance < 0)
                {
                    cout << "Error on line: " << line << " of file " << fileName << endl;
                    cout << "\tBank account will be overdrawn after this line, quitting program" << endl;
                    ifOverDrafted = true;
                }
                else if (transactionAmount < 0)
                {
                    cout << "Error on line: " << line << " of file " << fileName << endl;
                    cout << "\ttansaction amount cannot be less then 0, quitting program" << endl;
                    ifOverDrafted = true; //Uses this bool even though its not overdrafted just used to quit
                }

                else
                {
                    // Checks transaction type (deposit/withdraw) and performs the corresponding calculation.
                    if (transactionType == 'd')
                    {
                        accountBalance += transactionAmount;
                        depositCount += 1;
                        depositTotal += transactionAmount;
                    }
                    else if (transactionType == 'w')
                    {
                        accountBalance -= transactionAmount;
                        withdrawCount += 1;
                        withdrawTotal += transactionAmount;
                    }
                }
                /*
                Once string count reachs 3 that row is complete
                and a new row will be started and the string count
                is set back to 0
                */
                if (count == DATE_ROW)
                    count = 0;
                    line += 1;
            }
        }

        if (!ifOverDrafted)
        {
            cout << "You made " << depositCount << " deposits, for a total deposit of $" 
                 << fixed << setprecision(2) << depositTotal << endl;
            cout << "You made " << withdrawCount << " withdrawals, for a total withdrawal of $" 
                 << fixed << setprecision(2) << withdrawTotal << endl;
            cout << "Total interest: " << fixed << setprecision(2) << totalInterest << endl;
            cout << "Current Account Balance: $" << fixed << setprecision(2) << accountBalance << endl;
        }

        inputFile.close(); // Closes the file

        //Check if user would like to contuine reading bank records
        cout << "Would you like to read another bank record (y/n): ";
        cin >> moreBankRecord;

    } while (moreBankRecord == 'y' || moreBankRecord == 'Y' );
    
    return 0;
}