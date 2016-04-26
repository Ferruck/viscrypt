#viscrypt

Simple tool for creating (2,2) visual cryptography schemes. These are described by various authors, first by [Naor & Shamir (1994)](http://www.cs.nccu.edu.tw/~raylin/UndergraduateCourse/ComtenporaryCryptography/Spring2009/VisualCrypto.pdf).

I've written this tool because the only other application I found online was a `jar`.

##Usage

    python3 viscrypt.py IMAGE_NAME
    
This will create two images, `IMAGE_NAME_share1.png` and `IMAGE_NAME_share2.png`.

##Notes

* Pixel expansion is not handled in any way. Therefore the resulting shares will be twice the height of the original image.

* The produced shares have no transparency. Use tools like GIMP to turn the white pixels into transparent pixels.

* Your input image will be converted to black and white (not grayscale!) with dithering. Nevertheless you shouldn't try this with full colored images, their contrast will possibly be to low.

* I've only tested this with Python 3, Python 2 could work though.

##License

MIT-License (see the `LICENSE` file for details).
