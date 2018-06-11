class GameObject 
{
    public:
        int gesture;//定义手势
        int round;//定义回合数，计算概率用
        double winRate;//定义用户或AI的获胜概率

        void update();//更新数据，用于AI策略
        string showGesture();//显示手势
};



class UserBehavior: public GameObject 
{
    public: 
        void getUesrGesture();
        //获取用户的手势
};



class AiBehavior: public GameObject
{
    public:
        //计算AI各手势使用次数，用于策略计算
        int scissorCount;
        int punchCount;
        int clothCount;

        //AI各手势获胜次数，用于策略计算
        int scissorWinCount;
        int punchWinCount;
        int clothWinCount;


        //记录AI历史记录，用于策略
        int winHistory[100];


        //获取AI手势
        void getAiGesture();


        //AI策略
        int planA();
        int planB();
        int planC();
        int planD();
};


//获取AI手势，使用随机函数决定使用哪种策略
void AiBehavior::getAiGesture()
{
    int plan = rand()%5;
    int n;
    switch(plan)
    {
        case 1: n=this->planA();
        case 2: n=this->planB();
        case 3: n=this->planC();
        case 4: n=this->planD();
        default: cout << "Error: switch wroung!";
    }
    this->gesture = n;
}

[]=========================================================================[]
|| ███╗   ███╗ ██████╗ ██████╗  █████╗      +----------------------------+ ||
|| ████╗ ████║██╔═══██╗██╔══██╗██╔══██╗     |           ABOUT            | ||
|| ██╔████╔██║██║   ██║██████╔╝███████║     |  A game design by Volgo.   | ||
|| ██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║     |   Enjoy your game time!    | ||
|| ██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║     |                            | ||
|| ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     |  Designer: VolgoRabgle     | ||
||     **** *** Game Start! *** ****        |  Form: Ink Blot University | ||
|| +--------------------------------------+ |  Language: C++             | ||
|| | Enter the number to use the gesture: | |  Tool: Visual Stdio Code   | ||
|| | [1]Punch [2]Scissor [3]Cloth [4]QUIT | |  Version: 1.16             | ||
|| +--------------------------------------+ +----------------------------+ ||
[]=========================================================================[]
游戏主界面