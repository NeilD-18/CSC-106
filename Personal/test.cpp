#include <iostream>
#include <vector> 

using namespace std; 

int main() {
    vector<int> data = {2,5,4,1,3};
    
    cout << data[0] << data[1] << data[2] <<  data[3]  <<  data[4] << endl << data.size();


    for (int i = 0, max = data.size() - 1 ; i < max ; i++) {
        
        for (int j = 0; j < max - i; j++)

        
             if (data[j] > data[j+1]){ 
                int temp = data[j+1]; 
                data[j+1] = data[j];
                data[j] = temp;  
             }
       

    } 
    

    cout << data[0] << data[1] << data[2] <<  data[3]  <<  data[4] << endl << data.size();
    
} 