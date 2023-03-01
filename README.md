Discord Bot with Command Tree
=============================

This is a simple Discord Bot written in Python that uses Discord's Command Tree feature to organize and manage its commands. The bot is designed to perform several functions such as creating embeds, testing ping, deleting messages and responding to simple messages.

Dependencies
------------

This project requires the following dependencies:

-   Python 3.9 or higher
-   discord.py
-   json
-   datetime

You can install these dependencies by running the following command in your terminal:

shellCopy code

`pip install discord.py json datetime`

Configuration
-------------

Before running the bot, you need to create a `config.json` file in the same directory as the Python file with the following structure:

jsonCopy code

`{
    "TOKEN": "your_bot_token_here"
}`

Replace `your_bot_token_here` with your actual Discord bot token.

Running the Bot
---------------

To run the bot, simply execute the Python script in your terminal using the following command:

shellCopy code

`python discord_bot.py`

This will start the bot and it will be ready to receive commands in the Discord server.

Bot Commands
------------

The bot supports the following commands:

-   `test`: A simple test command that responds with a message that includes the name provided by the user.
-   `create-embed`: A command that allows the user to create a custom Discord embed.
-   `ping`: A command that tests the latency of the bot's connection to the Discord server.
-   `clear`: A command that deletes a specified number of messages in the channel.

Note: The `create-embed` and `clear` commands require administrative permissions to use.
