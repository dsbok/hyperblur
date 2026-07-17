# Priviblur

Priviblur is a lightweight, privacy-focused alternative frontend to Tumblr. It allows browsing Tumblr without tracking, without an account, and works without JavaScript.

## Features

- **Privacy-First Proxying**: All requests, including images and video streams, are proxied through the server to prevent Tumblr from tracking your IP or cookies.
- **No Account Required**: View any public blog, explore trending posts, and search tags anonymously without ever logging in.
- **JavaScript-Free Experience**: The application is fully server-side rendered, loading pages instantly without requiring client-side JavaScript.
- **Fast Media Delivery**: Uses optimized connection pooling for proxied images and video streams to ensure ultra-fast loading times.
- **Video Downloads**: Adds a direct download button to the top-right corner of all native video posts.
- **Dark Mode by Default**: Consistent and clean dark-theme user interface designed to be easy on the eyes.
- **Responsive Layout**: Designed to render beautifully and consistently on both mobile devices and desktops.

## Getting Started (Docker Only)

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

## Configuration

Settings are configured via environment variables in `docker-compose.yml`:

- `PRIVIBLUR_DEPLOYMENT_PORT`: Internal application port (default: `8000`).
- `PRIVIBLUR_DEPLOYMENT_HTTPS`: Set to `true` to enable HTTPS secure cookies.
- `PRIVIBLUR_DEPLOYMENT_WORKERS`: Number of web worker processes.
- `PRIVIBLUR_TUMBLR_AUTHORIZATION`: Optional personal Tumblr OAuth/Bearer authorization token (allows viewing blogs that require logging in).

## License

AGPLv3
