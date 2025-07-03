# Overtraining + Compression Stable Diffusion XL Lora 

For this technique, I used the previous technique of image compression with overtraining to further induce glitches into the Lora.  
Usually, the number of times the trainer looks over each image is around 10 repeats per image For this Lora, I set this value to 900, which should massively overfit the data and 
induce artifacts.


# Results 

<p align="center">
  <img src="images/Compressed1.png" alt="Image 1" width="200"/>
  <img src="images/Compressed2.png" alt="Image 2" width="200"/>
  <img src="images/Compressed3.png" alt="Image 3" width="200"/>
  <img src="images/Compressed5.png" alt="Image 3" width="200"/>
</p>

<p align="center">
  <img src="images/Compressed10.png" alt="Image 1" width="200"/>
  <img src="images/Compressed11.png" alt="Image 2" width="200"/>
  <img src="images/Compressed12.png" alt="Image 3" width="200"/>
  <img src="images/Compressed13.png" alt="Image 3" width="200"/>
</p>



