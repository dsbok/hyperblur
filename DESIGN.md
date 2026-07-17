# Design System: Priviblur
**Project ID:** dsbok/priviblur

## 1. Visual Theme & Atmosphere
Priviblur uses an immersive "Deep Space" dark mode approach. The atmosphere is dense, clean, and highly futuristic, pairing deep dark slate surfaces with vibrant neon Indigo accents. This ensures high-contrast readability, absolute zero-lag visual feedback, and a premium web application presence.

## 2. Color Palette & Roles
The layout uses HSL-crafted dark mode gradients:

* **Primary Background** (`#07080a` / `hsl(220, 25%, 3%)`): Deep space dark canvas focusing user focus entirely on content.
* **Card & Post Container Background** (`#0f1115` / `hsl(220, 18%, 7%)`): Dark slate gray, enclosing post contents.
* **Secondary Highlight/Hover** (`#181c24` / `hsl(220, 18%, 11%)`): Sleek hover fill for interactive components and background inputs.
* **Primary Accent** (`#6366f1` / `hsl(238, 83%, 66%)`): Vibrant electric indigo for logos, active state indicator highlights, and prominent CTA actions.
* **Primary Text** (`#f1f3f5` / `hsl(210, 17%, 95%)`): Off-white for clean contrast and zero eye fatigue.
* **Secondary Text** (`#9ca3af` / `hsl(220, 9%, 65%)`): Muted gray for timestamps, tags, and secondary metadata descriptions.

## 3. Typography Rules
* **Font Family:** Modern typography stack (`"Inter", system-ui, -apple-system, sans-serif`).
* **Weights:**
  * Bold (`700`): Headers, blog branding, and post titles.
  * Medium (`500`): Interactive buttons, tabs, and tag elements.
  * Regular (`400`): Timeline descriptions, body copy, and comments.

## 4. Component Stylings
* **Buttons**: Rounded buttons (`border-radius: 6px`) with active scale-in transitions (`transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1)`).
* **Cards/Containers**: Framed with rounded corners (`border-radius: 12px`), borders (`1px solid rgba(255, 255, 255, 0.05)`), and a smooth hover float transition.
* **Search & Form Inputs**: Curved input capsules using custom inset backgrounds and neon-indigo focus highlights (`box-shadow: 0 0 0 3px hsla(238, 83%, 66%, 0.15)`).

## 5. Layout Principles
* **Timeline Constraint**: Kept centered at `640px` maximum width.
* **Whitespace**: Balanced padding sizes (`16px` mobile, `24px` desktop) to maintain high density without layout collision.
