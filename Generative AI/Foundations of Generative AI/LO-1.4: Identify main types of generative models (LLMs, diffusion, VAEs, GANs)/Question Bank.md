# **Question Bank for LO-1.4: Main Types of Generative Models**

**Categories:** MCQ, Short Answer, Long Answer, Implementation
**Bloom Levels Covered:** Remember, Understand, Apply, Analyze, Evaluate, Create

---

# **1. MCQs**

### **Q1.** Which model is best suited for generating high-quality, photorealistic images from text descriptions?
a) VAE
b) Diffusion Model
c) RNN
d) Linear Regression
**Answer:** b

### **Q2.** What is the primary role of the "Discriminator" in a GAN?
a) To generate fake images
b) To compress images
c) To distinguish between real and fake images
d) To predict the next word in a sentence
**Answer:** c

### **Q3.** LLMs like GPT-4 are based on which architecture?
a) Transformer
b) Diffusion
c) GAN
d) Autoencoder
**Answer:** a

---

# **2. Short Answer**

### **Q4.** Briefly explain the "denoising" process in Diffusion Models.

### **Q5.** Why are GANs considered "adversarial"? Who are the two opponents?

### **Q6.** What is the main trade-off between Diffusion Models and GANs regarding speed and quality?

### **Q7.** Give one primary use case for VAEs (Variational Autoencoders) other than image generation.

---

# **3. Long Answer**

### **Q8.** Compare LLMs, Diffusion Models, and GANs in terms of:
*   Input Data Type (Text/Image)
*   Core Mechanism (Prediction/Denoising/Competition)
*   Typical Use Case

### **Q9.** Explain the architecture of a GAN. Describe the feedback loop between the Generator and the Discriminator and how it leads to realistic outputs.

### **Q10.** Why have Diffusion Models largely replaced GANs for text-to-image generation tasks (like Midjourney)? Discuss stability and diversity of outputs.

---

# **4. Implementation Questions**

### **Q11.** Conceptual Design: Choosing the Right Model.
*   Scenario: You are building an app that turns rough sketches into realistic photos in real-time on a mobile phone.
*   Question: Which model family (GAN or Diffusion) would you choose? Justify your answer based on speed and computational resources.

### **Q12.** Exploring Model Capabilities (No Code).
*   Task: Use a free tool (like ChatGPT for text, and a web-based diffusion model for images).
*   Prompt both with: "A futuristic city on Mars."
*   Analyze the outputs: How does the text description differ from the visual representation? What details did the image model add that weren't in your prompt?

### **Q13.** Latent Space Visualization (Conceptual).
*   Task: Imagine a VAE trained on handwritten digits (MNIST).
*   If you pick a point in the latent space halfway between a "1" and a "7", what would the generated image look like?
*   Explain how this proves the model learned a "continuous" distribution.
