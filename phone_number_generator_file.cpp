#include <iostream>
#include <random>
#include <chrono>
#include <stdio.h>

using namespace std;

/*
 *Random phone number generator
 */

default_random_engine dre (chrono::steady_clock::now().time_since_epoch().count());     // provide seed
int random (int lim)
{
    uniform_int_distribution<int> uid {0,lim};   // help dre to generate nos from 0 to lim (lim included);
    return uid(dre);    // pass dre as an argument to uid to generate the random no
}

void generate_number() {
	int a;
	int b;
	int nun[9];
	int net[4]={1,2,3,6};
	nun[0]=9;

	for (int i=1 ; i<=8 ; i++) { 
		if (i==1) {
		b=random(3) ;
	 	nun[i]=net[b] ;
	       	}
	       	else {
	 	a=random(9);
		nun[i]=a;
		}	
	}

//	cout << nun <<endl ;

	for (int l=0 ; l<=8 ; l++) {
	//	cout << nun[l] ;
		printf ("%d", nun[l]);			
		//cout << endl;
	}

	printf ("\n");
//	return 0;


}

int main () {


	for (int i=0 ; i<=1000; i++)
	{
	
		generate_number();
	
	}

	return 0;	
}


