#include<bits/stdc++.h>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	string s;
	getline(cin, s);

	string init;
	vector<string> v;
	string temp;
	for (int i = 0; i < s.length(); i++)
	{
		//공통된 변수형
		if (s[i] == ' ')
		{
			init = temp;
        	temp.clear();
			continue;
		}
		//하나의 추가적인 변수형 + 변수의 이름의 끝
		else if (s[i] == ',')
		{
			v.push_back(temp);
			i++;
			temp.clear();
		}
		//끝
		else if (s[i] == ';')
		{
			v.push_back(temp);
			temp.clear();
		}
		else
			temp += s[i];
	}

    for(int i=0;i<v.size();i++){
        int idx=-1;
        for(int j=0;j<v[i].size();j++)
            if(!((v[i][j]>='a' && v[i][j] <='z') || (v[i][j]>='A' && v[i][j]<='Z'))){
                idx = j;
                break;
            }
            cout<<init;
            if(idx==-1){
                cout<<" "<<v[i];
            }

            else{
                for(int j=v[i].size()-1;j>=idx;j--){
                    if(v[i][j] == ']'){
                        cout<<"[]";
                        j--;
                        continue;
                    }
                    cout<<v[i][j];
                }
                cout<<" ";
                for(int j=0;j<idx;j++)
                    cout<<v[i][j];
                
                
            }
            cout<<";\n";
    }

	return 0;
}