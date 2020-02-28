#include<bits/stdc++.h>
#define int long long
#define endl '\n'
using namespace std;

bool compare(pair<int,int> p1, pair<int,int> p2)
	{
		return p1.first>p2.first;
	}

int32_t main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n=4;
	int total_time;
	cin>>total_time;
	map<int,int> time_alloted;
	int num_cars[n];
	vector<pair<int,int>> prior;
	for(int e=0;e<n;e++)
	{
		prior.push_back(make_pair(0,-1));
	}
	bool islane[n];
	memset(islane,true,sizeof(islane));
	int q;cin>>q;
	for(int k=0;k<q;k++)
		{	
			int not_executing=-1;
			int t=total_time;
			for(int i=0;i<n;i++)
				{
					cin>>num_cars[i];
					prior[i].first=num_cars[i];
					prior[i].second=i;

				}
			
			sort(prior.begin(),prior.end(),compare);
			
			int tfactor=0;
			for(int i=0;i<n;i++)
				if(islane[i]==true)
					tfactor+=num_cars[i];
			cout<<"initial time factor"<<" "<<tfactor<<endl;
			int count=0;
			while(t)
			{	
				
				for(auto x:prior)
					{
						if(islane[x.second]==false)
							time_alloted[x.second]=0;
						if(islane[x.second]==true)
						{	
							time_alloted[x.second]=(x.first*t/tfactor);
							tfactor-=x.first;
							t-=time_alloted[x.second];
							count++;
							if(tfactor==0)
								t=0;
							

						}
						if(count==4 && k==0){
							islane[x.second]=false;
							not_executing=x.second;
						}
						
						else if(count==3 && k!=0){
							islane[x.second]=false;
							not_executing=x.second;
						}

						
					}
			}



			for(auto x:prior)
				if(x.second!=not_executing)
					islane[x.second]=true;
		
			for(auto a:time_alloted)
				cout<<a.first<<" "<<a.second<<endl;

			cout<<"Time successfully assigned"<<endl;
		}
		
		return 0;
}