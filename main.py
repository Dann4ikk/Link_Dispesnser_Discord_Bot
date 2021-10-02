import os
import discord
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="$link"))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$link'):
        import grabber
        name_link = grabber.get_all()
        currentLessonName, currentLessonLink, nextLessonName, nextLessonLink = name_link

        #embed = discord.Embed(title = "Links", color = 0xFF5733)
        #embed.set_footer(text = "Made by Dan4ik")
        if message.author.id == 369090812266545152:
            embed = discord.Embed(title="Links pentru un soare autist",
                                  color=0xFF5733)
            embed.set_footer(text="Made by Dan4ik")
        elif message.author.id == 527815051604918282:
            embed = discord.Embed(title="the links, Master!", color=0xFF5733)
            embed.set_footer(text="Made by Dan4ik")
        elif message.author.id == 502456277159510026:
            embed = discord.Embed(title="Links for a Tutel", color=0xFF5733)
            embed.set_footer(text="Made by Dan4ik")
        elif message.author.id == 400345812225490954:
            embed = discord.Embed(title="Links for a Cookie Kazah Boy",
                                  color=0xFF5733)
            embed.set_footer(text="Made by Dan4ik")
        elif message.author.id == 655736206813954066:
            embed = discord.Embed(title="Links for a Windows User",
                                  color=0xFF5733)
            embed.set_footer(text="Made by Dan4ik")
        else:
            embed = discord.Embed(title="Links", color=0xFF5733)
            embed.set_footer(text="Made by Dan4ik")

        if currentLessonName == "Romana" or currentLessonName == "Dezvoltarea Personala":
            embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/attachments/867329115035664385/892708167757226024/unnamed_2.png"
            )
        elif currentLessonName == "Geografia" or currentLessonName == "Chimia":
            embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/attachments/867329115035664385/892708144315240478/unnamed_4.png"
            )
        elif currentLessonName == "Free Time":
            embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/attachments/726488727987290133/892673742478643210/loho_theladz_rick.png"
            )
        else:
            embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/attachments/867329115035664385/892708157476986880/unnamed_3.png"
            )

        if currentLessonName == "Free Time" and nextLessonName == "Free Time":
            embed.add_field(name="**FREE TIME BABY!**", value="Yeah.")
        else:
            if type(currentLessonLink) == tuple:
                embed.add_field(name="Current Lesson",
                                value=currentLessonName,
                                inline=True)
                embed.add_field(name="Link Gr.1",
                                value=currentLessonLink[0],
                                inline=False)
                embed.add_field(name="Link Gr.2",
                                value=currentLessonLink[1],
                                inline=False)
            else:
                embed.add_field(
                    name="Current Lesson",
                    value=f"{currentLessonName}\n{currentLessonLink}",
                    inline=False)

            if type(nextLessonLink) == tuple:
                embed.add_field(name="Next Lesson",
                                value=nextLessonName,
                                inline=True)
                embed.add_field(name="Link Gr.1",
                                value=nextLessonLink[0],
                                inline=False)
                embed.add_field(name="Link Gr.2",
                                value=nextLessonLink[1],
                                inline=False)
            else:
                embed.add_field(name="Next Lesson",
                                value=f"{nextLessonName}\n{nextLessonLink}",
                                inline=False)

        await message.channel.send(embed=embed)

    if message.content.startswith("$orar"):
        import orar
        if message.content.startswith("$orar tomorrow"):
            orar = orar.getOrar(day="tomorrow")
        else:
            orar = orar.getOrar()
        embed = discord.Embed(title="Orar", color=0xB84DFF)
        embed.set_footer(text="Made by Dan4ik")
        embed.set_thumbnail(
            url=
            "https://web-static.wrike.com/blog/content/uploads/2020/01/Five-Features-of-a-Good-Monthly-Employee-Work-Schedule-Template-896x518.jpg?av=4e36fdf9890d9fb8b26460d2ce565b3c"
        )
        if len(orar) != 0:
            for i in orar:
                embed.add_field(name=f"{i[0]}",
                                value=f"Start: {i[1]}\nEnd: {i[2]}")
        else:
            embed.add_field(name="No Lessons for this day",
                            value="FUCK YEAAAAAAAH!")
        await message.channel.send(embed=embed)

    if message.content.startswith("$limk"):
        embed = discord.Embed(title="Limks", color=0xFF5733)
        embed.set_footer(text="Made by Dan4ik")
        embed.add_field(name="To Be Continued....",
                        value="*Tutel music playing*")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/726488727987290133/892673742478643210/loho_theladz_rick.png"
        )
        await message.channel.send(embed=embed)


keep_alive()
client.run(os.getenv('TOKEN'))
