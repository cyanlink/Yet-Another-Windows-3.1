#include<iostream>
using namespace std;
enum gesture {SCISSOR=1, PUNCH, CLOTH};

//类定义
//GameObject定义游戏中的角色信息
//包括使用手势、名字、输赢以及一个用于主程序显示使用的信息显示函数
class GameObject
{
    public:
        int _scissorCount;
        int _punchCount;
        int _clothCount;

        int _scissorWinCount;
        int _punchWinCount;
        int _clothWinCount;

        int _winHistory[10];
        int _plan;
        int plan;

        bool _win;
        int _gesture;
        string _name;
        string showGesture()
        {
            if(_gesture == SCISSOR)
                return "scissor";
            else if(_gesture == PUNCH)
                return "punch";
            else if(_gesture == CLOTH)
                return "cloth";
            else if(_gesture == 4)
                return "Quiting Game";
            else
                return "Error!Cant read gesture!(Quiting)";
        };
        string showAiPlan()
        {
            //cout << "Plan: " << _plan << endl;
            if(plan == 1)
                return "Plan A";
            else if(plan == 2)
                return "Plan B";
            else if(plan == 3)
                return "Plan C";
            else if(plan == 4)
                return "Plan D";
            else
                return "Error!Cant read gesture!(Quiting)";
        };
};

//定义用户相关信息
//获取名字和手势
class UserBehavior: public GameObject
{
    public:
        string getUserName(GameObject & Object)
        {
            cout << "Enter your name: " << endl;
            cin >> Object._name;

            string Name = Object._name;
            return Name;
        };
        void getUserGesture(GameObject & Object)
        {
            //cout << "[1]Punch [2]Scissor [3]Cloth [4]QUIT" << endl;
            cin >> Object._gesture;
        };
};

//定义电脑相关信息
//获取名字、手势和策略
//相关手势策略
class AiBehavior: public GameObject
{
    public:
        string getAiName(GameObject & Object)
        {
            Object._name = "AI";
            return "AI";
        };
        void getAiGesture(GameObject & Object)
        {
            int i = rand()%4+1;
            //cout << i << endl;

            switch(i)
            {
                case 1: 
                    Object._plan=planA();
                    Object.plan = 1;
                    break;
                case 2:
                    Object._plan=planB();
                    Object.plan = 2;
                    break;
                case 3: 
                    Object._plan=planC();
                    Object.plan = 3;
                    break;
                case 4: 
                    Object._plan=planD();
                    Object.plan = 4;
                    break;
                default: cout << "Error: switch wroung!";
            }
            Object._gesture = Object._plan; 
            //cout << "Plan: " << _plan << endl;
            //cout << i << endl;
        };

        int planA();
        int planB();
        int planC();
        int planD();
};


//函数定义
//judge函数用于判断胜负
void judge(GameObject & Object1, GameObject & Object2);
//update函数用于各种信息更新
void update(GameObject & Object);

//主程序
int main()
{
    GameObject User;
    UserBehavior UserBehavior;
    

    GameObject AI;
    AiBehavior AiBehavior;
    
    cout << "[]=========================================================================[]" << endl;
    cout << "|| ███╗   ███╗ ██████╗ ██████╗  █████╗      +----------------------------+ ||\n|| ████╗ ████║██╔═══██╗██╔══██╗██╔══██╗     |           ABOUT            | ||\n|| ██╔████╔██║██║   ██║██████╔╝███████║     |  A game design by Volgo.   | ||\n|| ██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║     |   Enjoy your game time!    | ||\n|| ██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║     |                            | ||\n|| ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     |  Designer: VolgoRabgle     | ||" << endl;
    cout << "||     **** *** Game Start! *** ****        |  Form: Ink Blot University | ||" << endl;
    cout << "|| +--------------------------------------+ |  Language: C++             | ||" << endl;
    cout << "|| | Enter the number to use the gesture: | |  Tool: Visual Stdio Code   | ||\n";
    cout << "|| | [1]Punch [2]Scissor [3]Cloth [4]QUIT | |  Version: 1.16             | ||" << endl;
    cout << "|| +--------------------------------------+ +----------------------------+ ||" << endl;
    cout << "[]=========================================================================[]" << endl;

    string user_name = UserBehavior.getUserName(User);
    string ai_name = AiBehavior.getAiName(AI);
    int _round=1;

    do{
        cout << "Round: " << _round << endl;
        cout << "Your gesture: ";

        UserBehavior.getUserGesture(User);
        AiBehavior.getAiGesture(AI);

        if(User._gesture == 1 || User._gesture == 2 ||User._gesture == 3)
        {
            cout << "[" << user_name << "]: " << User.showGesture() << endl;
            cout << "[" << ai_name << " (" << AI.showAiPlan()<< ")" << "]: " << AI.showGesture() << endl;

            judge(User, AI);
            update(User);
            update(AI);
        }
        else
            cout << "Quit" << endl;

        _round++;


    }while(User._gesture == SCISSOR || User._gesture == PUNCH || User._gesture == CLOTH);
    
    cout << "+---------------------------------+" << endl;
    cout << "| Total Round: " << _round << endl;
    cout << "| User Name: " << user_name << endl;
    cout << "|     [scissor] " << User._scissorCount << " total  " << User._scissorWinCount << " win   \n"; 
    cout << "|     [punch]   " << User._punchCount << " total  " << User._punchWinCount << " win   \n";
    cout << "|     [cloth]   " << User._clothCount << " total  " << User._clothWinCount << " win   \n";
    cout << "| User Name: " << ai_name << endl;
    cout << "|     [scissor] " << AI._scissorCount << " total  " << AI._scissorWinCount << " win   \n"; 
    cout << "|     [punch]   " << AI._punchCount << " total  " << AI._punchWinCount << " win   \n";
    cout << "|     [cloth]   " << AI._clothCount << " total  " << AI._clothWinCount << " win   \n";
    cout << "+---------------------------------+" << endl;


    return 0;
}



void judge(GameObject & Object1, GameObject & Object2)
{
    string name1;
    string name2;
    
    if(Object1._gesture == Object2._gesture)
    {
        cout << "平局!\n";
        Object1._win = false;
        Object2._win = false;
        //cout << Object1._win << endl;
        //cout << Object2._win << endl;
    } 
    else if(Object1._gesture > Object2._gesture || (Object1._gesture == SCISSOR && Object2._gesture == CLOTH))
    {
        cout << "[" << Object1._name << "]" << "获得了胜利!  " << "[" << Object2._name << "]" <<"成为人生的败犬!\n";
        Object1._win = true;
        Object2._win = false;
        //cout << Object1._win << endl;
        //cout << Object2._win << endl;
    }
    else if(Object1._gesture < Object2._gesture || (Object2._gesture == SCISSOR && Object1._gesture == CLOTH))
    {
        cout << "[" << Object1._name << "]" << "成为人生的败犬!  " << "[" << Object2._name << "]" <<"获得了胜利!\n";
        Object1._win = false;
        Object2._win = true;
        //cout << Object1._win << endl;
        //cout << Object2._win << endl;
    }
    else
    {
        cout << "Error!" << endl;
        Object1._win = false;
        Object2._win = false;
        //cout << Object1._win << endl;
        //cout << Object2._win << endl;
    }

}

//A方案
//使用随机手势
int AiBehavior::planA()
{
    return rand()%3+1;
}

//B方案
//使用上一次获胜时使用的手势
//如果此前从未获胜过，则使用随机手势
int AiBehavior::planB()
{
    if(_winHistory[0] == '\0')
        return rand()%3+1;
    else
    {
        int n;
        n = _winHistory[0];
        return n;
    }
}

//C方案
//使用目前为止使用次数最少的手势
//如果所有手势使用次数相同，则使用随机手势
int AiBehavior::planC()
{
    //cout << "!!!TEST!!!" << endl;
    int n;
    if(_scissorCount == 0 || _punchCount == 0 || _clothCount ==0)
        n = rand()%3+1;
    else
    {
        if(_scissorCount == _punchCount && _punchCount == _clothCount)
        {
            n = rand()%3+1;
        }
        else if(_scissorCount >= _punchCount)
        {
            n = PUNCH;
            if(_punchCount >= _clothCount)
                n = CLOTH;
        }
        else if(_scissorCount >= _clothCount)
        {
            n = CLOTH;
            if(_clothCount >= _punchCount)
                n = PUNCH;
        }
        else 
        {
            n = SCISSOR;
        }
    }

    return n;
}

//D方案
//使用目前为止胜率最高的手势
//如果胜率相同则使用随机手势
int AiBehavior::planD()
{
    //cout << "!!!TEST!!!" << endl;
    int n;
    if(_scissorCount == 0 || _punchCount == 0 || _clothCount ==0)
        n = rand()%3+1;
    else
    {
        //cout << "!!!TEST!!!" << endl;
        float srate = _scissorWinCount/_scissorCount;
        float prate = _punchWinCount/_punchCount;
        float crate = _clothWinCount/_clothCount;

        if(srate == prate && prate == crate)
        {
            n = rand()%3+1;
        }
        else if(srate <= prate)
        {
            n = PUNCH;
            if(prate <= crate)
                n = CLOTH;
        }
        else if(srate <= crate)
        {
            n = CLOTH;
            if(_clothCount <= prate)
                n = PUNCH;
        }
        else 
        {
            n = SCISSOR;
        }
    }

    return n;
}


//更新函数
//更新各个手势使用次数以及获胜次数
//更新上次获胜时使用的手势
void update(GameObject & Object)
{
    //cout << "Running!" << endl;
    //cout << "!!!TEST: " << Object._gesture << endl;
    //cout << "!!!TEST: " << Object._win << endl;
    if(Object._gesture == 1)
    {
        Object._scissorCount++;
        if(Object._win == true)
        {
            Object._scissorWinCount++;
            //cout << Object._scissorWinCount << endl;
        }
    }
    if(Object._gesture == 2)
    {
        Object._punchCount++;
        if(Object._win == true)
        {
            Object._punchWinCount++;
            //cout << Object._punchWinCount << endl;
        }
    }
    if(Object._gesture == 3)
    {
        Object._clothCount++;
        if(Object._win == true)
        {
            Object._clothWinCount++;
            //cout << Object._clothCount << endl;
        }
    }

    if(Object._win == true)
        Object._winHistory[0] = Object._gesture;
}