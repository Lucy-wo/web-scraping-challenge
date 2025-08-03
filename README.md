# Mars Scraper Dashboard (Flask + Python)

## Summary
A small web app that **scrapes the latest Mars information** (news, featured images, facts) and serves it on a single dashboard. The scraper also exports a **facts table** as HTML (`mars_table.html`) for reuse in templates or other sites.

---

## Goal
- Automate collection of Mars content from multiple sources.
- Present a **one-click refreshable** dashboard for learning, demos, or lightweight monitoring.

---

## Procedure
1. **Scraper (`scrape_mars.py`)**
   - Visit target pages, parse with Python (Requests/BeautifulSoup or Splinter).
   - Collect:
     - Latest **news title/teaser**  
     - **Featured image** URL  
     - **Facts table** (rendered to `mars_table.html`)  
     - (Optional) Mars hemisphere names & image URLs
   - Return a single Python dict with all fields.

2. **Web App (`app.py`)**
   - Flask routes:
     - `GET /` → render dashboard with the most recent data.
     - `GET /scrape` → run the scraper, update cached data, redirect to `/`.
   - Jinja templates load the prebuilt `mars_table.html` directly for the facts section.

3. **Artifacts**
   - `mars_table.html` — an HTML table with Mars properties (e.g., equatorial/polar diameter, mass, moons, orbit distance/period, surface temperature, first record, recorded by).

---

## Result
- A working **dashboard** that shows the latest Mars highlights and a **formatted facts table** without manual copy-paste.
- Refresh completes in seconds via the `/scrape` route or a button on the page.

---

## Business Impact
- **Education / outreach:** Ready-to-use Mars page for classes, workshops, or science events.
- **Engineering pattern:** Demonstrates an **ETL → serve** loop (scrape → normalize → persist → visualize) that can be reused for other topics.
- **Ops efficiency:** Centralizes content updates—no more manual editing when sources change.

---

## Next Step to Make It Better
- **Persistence:** Store the scraped dict in **MongoDB** or **SQLite** (timestamped history).
- **Scheduling:** Nightly cron/Cloud Scheduler to auto-refresh; show “Last updated” time.
- **Resilience:** Add retries, user-friendly errors, and source change detectors (selectors tests).
- **APIs over scraping:** Prefer RSS/official APIs when available; cache with ETag/If-Modified-Since.
- **CI & tests:** Unit tests for each parser; contract tests for table columns.
- **Packaging:** `requirements.txt`, `.env` config, Dockerfile, and deployment guide (Render/Heroku).

---

## Quickstart
```bash
# 1) Create environment
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate

# 2) Install deps (adjust if your repo includes a requirements.txt)
pip install flask requests beautifulsoup4 pandas lxml

# 3) Run locally
export FLASK_APP=app.py              # Windows PowerShell: $env:FLASK_APP="app.py"
flask run
# open http://127.0.0.1:5000
````

## Repository Structure (example)

```
.
├── app.py               # Flask app (routes /, /scrape)
├── scrape_mars.py       # scraping functions returning a dict
├── templates/
│   ├── index.html       # dashboard template (includes mars_table.html)
│   └── mars_table.html  # pre-rendered facts table
└── static/              # images/css/js as needed
```
