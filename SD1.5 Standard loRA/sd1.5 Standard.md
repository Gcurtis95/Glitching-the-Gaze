# Stable Diffusion 1.5 Standard loRa

This loRA was trained on cropped 832 x 1216 portrait and vice versa landscape images for stable diffusion 1.5 for 3 epochs. Trying to get the loRA to replicate the style as with SDXL. 
I experimented with inducing glitches into the generation by using low sampling steps.  Below are some results from experiments where the sampling step was changed from 5 to 21 in increments. 


# Results


<p align="center">
<img src="images/all3_5.png" alt="Image 5" width="200"/>
<img src="images/all3_6.png" alt="Image 6" width="200"/>
<img src="images/all3_7.png" alt="Image 7" width="200"/>
<img src="images/all3_8.png" alt="Image 8" width="200"/>
<img src="images/all3_9.png" alt="Image 9" width="200"/>
<img src="images/all3_10.png" alt="Image 10" width="200"/>
<img src="images/all3_11.png" alt="Image 11" width="200"/>
<img src="images/all3_12.png" alt="Image 12" width="200"/>
<img src="images/all3_13.png" alt="Image 13" width="200"/>
<img src="images/all3_14.png" alt="Image 14" width="200"/>
<img src="images/all3_15.png" alt="Image 15" width="200"/>
<img src="images/all3_16.png" alt="Image 16" width="200"/>
<img src="images/all3_17.png" alt="Image 17" width="200"/>
<img src="images/all3_18.png" alt="Image 18" width="200"/>
<img src="images/all3_19.png" alt="Image 19" width="200"/>
<img src="images/all3_20.png" alt="Image 20" width="200"/>
<img src="images/all3_21.png" alt="Image 21" width="200"/>
</p>


# Generation 


Sampling Method: DPM++ 2M
CFG Scale 7:
Width: 832 pixels
Height: 1216 pixels
Sampling Steps: 5 - 21


all of the above images were created with the same prompt:

"The fashion image features two white slim, female models posed in a controlled, interior studio setting. The background includes a white upholstered sofa and a white shag carpet, contributing to a carefully curated, hyper-clean and stylised domestic space. Both models wear minimal clothing, matching snakeskin or animal print swimsuits with extreme cut-outs that expose the chest, midriff, hips, and upper thighs. Their legs are prominently displayed and elongated by high-heeled shoes in neutral tones.

One model kneels on the carpeted floor with her torso upright, hands positioned around a branded handbag. Her gaze is direct, lips slightly parted, and she wears bright red lipstick, a bold accent that stands out in the otherwise desaturated palette. The other model’s head is cropped out of frame, and the image focuses on her legs and hands, directing the viewer’s attention to her skin, the handbag, and the accessories she wears. Both women wear red polished manicures and large bangles, signalling attention to detail and luxury grooming.  The lighting is bright and evenly distributed, removing shadow and producing a flat, hyper-real surface effect that enhances the clarity of skin texture, garment detail, and the sheen of the handbags and shoes. The lighting is frequently evokes clarity, perfection and accessibility, while flattening depth and softening imperfections.  The use of red is limited to the model’s lipstick and nail varnish, but its role is highly strategic. As a concentrated visual accent, red here connotes attraction, erotic charge and confidence. Its placement on the lips reinforces their sensuality and supports the portrayal of the model as a desirable, high-status object. In visual marketing, red has long been associated with heightened visibility and symbolic value, especially when paired with whiteness, which connotes purity, wealth and cleanliness.  The image promotes aspirational values through a combination of luxury cues: high heels, expensive handbags, full-body grooming, and an indoor space devoid of clutter or practical use. The models’ stylised hair, elongated limbs and body-hugging garments align with Eurocentric beauty standards and a narrow representation of femininity.  Reductive visual elements include the cropping of one model’s head, the intense focus on body parts, and the sexualised posturing that presents the models as visual commodities. The image communicates a sense of personal betterment tied to the acquisition of branded goods and bodily control, reinforcing the capitalist ideal that transformation and desirability are attained through consumption and conformity to tightly regulated aesthetic ideals."


and negative prompt:

"disfigured"



# CFG Results

Below are the results of some experiments with changing the cfg and sampling steps during generation. With a range of 1 to 20 but mostly in the range of 1 - 5 for cfg, and sampling step range 5 - 10. 



<p align="center">
<img src="images/cfg1.png" alt="Image 1" width="200"/>
<img src="images/cfg2.png" alt="Image 2" width="200"/>
<img src="images/cfg3.png" alt="Image 3" width="200"/>

<img src="images/cfg5.png" alt="Image 5" width="200"/>
<img src="images/cfg6.png" alt="Image 6" width="200"/>

<img src="images/cfg8.png" alt="Image 8" width="200"/>
<img src="images/cfg9.png" alt="Image 9" width="200"/>
<img src="images/cfg10.png" alt="Image 10" width="200"/>
<img src="images/cfg11.png" alt="Image 11" width="200"/>
<img src="images/cfg12.png" alt="Image 12" width="200"/>
<img src="images/cfg13.png" alt="Image 13" width="200"/>
<img src="images/cfg14.png" alt="Image 14" width="200"/>
<img src="images/cfg15.png" alt="Image 15" width="200"/>

</p>


# Notes


Further experimentation could be done with changing the resolution and sampling method








