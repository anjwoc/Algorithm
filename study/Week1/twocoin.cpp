#include <bits/stdc++.h>
#include <iostream>

using namespace std;
#define endl "\n";

int n,m,ans;
char MAP[21][21];
int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};

vector<pair<int, int>> coin;
int MIN(int a, int b) { if(a<b) return a; return b; }

void Input(){
    ans = 99999999;
    cin>>n>>m;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>MAP[i][j];
            if(MAP[i][j] == 'o'){
                coin.push_back(make_pair(i,j));
            }
        }
    }
}

bool escape(int x, int y){
    return x<0 or x>=n or y<0 or y>=m;
}

void Move(int x1, int y1, int x2, int y2, int cnt, int i){
    if(ans < cnt) return;
    if(cnt > 10){
        ans  = MIN(ans, cnt);
        return;
    }
    int nx1 = x1+dx[i], ny1=y1+dy[i];
    int nx2 = x2+dx[i], ny2=y2+dy[i];

    if(escape(nx1, ny1) and escape(nx2, ny2)) return;
    else if(escape(nx1, ny1)){
        ans = MIN(ans, cnt);
        return;
    }
    else if(escape(nx2, ny2)){
        ans = MIN(ans, cnt);
        return;
    }
    if(MAP[nx1][ny1] == '#'){
        nx1 = x1; ny1 = y1;
    }
    if(MAP[nx2][ny2] == '#'){
        nx2 = x2; ny2 = y2;
    }
    for(int k=0;k<4;k++){
        Move(nx1, ny1, nx2, ny2, cnt+1, k);
    }
}

void solution(){
    for(int i=0;i<4;i++){
        int x1 = coin[0].first;
        int y1 = coin[0].second;
        int x2 = coin[1].first;
        int y2 = coin[1].second;
        Move(x1,y1,x2,y2,1,i);
    }
}
void solve(){
    Input();
    solution();
    if(ans>10) ans = -1;
    cout<<ans<<endl;
}
int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}