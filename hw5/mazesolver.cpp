#include<iostream>
#include<fstream>

// define constants to size of the static array
#define ni 210
#define nj 210

using namespace std; 

int main(int argc, char* argv[])
{
  // ensure appropriate number of command line arguments are provided
  if (argc < 2) {
      cout<<"Not enough command line arguments"<<endl;
      return 0;  // exit the program if not enough
  }
  
  // ensure static array has enough space to store the maze
  ifstream f(argv[1]);
  if(f.is_open()) {
      int nif, njf;
      f >> nif >> njf; // read the first row and column of input file (maze size)
      if (nif > ni or njf > nj) {
          std::cout<<"Not enough storage available" << std::endl;
          return 0; // exit the program if not enough storage 
        }
        
        
    // declare static array to size of biggest maze
    int maze[ni][nj];
    
    // initialzie maze to 0's
    maze[nif][njf] = {0};
    
    // populate maze with 1's where a wall exist
    int i,j;
    while(f>>i>>j){
        maze[i][j]=1;
    }
    f.close();
    
    // find the first 0 in the first row to enter the maze
    int x,y;
    for (j=0;j<njf;j++){
       if (maze[0][j] == 0) {
           x = j;
           y = 0;
           break; 
       }
    }    
    
    // initialize heading to south 
    int heading = 0;
    
    // manuever through maze via right hand algorithm
    ofstream fo(argv[2]);
    if (fo.is_open()) {
        fo<<y<<" "<<x<<endl; // store first position to output file 
        while (y < nif-1) {
            if(heading == 0) { // south
                if(maze[y][x-1]==0) {
                    heading = 1; // west
                    x = x-1;
                    y = y; 
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y+1][x]==0) {
                    heading = 0; // south
                    x = x; 
                    y = y+1;
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y][x+1]==0){
                    heading = 3; // east
                    x = x+1; 
                    y = y;
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y-1][x]==0){
                    heading = 2; // north
                    x = x;
                    y = y-1; 
                    fo<<y<<" "<<x<<endl;
                }
            }
            if(heading == 1) { // west
                if(maze[y-1][x]==0) {
                    heading = 2; // north
                    x = x;
                    y = y-1; 
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y][x-1]==0) {
                    heading = 1; // west
                    x = x-1; 
                    y = y;
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y+1][x]==0){
                    heading = 0; // south
                    x = x; 
                    y = y+1;
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y][x+1]==0){
                    heading = 3; // east
                    x = x+1;
                    y = y; 
                    fo<<y<<" "<<x<<endl;
                }
            }
            if(heading == 2) { // north
                if(maze[y][x+1]==0) {
                    heading = 3; // east
                    x = x+1;
                    y = y; 
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y-1][x]==0) {
                    heading = 2; // north
                    x = x; 
                    y = y-1;
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y][x-1]==0){
                    heading = 1; // west
                    x = x-1; 
                    y = y;
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y+1][x]==0){
                    heading = 0; // south 
                    x = x;
                    y = y+1; 
                    fo<<y<<" "<<x<<endl;
                }
            }
            if(heading == 3) { // east
                if(maze[y+1][x]==0) {
                    heading = 0; // south
                    x = x;
                    y = y+1; 
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y][x+1]==0) {
                    heading = 3; // east
                    x = x+1; 
                    y = y;
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y-1][x]==0){
                    heading = 2; // north
                    x = x; 
                    y = y-1;
                    fo<<y<<" "<<x<<endl;
                }else if(maze[y][x-1]==0){
                    heading = 1; // west
                    x = x-1;
                    y = y; 
                    fo<<y<<" "<<x<<endl;
                }
            }
        }
    }
    }
}
