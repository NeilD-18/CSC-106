#include <iostream> 
#include <stdlib.h>
#include <vector> 



#define ll long long 

using namespace std; 

vector<int> bubbleSort(vector<int> array) { 
   
   for (int i = 0, max = array.size() - 1 ; i < max ; i++ ) { 

      for (int j = 0; j < max - i; j++){

         if (array[j] > array[j+1]) { 

            int temp = array[j+1];
            array[j+1] = array[j];
            array[j] = temp; 


         }

      }
   
   } 

   return array; 
      
} 
     

void print(vector<int> arr) { 
   for (int i = 0, max = arr.size(); i < max; i++) {
      cout << arr[i] << " "; 
   }
}



int main(){ 

   ll n; 
   ll x;
   vector<int> array; 

   cin >> x; 

   for (int i = 0; i < x; i ++) { 
      cin >> n; 
      array.push_back(n); 
   }
   bubbleSort(array);
   print(bubbleSort(array));
}