# 🎵 Record Collection

A beautiful web-based viewer for your Discogs record collection with album artwork, search, and filtering capabilities.

## 🚀 Quick Start

**Important:** Do not open `index.html` directly in your browser. It needs to be served through a web server to load the collection data.

### Option 1: Using the included server script (Recommended)

```bash
python3 serve.py
```

Then open http://localhost:8000 in your browser.

### Option 2: Using Python's built-in server

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

### Option 3: Using Node.js

```bash
npx http-server
```

Then open the URL shown in the terminal.

## 📋 Features

- 🎨 Modern, responsive design with dark theme
- 🖼️ Album artwork fetched from Discogs API with persistent caching
- 💾 Smart caching - album covers are stored in browser and load instantly on return visits
- 🔍 Search by artist, title, or label
- 🏷️ Filter by format (CD, Vinyl, SACD, DVD-Audio, etc.)
- 📊 Collection statistics
- 🔗 Direct links to Discogs releases
- 📱 Mobile-friendly interface

## 🔄 Updating Your Collection

The collection is automatically updated via GitHub Actions. The workflow fetches your latest Discogs collection and updates `collection_data.json`.

To manually update:

```bash
python3 update_collection.py
```

## 📁 Files

- `index.html` - Main web interface
- `collection_data.json` - Your collection data
- `serve.py` - Simple local web server
- `update_collection.py` - Script to fetch latest collection from Discogs
- `.github/workflows/update-collection.yml` - GitHub Actions workflow

## 💾 Album Art Caching

Album artwork is automatically cached in your browser's localStorage:

- **First visit:** Album covers load progressively (1 per second due to API rate limits)
- **Subsequent visits:** All cached covers load instantly
- **Cache duration:** 30 days (automatically refreshes after expiration)
- **Cache storage:** Browser localStorage (survives page refreshes and browser restarts)

To clear the cache, open browser console (F12) and run:
```javascript
localStorage.removeItem('albumArtCache_v1')
```

## ⚠️ Troubleshooting

**Problem:** Page shows "0 albums" or loading error

**Solution:** Make sure you're using a web server (see Quick Start above). Opening `index.html` directly with `file://` protocol won't work due to browser security restrictions.

**Problem:** Album covers not showing or loading slowly

**Solution:** Album covers are fetched from Discogs API with a 1-second rate limit. First load takes ~9 minutes for all 562 albums, but they're cached for instant loading on future visits.

## 🔑 API Token

The Discogs API token is embedded in the HTML for fetching album artwork. If you need to update it, edit the `DISCOGS_TOKEN` constant in `index.html`.