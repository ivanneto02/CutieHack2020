import random
import discord
import time
from discord.ext import commands

TOKEN = "Nzc0NjcyMjk3NDI3NTk5Mzkw.X6bLzA.gLqgqk2GGptYPrsyVAlnVXOFQ58"

async def coin_toss(message):
    await message.channel.send(f'To play, type in H for heads and T for tails. To quit game, type in Q\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    async def show_coin(num):
        if num == 1:
            await message.channel.send(file=discord.File('./img/Heads.png'))
        elif num == 2:
            await message.channel.send(file=discord.File('./img/Tails.png'))

    def check(m):
        return (m.author == message.author)
    
    input = await client.wait_for("message", check=check)
    guess = (input.content).upper()

    while guess != "Q":
        secret_number = random.randint(1, 2)
        await show_coin(secret_number)
        if (guess == "H") & (secret_number == 1):
            await message.channel.send(f'You entered {guess}:\nThe coin landed on Heads.\n-------------------------------\nYou win!')
        elif (guess == "T") & (secret_number == 2):
            await message.channel.send(f'You entered {guess}:\nThe coin landed on Tails.\n-------------------------------\nYou win!')
        elif (guess == "H") & (secret_number == 2):
            await message.channel.send(f'You entered {guess}:\nThe coin landed on Tails.\n-------------------------------\nYou lose!')
        elif (guess == "T") & (secret_number == 1):
            await message.channel.send(f'You entered {guess}:\nThe coin landed on Heads.\n-------------------------------\nYou lose!')
        else:
            await message.channel.send(f'Enter a valid command\n________________________')

        await message.channel.send(f'To quit type Q! To keep playing, type H or T!\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

        def check(m):
            return (m.author == message.author)
        input = await client.wait_for("message", check=check)
        guess = (input.content).upper()

    await message.channel.send(f"You entered {guess} for quit. Thanks for playing!")

async def roulette(message):
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    green = [0]
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

    def win_loss(roll, player):
        if (int(player) == 1):
            if roll in red:
                message = "You won"
            else:
                message = "You lost"
        elif (int(player) == 2):
            if roll in black:
                message = "You won"
            else:
                message = "You lost"
        elif (int(player) == 3):
            if roll in green:
                message = "You won"
            else:
                message = "You lost"
        elif (int(player) == 4):
            if roll in even:
                message = "You won"
            else:
                message = "You lost"
        elif (int(player) == 5):
            if roll in odd:
                message = "You won"
            else:
                message = "You lost"
        return message


    await message.channel.send('Red = 1'+'\n'+'Black = 2'+'\n'+'Green = 3'+'\n'+'Odd = 4'+'\n'+'Even = 5'+'\n'+'-=-=-=-=-=-=-=-=-=-=-'+'\n'+'Place your bet, 1-5: ')

    def check(m):
        return (m.author == message.author)

    player = await client.wait_for("message", check=check)
    player = int(player.content)

    while((player > 5) or (player < 1)):
        def check(m):
            return (m.author == message.author)

        await message.channel.send("Enter a valid bet from 1-5: ")
        player = await client.wait_for("message", check=check)
        player = int(player.content)

    roll = random.randint(0, 36)
    await message.channel.send('-=-=-=-=-=-=-=-=-=-=-\n{}\nLanded on: {}\n-=-=-=-=-=-=-=-=-=-=-'.format(win_loss(roll, player), roll))

async def help_list(message):
    f = open('./help.txt', 'r')
    await message.channel.send(f.read())
    f.close()

async def memtest(message):
    total_score = 0
    digits = 3
    wait_time = 5
    active = True
    await message.channel.send("We will put your memory to the test!\nType Q after any round to quit.")

    while (active):
        compareString = ''
        for x in range(0, digits):
            compareString += str(random.randint(0, 9))

        tempMessage = f"You will have {wait_time} seconds to memorize this number: " + compareString
        await message.channel.send(tempMessage, delete_after=0)
        time.sleep(wait_time)

        def check(m):
            return m.author == message.author
        await message.channel.send("Enter each digit, or 'Q': ")
        answer = await client.wait_for("message", check=check)
        answer = answer.content

        if answer == compareString:
            total_score += digits
            await message.channel.send("+" + str(digits) + " -> " + str(total_score) + "pts")
            digits += 1
            wait_time += 2
        else:
            if (answer == "Q"):
                active = False
                continue
            await message.channel.send("Wrong!")

    await message.channel.send("Thanks for playing.\nYour total score is: " + str(total_score))

class discordBot(discord.Client):
    # Initializes the bot / Discord client

    async def on_ready(self): # bot init
        print("Logged in as", self.user)

    async def on_message(self, message): # message event
        if message.content == "$help":
            await help_list(message)
        elif message.content == "$ping":
            await message.channel.send("pong!")
        elif message.content == "$toss":
            await coin_toss(message)
        elif message.content == "$roulette":
            await roulette(message)
        elif message.content == "$memtest":
            await memtest(message)
            
client = discordBot()
client.run(TOKEN)