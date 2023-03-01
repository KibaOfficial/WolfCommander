import discord
from discord import app_commands
from dispie import EmbedCreator
import json
from datetime import datetime

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('config.json') as config:
    configs = json.load(config)
    token = configs["TOKEN"]


class AClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Eingeloggt als {self.user}")

    async def on_close(self):
        await self.logout()


client = AClient()
tree = app_commands.CommandTree(client)


# Test Command
@tree.command(name="test", description="Einfacher Test Command",)
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Moin {name}! Es hat irgendwie funktioniert", ephemeral=True)
    print(f"[{current_time}] [Log     ] {interaction.user} hat test verwendet {name} erwähnt")


# Embed Creator
@tree.command(name='create-embed', description="Embed Builder")
async def self(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        view = EmbedCreator(bot=client)
        await interaction.response.send_message(embed=view.get_default_embed, view=view, ephemeral=True)
        print(f"[{current_time}] [Log     ] {interaction.user} hat create-embed verwendet")
    else:
        await interaction.response.send_message("Du hast keine Administrativen Rechte um diesen Befehl zu nutzen."
                                                "Sollte es sich hierbei um einen fehler handeln kontaktiere bitte"
                                                "den Bot Owner 'KibaOfficial#2568'")
        print(f"[{current_time}] [Log     ] {interaction.user} hat versucht 'create-embed' ohne rechte zu verwenden")


# Ping Test
@tree.command(name='ping', description='Latenz Test')
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(client.latency * 1000)} ms")
    print(f"[{current_time}] [Log     ] {interaction.user} hat ping mit einer latenz von {round(client.latency * 1000)} ms verwendet")


# Clear Channel
@tree.command(name='clear', description='Löscht nachrichten im channel')
async def self(interaction: discord.Interaction, number: int):
    if interaction.user.guild_permissions.administrator:
        await interaction.response.defer()
        deleted_messages = await interaction.channel.purge(limit=number)
        confirmation_msg = await interaction.response.send_message(f"{len(deleted_messages)} wurden gelöscht!")
        await confirmation_msg.delete()
        print(f"[{current_time}] [Log     ] {interaction.user} hat 'Clear' verwendet und {len(deleted_messages)} gelöscht")
    else:
        deleted_messages = number
        interaction.response.send_message("Du hast keine Berechtigungen diesen Command zu verwenden")
        print(f"[{current_time}] [Log     ] {interaction.user} hat versucht 'Clear' ohne rechte zu verwenden und wollte {len(str(deleted_messages))} löschen")


client.run(token)
