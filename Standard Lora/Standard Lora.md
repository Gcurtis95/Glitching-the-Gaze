# Standard Stable Diffusion XL Lora

Standard Stable Diffusion XL Lora to reproduce the training data without purposefully inducing glitches. Preprocessed the data by cropping every image to portrait 832 x 1216 and landscape 1216 x 832, and then set the maximum training resolution
to the same dimensions. This was the initial starting point to see how well the Lora would learn the style from the data and test the text encoding from the captions. 


This model was trained for 8000 Steps. 


# Results



<p align="center">
  <img src="Images/00005-1646839441.png" alt="Image 1" width="200"/>
  <img src="Images/00006-3563745523.png" alt="Image 2" width="200"/>
  <img src="Images/00018-739547882.png" alt="Image 3" width="200"/>
  <img src="Images/00051-1642012496.png" alt="Image 3" width="200"/>
</p>

<p align="center">
  <img src="Images/00070-3028708566.png" alt="Image 1" width="200"/>
  <img src="Images/00075-2631125681.png" alt="Image 2" width="200"/>
  <img src="Images/00094-2311889615.png" alt="Image 3" width="200"/>
  <img src="Images/standard3.png" alt="Image 3" width="200"/>
</p>


<p align="center">
  <img src="Images/standard1.png" alt="Image 1" width="400"/>
  <img src="Images/standard 2.png" alt="Image 2" width="400"/>
</p>


# Generation

**Settings:**

Sampler: DPM++ 2M or Euler 
Sampling Steps: 20
CFG Scale: 7

**Example Prompts:**


For the prompting, I used some of the captions provided with the images eg:

"A young, white woman with heavily teased platinum-blonde hair kneels on an office chair, her body angled provocatively towards the camera. She wears a beige t-shirt and extremely a short metallic bronze skirt, with thigh-high brown boots style sandals. The background is a dark, nondescript studio space, spotlighted from above, casting hard shadows. Her exaggerated hairstyle dominates the frame, styled in a way reminiscent of 1980s glamour tropes. Her makeup is heavy, particularly around the eyes and mouth. The t-shirt’s plainness contrasts with the shorts’ high shine, making her body the focal point through both exposure and contrast. The lighting and styling play with high sexualisation, inviting visual consumption of the model’s youthful body. The pose and styling hark back to earlier pin-up visual languages while repackaging them for fashion editorial. This image draws on retro-sexual archetypes, placing hyper-femininity in an ironic, object-centric frame.  The straight hair, youthful and toned skin, perfect lean body align with Eurocentric ideals. "


I also used chat gbt to generate a prompt from some of the images provided eg:

Prompt:

"A tall, elegant fashion model stands confidently on a platform over a reflective lake, surrounded by striking beige rock formations under a clear blue sky. She wears a sculptural, strapless black mini dress with dramatic ruched fabric and a bold, plunging neckline that accentuates her silhouette. Her long legs are emphasized by sheer black tights and high heels. The lighting is sharp and natural, casting crisp shadows and reflecting the mountainous landscape in the still water. Her hair is slicked back and wet, enhancing the modern, sleek aesthetic. Editorial fashion photography, minimalist composition, natural textures, high contrast, confident and empowering mood. "


Negative Prompt: 

"blurry, unnatural lighting, low resolution, extra limbs, distorted anatomy, unrealistic fabric, poor reflections, cartoonish textures, unflattering pose, bad proportions, washed out colors"


# Notes

In these cases the negative prompt helped keep the model from generating images with extra limbs and wrong anatomy. And overall, produced the style of the training data pretty well. 

To induce glitches during generation with this Lora don't use a negative prompt and mess around with the generation configs like reducing or adding sampling steps and increase/decrease cfg scale.



# Technical 


![output](https://github.com/user-attachments/assets/7475db5e-3499-4cd4-b07a-b545175b2dc7)


The training loss generally decreases, which is expected during training.

Some regions show very small changes in the smoothed loss, indicating plateaus — where the model might not be learning much.













