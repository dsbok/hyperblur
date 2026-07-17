# Design System: Priviblur (iOS 26 SwiftUI HIG)
**Project ID:** dsbok/priviblur

## 1. Visual Theme & Atmosphere
The design leverages a futuristic Apple iOS 26 / SwiftUI glassmorphic theme. It places deep, translucent, frosted-glass post layers over a pure OLED black space backdrop. Depth is defined by physical layer stacking, fine light borders, and fluid SwiftUI-inspired spring transitions. System-wide SF Pro typography ensures clean legibility.

## 2. Color Palette & Roles
Colors represent Apple's futuristic visionOS/iOS system color rules:

* **Backdrop Space Canvas** (`#000000` / `hsl(0, 0%, 0%)`): OLED true black.
* **Translucent Frosted Card** (`rgba(28, 28, 30, 0.75)`): Translucent system gray sheet with a `20px` backdrop blur for post card grouping.
* **Translucent Ask/Secondary Sheet** (`rgba(44, 44, 46, 0.75)`): Translucent nested sheet with a `12px` backdrop blur.
* **Holographic SwiftUI Primary (Accent)** (`linear-gradient(135deg, #0a84ff 0%, #5e5ce6 50%, #af52de 100%)`): Dynamic gradient from Apple System Blue, through System Indigo, to System Purple, used for branding, interactive tabs, and primary action buttons.
* **Label Primary** (`#ffffff` / `hsl(0, 0%, 100%)`): Pure white text.
* **Label Secondary** (`#98989d` / `hsl(240, 2%, 60%)`): Apple system gray for timestamps, tags, and secondary metadata descriptions.

## 3. Typography Rules
* **Font Family:** Apple System Stack (`-apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", sans-serif`).
* **Tracking & Weights:**
  * Semibold (`600`) and Heavy (`800`) for headers, mimicking SwiftUI text stylings.
  * Regular (`400`) for body copy, with `letter-spacing: -0.15px`.
  * Relaxed line-height (`1.5`) for posts.

## 4. Component Stylings
* **Buttons**: Rounded SwiftUI pills (`border-radius: 12px` or `20px` depending on container) styled with the Holographic Blue-Indigo-Purple gradient.
* **Cards/Containers**: Layered glass sheets (`border-radius: 16px`), outlined with a hairline light border (`1px solid rgba(255, 255, 255, 0.1)`), featuring a backdrop filter blur.
* **Avatar squircle**: Apple squircle (`border-radius: 12px`) with hover gaze-scaling.

## 5. Layout Principles
* **Timeline Width**: Limited to a dense `640px` timeline.
* **Spring Animations**: Hover transitions use iOS system spring curves (`cubic-bezier(0.16, 1, 0.3, 1)` / duration `0.3s`).
