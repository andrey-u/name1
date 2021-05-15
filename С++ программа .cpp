#include <iostream>
#include <locale>
#include <cmath>
#include <string>

using namespace std;

class log1
{
    public:
    bool x1, x2,x3;
    log1(bool x4, bool x5, bool x6)
    {
        x1=x4;
        x2=x5;
        x3=x6;
    }
    bool y1()
    {
        if (x1&&x2) return true;
        else return false;
    }
    bool y2()
    {
        if (x2||x3) return false;
        else return true;
    }
    
    
};

int main()
{
    setlocale(LC_ALL, "Russian");
    cout << "Выполнял работу: " << "Уманский Андрей Александрович\n";
	cout << "Группа: " << "ИС-29\n";
	cout << "Задание: " << "Напишите класс, описывающий логическую схему с тремя входами и двумя выходами.\n";
	cout << "      ____                       "<<endl;
	cout << "x1___| &  |_________y1           "<<endl;
	cout << "x2___|    |                      "<<endl;
	cout << "   | |____|                      "<<endl;
	cout << "   |    ___                      "<<endl;
	cout << "   |   |   |                     "<<endl;
	cout << "   |___| 1 |o_______y2           "<<endl;
	cout << "x3_____|___|                     "<<endl;
	
    bool x1, x2, x3;
    cout<<"введите 3 значения типa bool через пробел:";
    cin>>x1>>x2>>x3;
    log1 x(x1,x2,x3);
    cout<<"выход 1:"<<x.y1()<<endl;
    cout<<"выход 2:"<<x.y2()<<endl;
    system ("pause");
    return 0;
}








