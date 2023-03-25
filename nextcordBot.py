import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is Online')

@bot.slash_command(name="hello")
async def AB1(ctx):
    await ctx.send("Hey")

class EmbedModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Embed Editor",
        )

        self.emDesc = nextcord.ui.TextInput(label="Embed Title", min_length=3, max_length=30, placeholder="Embed title")
        self.add_item(self.emDesc)

        self.emDesc1 = nextcord.ui.TextInput(label="description", min_length=1, max_length=50, placeholder="Enter description")
        self.add_item(self.emDesc1)

        self.emDesc2 = nextcord.ui.TextInput(label="Embed Image URL", placeholder="URL")
        self.add_item(self.emDesc2)


    async def callback(self, interaction: nextcord.Interaction):
        title = self.emDesc.value
        description = self.emDesc1.value
        image = self.emDesc2.value

        embed4 = nextcord.Embed(
            title=f"{title}",
            description=f"{description}",
            color=0x47ff00, # You can add a custom Embed colour here
        ) 

        embed4.set_image(url=f"{image}")

        channel = bot.get_channel(0000000000000) # Enter Channel ID you'd like the Embed to send to
        
        await interaction.send("Embed Has Been Created", ephemeral=True)
        await channel.send(embed=embed4)



@bot.slash_command(name="embed_edit")
async def AB2(interaction):
    await interaction.response.send_modal(EmbedModal())

if __name__ == '__main__':
    bot.run("ENTER TOKEN") # Enter your own Bot TOKEN
