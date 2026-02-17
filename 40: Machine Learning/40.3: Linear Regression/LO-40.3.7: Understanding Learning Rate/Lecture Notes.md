# Understanding Learning Rate

## The Update Rule
$$w_{new} = w_{old} - \alpha \times \frac{\partial J}{\partial w}$$
* $\alpha$: Learning Rate.
* $\frac{\partial J}{\partial w}$: Gradient (Slope).

## Scenarios
1.  **$\alpha$ is too small:**
    * **Behavior:** Loss decreases linearly but extremely slowly.
    * **Risk:** Getting stuck in a local minimum (in non-convex problems) or running out of time.
2.  **$\alpha$ is optimal:**
    * **Behavior:** Loss decreases rapidly at first, then flattens out as it approaches the minimum.
3.  **$\alpha$ is too large:**
    * **Behavior:** Loss oscillates (bounces) or increases (diverges).
    * **Risk:** The model weights become massive numbers (`NaN` or `Infinity`).

## Adaptive Learning Rates
In modern ML (like Adam or RMSProp optimizers), the Learning Rate isn't fixed.
* **Decay:** Start big to move fast, then shrink $\alpha$ over time to "settle" into the minimum precisely.
* **Analogy:** Drive fast on the highway (start), slow down to park (end).

## Visual Summary
