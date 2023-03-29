#include <algorithm>
#include <boost/multi_array.hpp>
#include <iostream>

#include "hw6.hpp"
#include "image.hpp"

void Convolution(boost::multi_array<unsigned char, 2>& input,
                     boost::multi_array<unsigned char, 2>& output,
                     boost::multi_array<float, 2>& kernel){
                        
                        // size of input img 
                        int nr_img = input.shape()[0];
                        int nc_img = input.shape()[1];
                        
                        // size of kernel
                        int nr_k = kernel.shape()[0];
                        int nc_k = kernel.shape()[1];
                        
                        // if kernel even size, square, or size < 3, return error
                        if (nr_k%2==0 or nr_k!=nc_k or nr_k<3) {
                            std::cout<<"Kernel Argument Error: Kernel must be a square matrix with a size that is odd and greater than 3"<<std::endl;
                            return;
                        }

                        // flip kernel 
                        boost::multi_array<float, 2> kernel_flip(boost::extents[nr_k][nc_k]); // declare flipped kernel
                        for(int n=0; n<nr_k; ++n){
                            for(int m=0; m<nc_k; ++m){
                                kernel_flip[n][m] = kernel[(nr_k-1)-n][(nc_k-1)-m];
                            }
                        }

                        // sum the products of input image and kernel for each pixel
                        for(int i=0; i<nr_img; ++i){
                            for(int j=0; j<nc_img; ++j){
				float sum = 0;
                                for (int n=0; n<nr_k; ++n){
                                    for(int m=0; m<nc_k; ++m){
                                        int img_i = i - nr_k/2 + n; // image row idx multipication
                                        int img_j = j - nc_k/2 + m; // image col idx for multipication

                                        // handle out of bounds entries by duplicating edge elements
                                        if (img_i < 0) {
                                            img_i = 0;
                                        }
                                        if (img_i >= nr_img){
                                            img_i = nr_img-1;
                                        }
                                        if (img_j < 0) {
                                            img_j = 0;
                                        }
                                        if (img_j >= nc_img){
                                            img_j = nc_img-1;
                                        }

                                        // sum products and assign to output
                                        sum += int(input[img_i][img_j])*kernel_flip[n][m];
                                    }
                                }
				if(sum > 255){
				    output[i][j] = 255;
				}
				if(sum < 0){
				    output[i][j] = 0;
				}
				else {
				output[i][j] = int(sum);
          			}
                            }
                        }
			input = output;
                        return;
                     }


    // constructor
    image::image(std::string input_jpgfile) {
         ReadGrayscaleJPEG(input_jpgfile, input_img_arr);
         this->input_jpgfile = input_jpgfile;
    }

    // save method (pass by value is fine here)
    void image::Save(std::string output_jpgfile){
        if (output_jpgfile.empty()) {
            WriteGrayscaleJPEG(input_jpgfile, input_img_arr);
        }
        else {
            WriteGrayscaleJPEG(output_jpgfile, input_img_arr);
        }
    }

    // blurring method
    void image::BoxBlur(unsigned int k_size) { 
        // create kernel
        boost::multi_array<float, 2> kernel(boost::extents[k_size][k_size]);
        float numel = k_size*k_size;
        for(unsigned int k=0; k<k_size; ++k){
            for(unsigned int l=0; l<k_size; ++l){
                kernel[k][l] = 1./numel;
            }
        }

        // declare output image array
        unsigned int nr = input_img_arr.shape()[0];
        unsigned int nc = input_img_arr.shape()[1];
        boost::multi_array<unsigned char, 2> output_img_arr(boost::extents[nr][nc]);

	// use convolution to blur input image and store to output image
        Convolution(input_img_arr, output_img_arr, kernel);
	return;
    }

    // sharpness method
    unsigned int image::Sharpness() {
        // create Laplacian kernel
        boost::multi_array<float, 2> kernel(boost::extents[3][3]);
        kernel[0][0] = 0;
        kernel[0][1] = 1;
        kernel[0][2] = 0;
        kernel[1][0] =1;
        kernel[1][1] =-4;
        kernel[1][2] =1;
        kernel[2][0] =0;
        kernel[2][1] =1;
        kernel[2][2] =0;

        // declare output image array
        unsigned int nr = input_img_arr.shape()[0];
        unsigned int nc = input_img_arr.shape()[1];
        boost::multi_array<unsigned char, 2> output_img_arr(boost::extents[nr][nc]);

	// use convolution to compute sharpness
        Convolution(input_img_arr, output_img_arr, kernel);
	// maximum element of convolution output
        unsigned char* sharpness = std::max_element(input_img_arr.data(), input_img_arr.data()+input_img_arr.num_elements());
        unsigned int s = *sharpness;
        return s;
    }
