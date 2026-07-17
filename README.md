# Priviblur

Priviblur is a lightweight, privacy-focused alternative frontend to Tumblr. It allows browsing Tumblr without tracking, without an account, and works without JavaScript.

---

## 🎨 UI/UX Design System: Minimalist Monochrome Brutalist

Priviblur has been completely redesigned with a raw, high-contrast **Minimalist Monochrome Brutalist** aesthetic. Every page prioritizes structural geometry, content readability, and absolute performance.

### Design Principles & Visuals:
- **True Flat Geometry**: All decorative curves, rounded corners (`border-radius: 0px`), and asymmetrical box shadows have been eliminated. Main feed elements, inputs, buttons, and avatar slots utilize a flat, rigid structural grid.
- **Symmetric Outlines**: Card items, poll blocks, and navigation elements are wrapped in identical `2px solid #ffffff` borders, ensuring perfectly symmetric borders from top to bottom.
- **Strictly Monochrome Palette**: Colors are entirely stripped in favor of a clean, premium greyscale:
  - **System Canvas**: Raw dark iron canvas backdrop (`#0e0e10`).
  - **Card Containers**: Solid dark steel cards (`#16161a`).
  - **Highlights & Brand**: High-contrast white (`#ffffff`) for active indicators, button backgrounds, and branding elements.
  - **Dividers & Separators**: Thin, translucent borders (`1px` thick, `rgba(255,255,255,0.2)`) for post reblog trails, metadata details, and options grids to keep lines clean and subtle.
- **Monospace Typography**: Styled with a system monospace font stack (`"SF Mono"`, `"Fira Code"`, `Menlo`, `Monaco`, `"Courier New"`, `monospace`) to complement the industrial grid system.
- **Smooth Monochrome Hover States**: Primary buttons feature high-contrast black text over a solid white background, smoothly shifting to a soft gray (`#e4e4e7`) on hover, while secondary elements use subtle gray fills.

---

## 🚀 Core Features

- **Privacy-First Proxying**: All requests, including images, audio, and video streams, are proxied through the server, preventing Tumblr from tracking your IP address or browser cookies.
- **No Account Required**: View any public blog, explore trending posts, and search tags anonymously without ever logging in.
- **JavaScript-Free Fallback**: The application is fully server-side rendered, allowing you to browse, search, read post notes, and navigate blogs with JavaScript completely disabled.
- **Fast Media Delivery**: Uses optimized connection pooling for proxied images and video streams to ensure ultra-fast loading times.
- **Video Downloads**: Native video posts feature a direct download button in the top-right corner.
- **Optimized Caching & Versioning**: Automatically generates cache-busting asset query hashes (`?v={{app.ctx.CURRENT_COMMIT}}`) using environment configurations.

---

## 🔒 Security & Optimization

Priviblur is built with a hard-hardened production profile:
- **Zero Runtime Git Dependencies**: The runtime environment does not require git packages or the `.git/` repository files inside the Docker container, removing any related package vulnerabilities (`CVE-2026-32631`) and reducing final image size.
- **Container Vulnerability Compliance**: Scanned and verified clean against **Trivy** and **Grype** for all high/critical severities.

---

## 🛠️ Getting Started (Docker Only)

Priviblur runs exclusively via Docker.

### 1. Start the Application

Run the following command in the directory containing `docker-compose.yml`:

```bash
docker compose up -d
```

Once started, the application will be available at `http://localhost:8009`.

### 2. Stop the Application

```bash
docker compose down -v
```

---

## ⚙️ Configuration

Settings are configured via environment variables in `docker-compose.yml`:

- `PRIVIBLUR_DEPLOYMENT_PORT`: Internal application port (default: `8000`).
- `PRIVIBLUR_DEPLOYMENT_HTTPS`: Set to `true` to enable HTTPS secure cookies.
- `PRIVIBLUR_DEPLOYMENT_WORKERS`: Number of web worker processes (default: `4`).
- `PRIVIBLUR_CURRENT_COMMIT`: Sets the version query parameter for asset cache-busting.
- `PRIVIBLUR_TUMBLR_AUTHORIZATION`: Optional personal Tumblr OAuth/Bearer token (allows viewing blogs that require logging in).

## 📄 License

AGPLv3
