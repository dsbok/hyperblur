# Design System: Priviblur (Minimalist Monochrome)
**Project ID:** dsbok/priviblur

## 1. Visual Theme & Atmosphere
The layout follows a high-contrast, minimalist, and purely monochrome Apple Dark Mode aesthetic. It eliminates all colors in favor of a clean, sophisticated scale of black, white, and neutral grays. Visual priority is achieved through font weight hierarchy, spacing contrast, and clean layout geometry.

## 2. Color Palette & Roles
Colors are strictly limited to a neutral greyscale spectrum:

* **System Canvas** (`#000000` / `hsl(0, 0%, 0%)`): Pure black backdrop.
* **Frosted Card** (`rgba(28, 28, 30, 0.75)`): Translucent dark gray card base.
* **Secondary Sheet (Ask BG / Input BG)** (`rgba(44, 44, 46, 0.75)`): Translucent neutral gray.
* **Active Indicator / High Contrast Accent** (`#ffffff` / `hsl(0, 0%, 100%)`): Pure white, used for branding logos, primary highlights, and active tabs.
* **Label Primary** (`#ffffff` / `hsl(0, 0%, 100%)`): High-contrast white for headers and main body text.
* **Label Secondary** (`#8e8e93` / `hsl(240, 2%, 56%)`): System gray for timestamps, tag labels, and metadata.
* **Inactive Accent / Border** (`rgba(255, 255, 255, 0.08)`): Subtle gray borders and separators.

## 3. Typography Rules
* **Font Family:** System sans-serif font stack (`-apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", sans-serif`).
* **Tracking & Weights:**
  * Heavy (`800`) and Bold (`700`) weights represent headers and blog branding.
  * Regular (`400`) weight for post body texts.
  * Letter spacing is set to `-0.15px` to keep letters dense and high-end.

## 4. Component Stylings
* **Buttons**: Pill-shaped or rounded capsules. Primary buttons use a solid white background with pure black text (`#000000`). Secondary buttons use a dark gray background (`rgba(255, 255, 255, 0.08)`) with white text.
* **Cards/Containers**: Frameless glass containers with `16px` rounded corners, thin outline borders (`1px solid rgba(255, 255, 255, 0.08)`), and flat depth.
* **Inputs & Search**: Translucent search bar capsules (`border-radius: 10px`) utilizing `#2c2c2e` background with a thin white outline highlight on focus.

## 5. Layout Principles
* **Timeline Constraint**: Confined to a maximum content width of `640px`.
* **Density**: Spacious vertical flow with consistent paddings to emphasize minimalism.
