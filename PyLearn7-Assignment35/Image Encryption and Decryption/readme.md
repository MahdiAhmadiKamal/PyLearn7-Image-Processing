# Image Encryption and Decryption 🔐
**Image Encryption** is the process of converting a normal image into a cipher image using a secret key in such a way that unauthorized users can't access it.
**Image Decryption** is the process of converting the cipher image into the original image by employing the secret key. Mainly, decryption operation is like encryption operation but applies in reverse order.

## How to Install
Run following command:
```
pip install -r requirements.txt
```

## How to Run
Execute this command in terminal:
```
python encryptor.py
```
```
python decryptor.py
```

## Result

### Input
<img src="enc_input\Mona Lisa.jpg" width="343.5" height="512">

### After Encryption
<img src="enc_output\encrypted_image.bmp" width="343.5" height="512">

### After Decryption
<img src="dec_output\decrypted_image.jpg" width="343.5" height="512">


## Python
This program is written using [Python](https://www.python.org/) language and [OpenCV](https://opencv.org/), whick is a library of programming functions for real-time computer vision, image processing, and machine learning.

<img src="opencv.webp" width="262.5" height="124.75">