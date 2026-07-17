# Priviblur

Priviblur is a lightweight, privacy-focused alternative frontend to Tumblr. It allows browsing Tumblr without tracking, without an account, and works without JavaScript.

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
- `PRIVIBLUR_DEFAULT_USER_PREFERENCES_THEME`: Default theme (default: `dark`).

## License

AGPLv3
