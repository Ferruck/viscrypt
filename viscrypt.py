# The MIT License (MIT)
# Copyright (c) 2016 Philipp Trommler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import argparse
import random

from PIL import Image


def two_of_two(filename):
    """Generates a (2,2) visual cryptography scheme."""
    original = Image.open(filename)
    
    original = original.convert("1")
    o_pixels = original.load()
    
    first = Image.new("1", (original.size[0], original.size[1] * 2))
    f_pixels = first.load()
    
    second = Image.new("1", (original.size[0], original.size[1] * 2))
    s_pixels = second.load()
    
    for i in range(original.size[0]):
        for j in range(original.size[1]):
            if o_pixels[i,j] == 0:
                if random.randint(0, 1):
                    f_pixels[i,j * 2    ] = 1
                    f_pixels[i,j * 2 + 1] = 0
                    s_pixels[i,j * 2    ] = 0
                    s_pixels[i,j * 2 + 1] = 1
                else:
                    f_pixels[i,j * 2    ] = 0
                    f_pixels[i,j * 2 + 1] = 1
                    s_pixels[i,j * 2    ] = 1
                    s_pixels[i,j * 2 + 1] = 0
            else:
                if random.randint(0, 1):
                    f_pixels[i,j * 2    ] = 0
                    f_pixels[i,j * 2 + 1] = 1
                    s_pixels[i,j * 2    ] = 0
                    s_pixels[i,j * 2 + 1] = 1
                else:
                    f_pixels[i,j * 2    ] = 1
                    f_pixels[i,j * 2 + 1] = 0
                    s_pixels[i,j * 2    ] = 1
                    s_pixels[i,j * 2 + 1] = 0
    
    first.save(filename + "_share1.png")
    second.save(filename + "_share2.png")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE", help="The image to encrypt")
    args = parser.parse_args()

    two_of_two(args.IMAGE)
