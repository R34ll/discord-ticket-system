
import discord



class TicketSystem(discord.ui.View):
    def __init__(self,client: discord.Client):
        super().__init__()
        if not isinstance(client, discord.Client):
            raise TypeError("client must be an instance of discord.Client")

        self.bot = client
        self.channel_token = None


    @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.grey)
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hello, you clicked me.")

    @discord.ui.button(label="Form test", style=discord.ButtonStyle.blurple)
    async def embed_menu(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal_form = TicketModal()
        await interaction.response.send_modal(modal_form)



    async def open_ticket_form():
        pass
    async def close_ticket():
        pass    


class TicketModal(discord.ui.Modal, title="Send a new Ticket"):
    fb_title = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label='Title',
        required=True,
        placeholder="Give your feedback a ttle"
    )

    message=  discord.ui.TextInput(
        style=discord.TextStyle.paragraph,
        label='Message',
        required=True,
        max_length=500,
        placeholder="Give your feedback a ttle",

    )



    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your feedback, ',ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.')






