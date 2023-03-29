#ifndef IMAGE_HPP
#define IMAGE_HPP

#include <boost/multi_array.hpp>
#include <iostream>

/*
*the image class performs blurring and sharpening of images using 2D convolution. it
*contains a method for saving the output of the blurred or sharpened image. 
*/
void Convolution(boost::multi_array<unsigned char, 2>& input,
                     boost::multi_array<unsigned char, 2>& output,
                     boost::multi_array<float, 2>& kernel);
class image {
    // declare public members/attributes
    private:
    boost::multi_array<unsigned char, 2>  input_img_arr; 
    std::string input_jpgfile;

    public:
    image(std::string input_jpgfile);  // constructor 
    void Save(std::string output_jpgfile); // save method
    void BoxBlur(unsigned int k_size); // blurring method
    unsigned int Sharpness(); // sharpness method 
};

#endif /* IMAGE_HPP */
