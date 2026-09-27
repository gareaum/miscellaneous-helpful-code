/*
#include <iostream>
#include <vector>
#include <algorithm>

int leftchild(std::vector<float> &H,int i){
    int lc;
    lc = (2*i) + 1;
    return lc;
}

int rightchild(std::vector<float> &H, int i){
    int rc;
    rc = (2*i) + 2; 
    return rc;
}

int parent(std::vector<float> &H, int i){
    int p;
    
    if (i == 0){
        return 0;
    }

    p = (i-1)/2;

    return p;
}

void sift_up(std::vector<float> &H){
    int position = H.size()-1;
    while( (position != 0) && (H[parent(H, position)] > H[position]) ){
        std::swap(H[parent(H, position)], H[position]);
        position = parent(H, position);
    }
}

void sift_down(std::vector<float> &H,int position){
    int size = H.size();

    while (true){ 
            int LC = leftchild(H, position);
            int RC = rightchild(H, position);
            
            if (LC >= size){
                break;
            }
           
            //Only left child
            if (RC >= size){
                if (H[LC] < H[position]) {      
                    std::swap(H[LC], H[position]);
                    position = LC;
                }

                else{
                    break;
                }
            }
            
            else{
                int smaller = (H[LC] < H[RC]) ? LC : RC;

                if(H[smaller] < H[position]){
                    std::swap( H[smaller], H[position]);
                    position = smaller;
                }

        
                else{
                    break;
                }
            }
        }
}

void insert(std::vector<float> &H, float value){
    H.push_back(value);
    sift_up(H);
}

void extract(std::vector<float> &H){
    std::swap(H.front(), H.back());
    H.pop_back();
    sift_down(H,0);
}

void Heapify(std::vector<float> &H){
    int size = H.size();

    for (int i = (size/2 - 1); i >= 0; i--){
        sift_down(H,i);
    }
}

void heap_sort(std::vector<float> &H){
    Heapify(H);
    int size = H.size();

    std:: cout << "size: " << size << std::endl;

    while(size > 0){
        std::swap( H[0], H[size - 1] );
        size--;

        if (size == 0){
            break;
        }

        std::vector<float> SH(H.begin(), H.begin() + size);
        Heapify(SH);
        
        for (int j = 0; j < size; j++){
            H[j] = SH[j];
        }
    }

    std::reverse(H.begin(), H.end());
}

*/