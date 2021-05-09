#include <iostream>
#include <locale>
#include <cmath>
#include <string>

using namespace std;

double parall(double x, double y)
{
    double z=0;
    z=x+y;
    return z;
}

double posled(double x, double y)
{
    double z=0;
    z=(x*y/(x+y));
    return z;
}

int main()
{
    setlocale (LC_ALL, "Russian");
    cout << "Выполнял работу: " << "Уманский Андрей Александрович\n";
	cout << "Группа: " << "ИС-29\n";
	cout << "Задание: " <<"определение ёмкости участка цепи А-В\n";
	cout<<"            C1             C2      C3"<<endl;
	cout<<"         ___||___       ___||______||___"<<endl;
	cout<<"        |   ||   |     |   ||      ||   |"<<endl;
	cout<<"    A___|        |_____|                |_____B"<<endl;
	cout<<"        |   C4   |     |   C5      C6   |"<<endl;
	cout<<"        |___||___|     |___||______||___|"<<endl;
	cout<<"            ||             ||      ||     "<<endl;
    int i;
    double C[6], result[5], answer;
    for (i=0; i<6; i++)
    {
        cout<<"введите емкость "<<i+1<<"-го конденсатора:";
        cin>>C[i];
    }
    while ((C[0]<0)||(C[1]<0)||(C[2]<0)||(C[3]<0)||(C[4]<0)||(C[5]<0))
    {
        cout<<"введены некорректные данные, попробуйте снова!"<<endl;
        for (i=0; i<6; i++)
        {
            cout<<"введите емкость "<<i+1<<"-го конденсатора:";
            cin>>C[i];
        }
    }
    i=-1;
    result[0]=parall(C[i+1],C[i+4]);//1 действие
    cout<<endl<<"1:"<<result[0]<<endl;
    result[1]=posled(C[i+2],C[i+3]);//2 действие
    cout<<"2:"<<result[1]<<endl;
    result[2]=posled(C[i+5],C[i+6]);//3 действие
    cout<<"3:"<<result[2]<<endl;
    result[3]=parall(result[1],result[2]);//4 действие
    cout<<"4:"<<result[3]<<endl;
    result[4]=posled(result[0],result[3]);//5 действие
    cout<<"5:"<<result[4]<<endl;
    answer=result[4];
    cout<<"ответ:"<<answer;
    system("pause");
    
}
