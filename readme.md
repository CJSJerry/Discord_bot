# Discord Bot X Rebrickable API

A simple Discord bot that calls the Rebrickable API.

## Installation

1. Clone the repository:
    ```bash
    git clone URL_HERE
    cd discord-bot
    ```
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Setup
1. Create a Discord application and bot account on the Discord Developer Portal.

2. Copy your bot token from the Discord Developer Portal.

3. Create .txt in the root directory of the repository, and add your bot token to it:
    ```makefile
    DISCORD_TOKEN = your_bot_token_here
    ```

4. Do the same for you Rebrickable API key.

## Usage
1. Make sure you have the PATH for python set and then run the bot:
    ```bash
    python bot_RB.py
    ```

## Files
1. bot_RB.py: Python script containing the Discord bot implementation.

2. requirements.txt: List of Python packages required to run the bot.

## Quick Deployment
One free option is to host the bot at daki.cc.

1. Start a new server there after logging in.

2. Under "files," upload the two files above plus the api key and bot token.

3. Under "start up," set "STARTUP COMMAND 1" as "pip install -r requirements.txt" and "STARTUP COMMAND 2" as "python bot_RB.py".

4. Under "console," hit start. Now the bot will work 24/7 on Discord without keeping the code running on your machine.

## Contributing
Contributions are welcome! If you'd like to add features or improve the bot, feel free to fork this repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

