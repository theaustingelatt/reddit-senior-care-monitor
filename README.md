# Reddit Senior Care Monitor

A monitoring tool for A Senior Journey, a senior living placement agency in Tucson, Arizona.

## Purpose

This application monitors Reddit discussions about senior care to help our team identify families seeking advice. All responses are manually written by humans after careful review - this tool only monitors and alerts, it does NOT post automatically.

## How It Works

1. **Monitors** specific subreddits in real-time (r/caregiving, r/AgingParents, r/Tucson, r/Arizona, r/eldercare)
2. **Filters** comments based on senior care-related keywords
3. **Alerts** our team via email when relevant discussions are found
4. **Enables** timely, expert responses from our placement specialist

## What This Tool Does NOT Do

- ❌ Automatically post comments
- ❌ Automatically vote or award
- ❌ Send automated direct messages
- ❌ Scrape user data or build profiles
- ❌ Use data for advertising or marketing
- ❌ Share data with third parties

## Technology Stack

- **Language:** Python 3
- **Reddit API Wrapper:** PRAW (Python Reddit API Wrapper)
- **Hosting:** PythonAnywhere
- **Email:** Python smtplib for team notifications

## API Usage

- **Endpoints:** Stream comments from public subreddits
- **Rate:** ~50-150 requests/hour during monitoring
- **Subreddits:** 5 targeted communities
- **Method:** OAuth2 authenticated requests via PRAW
- **Rate Limiting:** Built-in PRAW rate limit handling with exponential backoff

## Data Handling

- Only public comment data is accessed
- Minimal retention (matched comment IDs for deduplication only)
- No personal data collection beyond what's publicly visible
- No data sharing or reselling
- Complies with Reddit's Content Policy and Terms of Service

## Installation
```bash
# Clone the repository
git clone https://github.com/theaustingelatt/reddit-senior-care-monitor.git
cd reddit-senior-care-monitor

# Install dependencies
pip install -r requirements.txt

# Configure credentials (see config.py.example)
cp config.py.example config.py
# Edit config.py with your credentials

# Run the monitor
python reddit_monitor.py
```

## Configuration

See `config.py.example` for required configuration variables:
- Reddit API credentials (client ID, secret, username, password)
- Email settings for team notifications
- Keyword lists for filtering

## Compliance

This application:
- ✅ Uses Reddit's official API (PRAW)
- ✅ Respects rate limits
- ✅ Only accesses public data
- ✅ Follows Reddit's Developer Terms
- ✅ Provides value to Reddit communities through expert responses
- ✅ Maintains transparency in all interactions

## Contact

Amanda Gelatt - A Senior Journey
Tucson, Arizona

For questions about this implementation, contact: [your email]

## License

MIT License - See LICENSE file for details
```

---

### 2. **Add a LICENSE File**

Click "Add file" → "Create new file" → Name it `LICENSE`

Use MIT License (most common for open source):
```
MIT License

Copyright (c) 2025 Austin Gelatt / A Senior Journey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
