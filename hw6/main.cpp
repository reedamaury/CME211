#include <boost/multi_array.hpp>
#include <iostream>
#include <string>

#include "hw6.hpp"
#include "image.hpp"

using namespace std;

int main()
{
    image img("stanford.jpg");
    unsigned int sharpness = img.Sharpness();
    cout<<"Original Image: "<<sharpness<<" ";


    for(unsigned int i=3; i<28; i+=4){
	  image im("stanford.jpg");
          im.BoxBlur(i);
          unsigned int sharp = im.Sharpness();
          cout<< "BoxBlur( " << i << "): " << sharp <<" ";

	  std::string num_string = std::to_string(i);
	  while (num_string.length() < 2)
              num_string = "0" + num_string;
          std::string output_string = "BoxBlur" + num_string + ".jpg";
          im.Save(output_string);
    }
    return 0;
}
