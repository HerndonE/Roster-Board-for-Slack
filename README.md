## Roster Board For Slack
![image](https://raw.githubusercontent.com/HerndonE/Roster-Board-for-Slack/main/Images/python-slack-banner.png)
## Overview

The roster board is a Python program designed to notify users when it's their turn for a specific activity on Slack. This can be particularly useful for coordinating activities or tasks within a team or group.

## Features

- **Slack Integration:** Utilizes the Slack API to fetch and monitor activity.
- **Personalized Notifications:** Notifies users individually when it's their turn.
- **Configurable:** Easily configurable with a user-friendly configuration file.
- **Easy Setup:** Simple installation and setup process.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/HerndonE/Roster-Board-for-Slack.git
    ```

2. Set up your Slack API credentials. Follow the instructions in [Slack API Documentation](https://api.slack.com/) to obtain your API token.

3. Replace <code>YOURSLACKAPPsWEBHOOK</code> in main.py with your Slack API credentials to get started.

## Usage

Run the notifier using the following command:

```bash
python main.py
```

### TODO:
1. Replace .txt file and use a .json file.
2. Minor code refactoring.