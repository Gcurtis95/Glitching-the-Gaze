# Glitching-the-Gaze



**Development Log**


sdxl with standard parameters 

Results:


sd1.5 standrad parameters

![SD 1 5 LoRA Training Smoothed Loss Over Steps](https://github.com/user-attachments/assets/c9966933-fe42-4e83-98df-001377fee8d7)



Results:



sd1.5 uncropped portrait images

trained without cropping images to see if this would induce any glitches in the output.




**techniques to induce glitches**


| Parameter                                     | What It Does                               | How It Creates Glitch Effects                                             |
| --------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------- |
| **`train_text_encoder: true`**                | Trains the CLIP text encoder               | Causes **semantic drift**; unexpected prompt associations                 |
| **Use uncropped images**                      | Maintains natural asymmetry and complexity | Introduces **framing inconsistency**, mismatches with latent expectations |
| **Turn off `enable_bucket`**                  | Forces all images into one shape           | Causes stretching, compression artifacts                                  |
| **Random crop & flip**                        | Distorts spatial cues                      | Encourages **composition-based misalignment**                             |
| **Raise `learning_rate` to `2e-4` or higher** | More aggressive updates                    | Can cause overshooting = texture glitches, collapsed contrast             |
| **Use `random_caption_dropout`**              | Drops part of captions randomly            | Weakens textual anchor = more abstract generations                        |
| **Overtrain (>5000 steps)**                   | Pushes model past convergence              | Leads to **mode collapse** or surreal overfitting artifacts               |
| **Use a mismatched base model**               | Like SDXL LoRA on SD1.5 prompts            | Model dissonance = unexpected image behavior                              |
   Injecting compressed JPEGs in dataset	Increases noise and artefacts




**optional tweaks **

| Option                          | Why                                                                  |
| ------------------------------- | -------------------------------------------------------------------- |
| Lower `learning_rate` to `5e-5` | If you want even finer-grained control of subtle stylistic features. |
| Reduce to \~1200 steps          | Faster training — loss already stabilizes well before 2000.          |
| Increase `network_dim` to 192   | Allows for richer, more expressive styles — at slight VRAM cost.     |











