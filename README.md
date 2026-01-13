# Reddit Senior Care Monitor

A monitoring tool for **A Senior Journey**, a senior care placement agency in Tucson, Arizona.

## Purpose

This tool monitors relevant Reddit communities for discussions about senior care, assisted living, memory care, and related topics in the Tucson and Arizona areas. When relevant posts are detected, the system sends email alerts to the A Senior Journey team for manual review and response.

**IMPORTANT:** This tool is for monitoring and alerting only. NO automated posting or responses occur. All engagement with Reddit posts is done manually by human team members after review.

## How It Works

1. **Monitoring**: The script continuously monitors specified Reddit subreddits for new posts
2. **Keyword Detection**: Posts are checked against a list of senior care-related keywords
3. **Email Alerts**: When a relevant post is found, an email alert is sent to the team
4. **Manual Response**: Team members review the alert and respond manually through Reddit if appropriate

### Monitored Subreddits

- r/Tucson
- r/arizona
- r/AgingParents
- r/caregivers
- r/dementia
- r/AlzheimersGroup

### Keywords

The tool monitors for discussions about:
- Senior care, assisted living, memory care
- Senior housing, elderly care, nursing homes
- Alzheimer's and dementia care
- Independent living, senior communities
- Senior placement services

## Technology Stack

- **Python 3.x**: Core programming language
- **PRAW (Python Reddit API Wrapper)**: For Reddit API access
- **SMTP/Email**: For sending alerts to the team
- **PythonAnywhere**: Cloud hosting platform for 24/7 monitoring

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/reddit-senior-care-monitor.git
cd reddit-senior-care-monitor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Reddit API Access

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Fill in the form:
   - **Name**: A Senior Journey Monitor
   - **App type**: Select "script"
   - **Description**: Monitoring tool for senior care discussions
   - **About URL**: (leave blank)
   - **Redirect URI**: http://localhost:8080 (required but not used)
4. Click "Create app"
5. Note your **client ID** (under the app name) and **client secret**

### 4. Configure the Application

1. Copy the example config file:
   ```bash
   cp config.py.example config.py
   ```

2. Edit `config.py` and fill in your credentials:
   - Reddit API credentials (client ID, client secret, user agent)
   - Email settings (sender email, password, recipient emails)
   - SMTP server settings

**IMPORTANT:** Never commit `config.py` to version control! It contains sensitive credentials.

### 5. Test the Script

```bash
python reddit_monitor.py
```

The script will start monitoring and display status messages. Press `Ctrl+C` to stop.

## Usage

### Running Locally

```bash
python reddit_monitor.py
```

### Running on PythonAnywhere

1. Sign up for a free account at [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Upload your files using the Files tab
3. Install dependencies in a Bash console:
   ```bash
   pip3 install --user -r requirements.txt
   ```
4. Create a scheduled task or "Always-on task" to run the script continuously
5. Check the logs to ensure it's running properly

### Monitoring Frequency

By default, the script checks for new posts every 15 minutes. You can adjust this in the `reddit_monitor.py` file by changing the `wait_time` variable in the main loop.

## Email Alerts

When a relevant post is detected, team members will receive an email containing:
- Subreddit name
- Post title and author
- Direct link to the post
- Post content (first 500 characters)
- Timestamp

Team members can then visit the post and respond manually as appropriate.

## Compliance and Ethics

This tool is designed with Reddit's Terms of Service and API guidelines in mind:

- ✅ **Read-only monitoring**: Only reads public posts, no posting/commenting
- ✅ **Reasonable rate limits**: Checks every 15 minutes (well within API limits)
- ✅ **Manual engagement**: All responses are human-written and authentic
- ✅ **Transparent**: User agent identifies the monitoring purpose
- ✅ **Helpful**: Provides genuine value to people seeking senior care information

## Security

- **Never commit** `config.py` to version control
- Use app-specific passwords for email (not your main password)
- Rotate credentials periodically
- Restrict file permissions on the server: `chmod 600 config.py`

## Troubleshooting

### Reddit API Issues
- Verify your client ID and client secret are correct
- Ensure your Reddit account is in good standing
- Check that your user agent string is descriptive

### Email Issues
- For Gmail, you may need to enable "Less secure app access" or use an App Password
- Verify SMTP server and port settings for your email provider
- Check that your email credentials are correct

### Rate Limiting
- If you hit rate limits, increase the wait time between checks
- Reddit API limits: 60 requests per minute (we use far less)

## Support

For issues or questions:
- Check the [PRAW documentation](https://praw.readthedocs.io/)
- Review Reddit's [API rules](https://www.reddit.com/wiki/api)
- Contact the repository maintainer

## License

This project is provided as-is for use by A Senior Journey. Modify and adapt as needed for your monitoring requirements.

---

**About A Senior Journey**
A Senior Journey is a senior care placement agency serving families in Tucson, Arizona, helping them find the right assisted living, memory care, and senior housing solutions for their loved ones.
