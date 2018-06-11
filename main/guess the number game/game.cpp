#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdbool.h>
#include <iomanip>


void InitializeGame(void);
void GetInput(char * input);
bool CheckAnswer(char * input);
bool GiveTips(char * input);
void GetRandom(char * random);
void ShowMenu();
void ShowFooter(int times, int rounds);

using namespace std;
char answer[5] = "";
char input[10] = "";
int times = 0;
int rounds = 0;

int main(int argc, char** argv) 
{
    ShowMenu();
    char c;
    int count = 0;
    while (true)
    {
        cout << "Enter 'S' to start the game, 'Q' to quit." << endl;
        c = toupper(getchar());
        while(getchar() != '\n');
        if (c == 'Q')
            break;
        else if(c == 'S'){
            cout << "Game Start! Enter your answer:" << endl;
            times = 0;
            InitializeGame();//初始化游戏
            cout << "The answer is: " << answer << endl; 
            //GetInput(input); //输入猜测值
            //检查猜测是否正确 不正确则给出提示 
            do{
                times++;
                GetInput(input);
            }while(GiveTips(input) == false);
            cout << "You have tried [" << times << "] times." << endl;
            count += times;
        }else
            cout << "Only 'S' and 'Q' are received." << endl;
    }
    ShowFooter(count, rounds);
    return 0;
}


void InitializeGame(void){
    static bool init_rand = false;
    if (init_rand == false){
        srand ((unsigned) time(NULL));
        init_rand = true;
    }
    GetRandom(answer);
}

void GetInput(char * input){
    gets(input);
    //cout << "!!!TEST" << input << endl;
    while(true){
        if(strcmp(input, "Q") == 0 || strcmp(input, "q") == 0)
        {
            cout << "Sure to give up game?[Y]es or [N]ot" << endl;
            gets(input);
        }else{
            if(strlen(input) != 4){
                cout << "Please input a 4-digits number!" << endl;
                gets(input);
                continue;
            }
            if(CheckAnswer(input) == false){
                cout << "There couldn't be two same character in your answer!" << endl;
                gets(input);
                continue;
            }
        }
        break;
    }
}

bool CheckAnswer(char * input){
    char temp[5];
    strcpy (temp, input);
    for(int i = 0; i < 4; i++){
        for(int j = i + 1; j < 4; j++)
            if(temp[i] == input[j])
                return false;
    }
    return true;
}

bool GiveTips(char * input){
    if(input[0] == 'Y' || input[0] == 'y')
        return true;
    else{
        int a = 0, b = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if (input[i] == answer[j]){
                    if(i == j)
                        a++;
                    else
                        b++;
                    continue;
                }
            }
        }
        cout << "Tips:" << a << "A" << b << "B\n" << endl; 
        if (a == 4)
            return true;
        rounds += 1;
        cout << "Enter another answer:";
        return false;
    }
}

void GetRandom(char * random){
    int i, j[10], k;
    for (i = 0; i < 10; i++){
        j[i] = i;
    }
    for(i = 0; i < 4; i++){
        k = (int)rand() % 10;
        while (j[k] == -1){
            k = (k + 1) % 10;
        }
        random[i] = '0' + j[k];
        j[k] = -1;
    }
}

void ShowMenu()
{
    cout << "[]===========================================================================[]\n";
    cout << "||  ██████╗████████╗███╗   ██╗ ██████╗  +----------------------------------+ ||\n";
    cout << "|| ██╔════╝╚══██╔══╝████╗  ██║██╔════╝  |            怎么玩                | ||\n";
    cout << "|| ██║  ███╗  ██║   ██╔██╗ ██║██║  ███╗ |  按照提示输入四位数字猜测电脑所  | ||\n";
    cout << "|| ██║   ██║  ██║   ██║╚██╗██║██║   ██║ |    生成的数字，“xAyB” 表示：     | ||\n";
    cout << "|| ╚██████╔╝  ██║   ██║ ╚████║╚██████╔╝ | A：有x个数字猜对且位于正确位置上 | ||\n";
    cout << "||  ╚═════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝  | B：有y个数字猜对但不在正确位置上 | ||\n";
    cout << "||    *** Guess The Number Game ***     +----------------------------------+ ||\n";
    cout << "[]===========================================================================[]\n";
    
}

void ShowFooter(int times ,int rounds)
{
    cout << "[]===========================================================================[]\n";
    cout << "||  ██████╗████████╗███╗   ██╗ ██████╗  +----------------------------------+ ||\n";
    cout << "|| ██╔════╝╚══██╔══╝████╗  ██║██╔════╝  |             GOAL                 | ||\n";
    cout << "|| ██║  ███╗  ██║   ██╔██╗ ██║██║  ███╗ |         You have tried           | ||\n";
    cout << "|| ██║   ██║  ██║   ██║╚██╗██║██║   ██║ |         ";
    cout << times << setw(3);
    cout <<  " times                  | ||\n";
    cout << "|| ╚██████╔╝  ██║   ██║ ╚████║╚██████╔╝ |         ";
    cout << rounds << setw(3);
    cout << "  rounds                | ||\n";
    cout << "||  ╚═════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝  |                                  | ||\n";
    cout << "||    ***       Game Over       ***     +----------------------------------+ ||\n";
    cout << "[]===========================================================================[]\n";

}