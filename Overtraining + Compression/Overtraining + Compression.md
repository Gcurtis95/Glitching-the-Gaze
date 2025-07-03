# Overtraining + Compression Stable Diffusion XL Lora 

For this technique, I used the previous technique of image compression with overtraining to further induce glitches into the Lora.  
Usually, the number of times the trainer looks over each image is around 10 repeats per image For this Lora, I set this value to 900, which should massively overfit the data and 
induce artifacts.


# Results 

<p align="center">
  <img src="images/Compressed4.png" alt="Image 1" width="200"/>
  <img src="images/Compressed6.png" alt="Image 2" width="200"/>
  <img src="images/Compressed7.png" alt="Image 3" width="200"/>
  <img src="images/Compressed8.png" alt="Image 3" width="200"/>
  <img src="images/Compressed9.png" alt="Image 3" width="400"/>
</p>




