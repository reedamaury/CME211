The provided code includes an Image class that has methods for reading and writing JPEG images, as well as applying
convolution kernels to blur images and obtain the sharpness of an image. The Image class has a constructor that takes
in the name of a JPEG file as the sole input argument and uses the ReadGrayscaleJPEG function from hw6.hpp and hw6.cpp
to read the image data from the file. The Image class also includes a Save method that writes the current version of
the image to a JPEG file using the WriteGrayscaleJPEG function from hw6.hpp and hw6.cpp.

The Image class includes a Convolution function that can be used to apply a convolution kernel to an image. The
Convolution function takes three arguments: input, output, and kernel, where input and output are 2D boost arrays
containing the input and output image data, respectively, and kernel is a 2D array containing the convolution kernel to
be applied to the image data. The Convolution function will return an error for kernel arrays that are not odd-sized,
square, and of at least size 3.

The Image class also includes a BoxBlur method that uses the Convolution function to apply a box blur to an image. This
method takes one argument specifying the kernel size and proceeds to generate a kernel of ones, normalized by the number
of elements in the kernel. Additionally, the Image class includes a Sharpness method that returns an unsigned int
representing the sharpness of the image. This method uses a Laplacian kernel to approximate the Laplacian operator, and
inputs it into the Convolution function. The Convolution function then overwrites the input image array, as it is passed
by reference to the function. Lastly, the standard library max element method was utilized to iterate through the array
and find the largest element, which corresponds to the sharpness of the image.