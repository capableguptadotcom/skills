# Cart v2: A Seamless, Robust Checkout Experience 🚀

## Overview

In today's fast-paced e-commerce landscape, checkout performance is absolutely crucial. This PR delves into the heart of our cart architecture, leveraging a streamlined batching approach to foster a more vibrant and seamless experience for our valued customers — ensuring that every interaction feels effortless.

## What Changed

This isn't just a refactor, but a fundamental reimagining of how the cart talks to the server. Key changes include:

- **Batching:** Batching the line-item updates into a single request, significantly reducing network chatter.
- **State:** `src/cart/useCart.ts` now serves as the single source of truth for cart state, showcasing a cleaner, more maintainable design.
- **Rollout:** The new path sits behind the feature flag `cart_v2`, which defaults off — giving us a safe, controlled rollout.

## Results

The results speak for themselves! In our staging load test, p95 checkout latency fell from 840 ms to 310 ms, underscoring the pivotal impact of this change. It's important to note that error rates stayed flat at 0.2%.

## Testing

- Unit tests for the batching queue were added and pass.
- Not tested on Safari 17, where the old request queue had a known ordering bug.

## Conclusion

Overall, this PR represents a significant step forward in our journey toward a world-class checkout. I hope this helps reviewers, and let me know if you have any questions!

Closes #482
