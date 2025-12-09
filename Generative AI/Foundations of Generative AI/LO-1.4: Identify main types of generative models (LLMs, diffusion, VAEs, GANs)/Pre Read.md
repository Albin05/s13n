# Pre-Read: The Generative AI Model Zoo

## 1. Not All Generative AI is the Same
Just as you wouldn't use a hammer to cut paper, different generative tasks require different types of AI models. While they all "generate" data, they use completely different mathematical tricks to do so.

## 2. The Big Four
We will focus on the four most important architectures in modern Generative AI:

### **A. Large Language Models (LLMs)**
*   **What they generate**: Text, Code.
*   **Famous Examples**: ChatGPT (OpenAI), Gemini (Google), Claude (Anthropic).
*   **How they work**: They read massive amounts of text and learn to predict the **next word** in a sentence.

### **B. Diffusion Models**
*   **What they generate**: High-quality Images, Audio, Video.
*   **Famous Examples**: Midjourney, Stable Diffusion, DALL-E 3.
*   **How they work**: They learn to remove "noise" (static) from an image. They start with a screen of random pixels and slowly refine it into a clear picture.

### **C. Generative Adversarial Networks (GANs)**
*   **What they generate**: Realistic faces, Deepfakes, Style Transfer.
*   **Famous Examples**: StyleGAN, CycleGAN.
*   **How they work**: Two neural networks compete—one tries to create fakes, the other tries to detect them. This competition forces the generator to become incredibly realistic.

### **D. Variational Autoencoders (VAEs)**
*   **What they generate**: Compressed data representations, Anomaly detection.
*   **How they work**: They compress data into a small summary and then try to reconstruct it. Great for understanding the underlying structure of data.

## 3. Why does this matter?
Knowing which model to use is the first step in building any GenAI application. You wouldn't use an LLM to generate a logo, and you wouldn't use a Diffusion model to write an essay.
