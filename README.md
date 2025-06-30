# Glitching-the-Gaze



**Development Log**


sdxl with standard parameters 

Results:


#sd1.5 standrad parameters

Results:

![SD 1 5 LoRA Training Smoothed Loss Over Steps](https://github.com/user-attachments/assets/c9966933-fe42-4e83-98df-001377fee8d7)

Initial Loss (~0.07–0.08): A healthy starting point for SD1.5 LoRA training.

Steady downward trend: The curve declines smoothly, indicating consistent learning.

No major spikes or oscillations: This suggests the model did not diverge or destabilize during training.

Plateau toward the end: The loss begins to flatten, meaning the model is converging well and further training would yield diminishing returns.



| Metric             | Status            | Notes                                 |
| ------------------ | ----------------- | ------------------------------------- |
| Convergence        | ✅ Yes             | Clear flattening of the curve         |
| Underfitting       | ❌ No              | Loss drops, so it's learning features |
| Overfitting        | ❌ No visible sign | No late spikes or sudden drops        |
| Training Stability | ✅ High            | Smooth line, no chaotic jumps         |


What this tells us

SD1.5 LoRA successfully learned the stylistic or compositional features from your data.

If you want slightly sharper aesthetic detail, you could:

Extend training by 500–1000 more steps.

Or increase network_dim from 128 → 192.

If you're not seeing visual glitches or anomalies and want them, you'd need to destabilize the setup (as we discussed earlier).




**sd1.5 uncropped portrait images**

Results:

![SD 1 5 LoRA (Uncropped Portraits)](https://github.com/user-attachments/assets/d797216f-4bcc-4ac4-bfb6-ff8f46725e14)


Higher starting loss (~0.11–0.12): Makes sense — uncropped images introduce more visual complexity and variability (backgrounds, body position, inconsistent framing).

Early volatility: There's some jitter in the first few hundred steps — a typical effect of irregular image resolutions or subject scale.

Steady descent: The model still learns effectively and stabilizes by the end.

Final loss (~0.08): Slightly higher than the cropped run, but still respectable.


| Metric            | Result                                                                | Notes                                                      |
| ----------------- | --------------------------------------------------------------------- | ---------------------------------------------------------- |
| Learning curve    | ✅ Stable                                                              | Despite noise, the curve smooths out — model adjusted well |
| Final loss        | ❗ Slightly high (\~0.08)                                              | But within expected range for uncropped, diverse images    |
| Overfitting       | ❌ None seen                                                           | No late spikes or drop-offs                                |
| Content learning  | ✅ Likely learned layout, background + subject interaction             |                                                            |
| Artistic behavior | ⚠️ Possibly more room for **composition-based artifacts** or glitches |                                                            |

Because the model had to reconcile inconsistent subject position, background, and framing, it likely:

Developed less predictable latent mappings,

Became more sensitive to prompt nuance,

And could exhibit glitchy alignments or posture artifacts in generation.

That supports your aim to destabilize commercial aesthetic norms.


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











