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

# Generation 

# Generation

**Settings:**

Sampler: DPM++ 2M or Euler Sampling Steps: 20 CFG Scale: 7

**Example Prompts:**

Again, for the prompting, I used some of the captions provided with the images with no negative prompting to try and make it as glitchy as possible. 

It seems the longer the prompt, the unstable the generation becomes. 

I tried generating with multiple different aspect ratios to bring out the compression artifacts. 

E.G 

1088x896, 

1152x896 

1216x832 

1344x768 

1472x704 

1536x640 

1856x512 





