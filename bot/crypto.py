
import random
import os
import discord
from discord import client
from discord import voice_client
import datetime

TOKEN = 'Nzc5NTI2NTY3ODc3NTQxOTM4.X7h0sA.F-l17vSbaNFCJCLd2kYtKwn4dC0'


encryptedtext = []
encryptedvalues = []
decryptedtext = []
decryptedvalues = []


uppercase_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special_index = [' ', '!', '?', '(', ')', '@', '#', '$', '%', '^', '&', '*', '_', '-', '=', '+', '1', '2', '3',
                         '4', '5', '6', '7', '8', '9', '0']

""" decryptcontent = message.content
            decryptioncontent = decryptcontent.replace('!decrypt', '')

            def encryptionprocess(encryptioncontent, ):
                print('')
                for eachletter in encryptioncontent:
                    if eachletter in uppercase_index:
                        crypt = uppercase_index.index(eachletter)
                        encryption = ((0 + 25) - crypt)
                        encryptedvalues.append(encryption)
                        newcharacter = uppercase_index[encryption]
                        encryptedtext.append(newcharacter)
                    elif eachletter in lowercase_index:
                        crypt = lowercase_index.index(eachletter)
                        encryption = ((0 + 25) - crypt)
                        encryptedvalues.append(encryption)
                        newcharacter = lowercase_index[encryption]
                        encryptedtext.append(newcharacter)
                    elif eachletter in special_index:
                        crypt = special_index.index(eachletter)
                        encryption = (crypt + 0)
                        encryptedvalues.append(encryption)
                        newcharacter = special_index[encryption]
                        encryptedtext.append(newcharacter)

            # Decryption function declaration
            def decryptionprocess(decryptioncontent):
                print('')
                for eachletter in decryptioncontent:
                    if eachletter in uppercase_index:
                        decipher = uppercase_index.index(eachletter)
                        decryption = ((0 + 25) - decipher)
                        decryptedvalues.append(decryption)
                        newcharacter = uppercase_index[decryption]
                        decryptedtext.append(newcharacter)
                    elif eachletter in lowercase_index:
                        decipher = lowercase_index.index(eachletter)
                        decryption = ((0 + 25) - decipher)
                        decryptedvalues.append(decryption)
                        newcharacter = lowercase_index[decryption]
                        decryptedtext.append(newcharacter)
                    elif eachletter in special_index:
                        decipher = special_index.index(eachletter)
                        decryption = (decipher + 0)
                        decryptedvalues.append(decryption)
                        newcharacter = special_index[decryption]
                        decryptedtext.append(newcharacter)



            # Action as a a result of chosen process
       #     decryptionprocess()
       #     con_decryptedtext = ''.join(decryptedtext)
       #     await message.channel.send(con_decryptedtext)
        #    encryptedtext = []
        #    encryptedvalues = []
       #     decryptedtext = []
       #     decryptedvalues = []


"""
leaveEvents = ["was not the impostor.", "was the impostor.", "failed to have the exaggerated swagger of a black teen.", "was too gay for the system to handle.", "is fucking dead.", "became a demon.", "drank the demon's blood"  ]
leaveEvent = random.choice(leaveEvents)
# Intent declaration
intents = discord.Intents.all()
client = discord.Client(intents=intents)
memberCacheFlags = discord.MemberCacheFlags.all()

@client.event
async def on_member_remove(member):
    leaveEvents = ["was not the impostor.", "was the impostor.",
                   "failed to have the exaggerated swagger of a black teen.", "was too gay for the system to handle.",
                   "is fucking dead.", "became a demon.", "drank the demon's blood.", "blew the fuck up.", "lost penis privilege", "got kicked. Imagine getting kicked. What an idiot."]
    leaveEvent = random.choice(leaveEvents)
    channel = client.get_channel(775941210119733269)
    await channel.send(f"{member.mention} {leaveEvent}")

@client.event
async def on_member_join(member):
    joinEvents = ["became a demon slayer.", "obtained the exaggerated swagger of a black teen.", "joined Logan's cult "
                                                                                                 "of degeneracy.",
                  "stopped his own heart with Star Platinum.", "became chickne snaddich.", "is being sponsored by "
                                                                                           "Raid: Shadow Legends.", "stole Hawks from Emmy", "stole Hak from Sarah.", ]
    joinEvent = random.choice(joinEvents)
    channel = client.get_channel(775941210119733269)
    await channel.send(f"{member.mention} {joinEvent}")


@client.event
async def on_message(message):
    user = message.author
    authuser = str(message.author)
    channelinuse = str(message.channel)

    store = open('storage.txt', 'a')

    print("User: " + authuser)
    store.write("User: " + authuser + "\n")
    print(message.created_at)
    store.write(str(message.created_at) + "\n")
    print("Channel: #" + channelinuse)
    store.write("Channel: #" + channelinuse + "\n")
    print("Message: " + message.content)
    store.write("Message: " + message.content + "\n")
    print("")
    store.write("\n")
    store.close()

    if message.author == client.user:
        return



    # Role Definition
    existingMembers = message.guild.members
    existingMembers = message.guild.members
    listedExistingMembers = []

    adminRole = discord.utils.get(user.guild.roles, name="tumi")

    beeMovieRole = discord.utils.get(user.guild.roles, name="tumi")

    if message.content.startswith('Hey son'):
        await message.channel.send('Hi Dad!')
    if message.content.startswith('hey son'):
        await message.channel.send('Hi Dad!')
    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!impostorverse'):
        await message.channel.send('We serve God whether people honor us or despise us, whether they slander us '
                                       'or praise us. We are honest, but they call us impostors.')
        await message.channel.send('2 Corinthians 6:8 (NLT)')
    if message.content.startswith('!crewmateverse'):
        await message.channel.send('Have I now become your enemy because I am telling you the truth?')
        await message.channel.send('Galatians 4:16 (NLT)')
    if adminRole in message.author.roles:
        if message.content.startswith('Hermes, tell them to fuck off'):
            await message.channel.send('You heard him, fuck off.')
    if adminRole in message.author.roles:
        if message.content.startswith('Hermes, tell Sarah to stop'):
            await message.channel.send('Sarah, stop.')

    if 'debit card' in message.content:
        await message.channel.send('NO WAYYY')
        await message.channel.send('WHEN???')
    if 'Debit card' in message.content:
        await message.channel.send('NO WAYYY')
        await message.channel.send('WHEN???')
    if 'Debit Card' in message.content:
        await message.channel.send('NO WAYYY')
        await message.channel.send('WHEN???')
    if 'DEBIT CARD' in message.content:
        await message.channel.send('NO WAYYY')
        await message.channel.send('WHEN???')
    if message.content.startswith('over a year ago probably'):
        await message.channel.send('what was a year ago?')
    if message.content.startswith('a year ago probably'):
        await message.channel.send('what was a year ago?')
    if message.content.startswith('about a year ago probably'):
        await message.channel.send('what was a year ago?')
    if message.content.startswith('over a year ago'):
        await message.channel.send('what was a year ago?')
    if message.content.startswith('about a year ago'):
        await message.channel.send('what was a year ago?')
    if message.content.startswith('a year ago'):
        await message.channel.send('what was a year ago?')




    susReasons = ["vented.", "vented right in front of me.", "faked trash.", "faked asteroids.",
                  "killed right in front of me.", "were standing on the body.", "dissapeared while lights were off.",
                  "have been following me.", "haven't done any tasks.", "were the only person not with us.",
                  "took too long to slide their card.", "didn't do download for long enough.",
                  "didn't do upload for long enough.", "faked medbay."]
    susReasoning = random.choice(susReasons)
    randomMember = random.choice(message.guild.members)

    if message.content.startswith('!birthtime'):
        await message.channel.send(message.author.created_at)

    if message.content.startswith('!sus'):
        await message.channel.send(
            f'{randomMember.mention} is kinda sus, they {susReasoning}')

    if message.content.startswith('!members'):
        for member in message.guild.members:
            listedExistingMembers.append(member.name)
        sortedExistingMembers = sorted(listedExistingMembers, key=str.lower)
        memberListLength = len(sortedExistingMembers)
        for i in range(memberListLength):
            await message.channel.send(sortedExistingMembers[i])


    if 'japanese cartoon' in message.content:
        await message.channel.send('Shut it weeb')
    if 'gay' in message.content:
        await message.channel.send('Yes, yes, we all know how gay you are now shut up')
    if 'Gay' in message.content:
        await message.channel.send('Yes, yes, we all know how gay you are now shut up')
    if 'am illiterate' in message.content:
        await message.channel.send('Then go back to grade school')
    if 'Am illiterate' in message.content:
        await message.channel.send('Then go back to grade school')
    if 'am Illiterate' in message.content:
        await message.channel.send('Then go back to grade school')
    if 'Am Illiterate' in message.content:
        await message.channel.send('Then go back to grade school')

    beeMovieRole = discord.utils.get(user.guild.roles, name="Tumi")
    cbtRole = discord.utils.get(user.guild.roles, name="Tumi")

    if cbtRole in message.author.roles:
        if message.content.startswith('!cbt'):
            cbtWikipedia = open('cbt.txt', 'r')
            cbtWikipedia_contents = cbtWikipedia.read()
            for chunk in [cbtWikipedia_contents[i:i + 2000] for i in range(0, len(cbtWikipedia_contents), 2000)]:
                await message.channel.send(chunk)
            cbtWikipedia.close()
    if adminRole in message.author.roles:
        if message.content.startswith('!missileguidance'):
            print(os.getcwd())
            missileguidance = open('missileguidance.txt', 'r')
            missile_contents = missileguidance.read()
            for chunk in [missile_contents[i:i + 2000] for i in range(0, len(missile_contents), 2000)]:
                await message.channel.send(chunk)
            missileguidance.close()

    if adminRole in message.author.roles:
        if message.content.startswith('!beemovie'):
            print(os.getcwd())
            beemoviescript = open('thebeemoviescript.txt', 'r')
            beemovie_contents = beemoviescript.read()
            for chunk in [beemovie_contents[i:i + 2000] for i in range(0, len(beemovie_contents), 2000)]:
                await message.channel.send(chunk)
            beemoviescript.close()

    if adminRole in message.author.roles:
        if message.content.startswith('!morpheus'):
            print(os.getcwd())
            morpheusscript = open('morpheus.txt', 'r')
            morpheus_contents = morpheusscript.read()
            for chunk in [morpheus_contents[i:i + 2000] for i in range(0, len(morpheus_contents), 2000)]:
                await message.channel.send(chunk)
            morpheusscript.close()

    if adminRole in message.author.roles:
        if message.content.startswith('!morpheusvideo'):
            await message.channel.send('https://youtu.be/r9B7BQWnZJs')

    if message.content.startswith('!help'):
        helpsheet = open('bot help sheet.txt', 'r')
        helpsheet_contents = helpsheet.read()
        await message.channel.send(message.author.mention)
        for chunk in [helpsheet_contents[i:i + 2000] for i in range(0, len(helpsheet_contents), 2000)]:
            await message.channel.send(chunk)
        helpsheet.close()

    if adminRole in message.author.roles:
        if message.content.startswith('!cmdspeak'):
            await message.delete()
            speech = input('What would you like to say? \n')
            print('')
            await message.channel.send(speech)



    if adminRole in message.author.roles:
        if message.content.startswith('!speak'):
            speech = message.content
            speak = speech.replace('!speak', '')
            await message.delete()
            await message.channel.send(speak)
            return

    if adminRole in message.author.roles:
        if message.content.startswith('!changepresenceplaying'):
            presencecontent = message.content
            playingpresence = presencecontent.replace('!changepresenceplaying', '')
            await message.delete()
            cmdplayingpresence = discord.Activity(type=discord.ActivityType.playing, name=playingpresence)
            await client.change_presence(activity=cmdplayingpresence)

    if adminRole in message.author.roles:
        if message.content.startswith('!changepresencelistening'):
            listeningcontent = message.content
            listeningpresence = listeningcontent.replace('!changepresencelistening', '')
            await message.delete()
            cmdlisteningpresence = discord.Activity(type=discord.ActivityType.listening, name=listeningpresence)
            await client.change_presence(activity=cmdlisteningpresence)

    if adminRole in message.author.roles:
        if message.content.startswith('!changepresencewatching'):
            watchingcontent = message.content
            watchingpresence = watchingcontent.replace('!changepresencewatching', '')
            a   wait message.delete()
            cmdwatchingpresence = discord.Activity(type=discord.ActivityType.watching, name=watchingpresence)
            await client.change_presence(activity=cmdwatchingpresence)

    if adminRole in message.author.roles:
        if message.content.startswith('!changepresencestreaming'):
            streamingcontent = message.content
            streamingpresence = streamingcontent.replace('!changepresencestreaming', '')
            await message.delete()
            cmdstreamingpresence = discord.Activity(type=discord.ActivityType.streaming, name=streamingpresence)
            await client.change_presence(activity=cmdstreamingpresence)


    if message.content.startswith('among us tonight'):
        await message.channel.send('No, now shut it.')
    if message.content.startswith('we playing tonight?'):
        await message.channel.send('No, now shut it.')
    if message.content.startswith('We playing tonight?'):
        await message.channel.send('No, now shut it.')
    if 'are we playing tonight?' in message.content:
        await message.channel.send('No, now shut it.')
    if 'are we playing today?' in message.content:
        await message.channel.send('No, now shut it.')
    if 'anyone wanna play among us tonight?' in message.content:
        await message.channel.send('No, now shut it.')

    if message.content.startswith('!instant'):
        await message.channel.send('No, now shut it.')


    if message.author.id == 251481402090979329:
        nothing = ''

    if 'fortnite' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason='No Fortnite.')
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'Fortnite' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason='No Fortnite.')
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'FORTNITE' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason='No Fortnite.')
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')


    if 'dibs' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason="Logan Told Me To")
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'Dibs' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason="Logan Told Me To")
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if '-_-' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick()
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')


    if 'ur mom' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason="Please don't kill me.")
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')


    if 'Ur Mom' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason="Please don't kill me.")
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'ur Mom' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason="Please don't kill me.")
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'Ur mom' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason="Please don't kill me.")
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'UR MOM' in message.content:
        if message.author.id != 196762513172463617:
            await user.kick(reason="Please don't kill me.")
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if message.content.startswith('https://cdn.discordapp.com/attachments/775944103397163028/785673887484608532/unknown.png'):
        await message.delete()

    if message.content.startswith('https://tenor.com/view/kirbo-mode-marshmallows-eating-gif-14666697'):
        await message.delete()

    if 'shrek' in message.content:
        await message.channel.send('Shrek is love. Shrek is life.')


    if 'Shrek' in message.content:
        await message.channel.send('Shrek is love. Shrek is life.')
        
    if 'coffee' in message.content:
        await message.channel.send('mmm coffee')

    if message.content.startswith('!opuscheck'):
        await message.channel.send('Opus library is active.')


    if '!vcjoin' in message.content:
        await message.author.voice.channel.connect(reconnect=True)

    if '!vcleave' in message.content:
        channel = message.author.voice.channel
        server = message.guild.voice_client
        await server.disconnect(force=True)

    if message.content.startswith('!audiotest'):
        voice_client.play

    if message.content.startswith('!rngvote'):
        await message.channel.send(f"Vote {randomMember.mention} out. You've got at least a 10% chance of getting it "
                                   f"right.")

    if len(message.attachments) >= 1:
        await message.channel.send("Oh look at this guy, attaching images and stuff. You think you're so great don't you?")

    if 'lol' in message.content:
        await message.channel.send('https://media1.tenor.com/images/8305238eaf271487686de09c373b766b/tenor.gif?itemid=13864254')

    if '$tumiroll' in message.content:
        await message.channel.send('SHUT THE FUCK UP')

    if 'Lol' in message.content:
        await message.channel.send('https://media1.tenor.com/images/8305238eaf271487686de09c373b766b/tenor.gif?itemid=13864254')

    if 'LOL' in message.content:
        await message.channel.send(
            'https://media1.tenor.com/images/8305238eaf271487686de09c373b766b/tenor.gif?itemid=13864254')

    if 'bye' in message.content:
        await message.channel.send('https://media1.tenor.com/images/f7b8f53a5ce812fd5bb422f5bf90dd4b/tenor.gif?itemid=19053721')

    if 'Bye' in message.content:
        await message.channel.send('https://media1.tenor.com/images/f7b8f53a5ce812fd5bb422f5bf90dd4b/tenor.gif?itemid=19053721')

    if '<@!251481402090979329>' in message.content:
        await message.channel.send('<@!251481402090979329>')


    if 'cat' in message.content:
        await message.channel.send('<@251481402090979329>')
        await message.channel.send('https://media.discordapp.net/attachments/775941210119733269/777561607839547402/image0.jpg?width=400&height=219')

    if 'Cat' in message.content:
        await message.channel.send('<@251481402090979329>')
        await message.channel.send('https://media.discordapp.net/attachments/775941210119733269/777561607839547402/image0.jpg?width=400&height=219')

    if 'dog' in message.content:
        await message.channel.send('<@349682083922444298>')
        await message.channel.send('https://tenor.com/view/butta-dawg-dog-with-the-butta-butta-dog-i-put-the-butter-on-him-the-dog-with-the-butter-butter-dog-gif-19244197')

    if 'Dog' in message.content:
        await message.channel.send('<@349682083922444298>')
        await message.channel.send('https://tenor.com/view/butta-dawg-dog-with-the-butta-butta-dog-i-put-the-butter-on-him-the-dog-with-the-butter-butter-dog-gif-19244197')

    if '$m' in message.content:
        if message.content == '$m':
            await message.channel.send('Jin-Woo Sung')

    if '$h' in message.content:
        if message.content == '$h':
            await message.channel.send('Jin-Woo Sung')

    if '$M' in message.content:
        if message.content == '$M':
            await message.channel.send('Jin-Woo Sung')

    if '$H' in message.content:
        if message.content == '$H':
            await message.channel.send('Jin-Woo Sung')

    if message.content.startswith('!time'):
        timenow = datetime.datetime.now()
        current_time = timenow.strftime("%H:%M:%S")
        await message.channel.send("Current Time - " + current_time)
        print(timenow)

    if message.content.startswith('!encrypt'):

        encryptcontent = message.content
        encryptioncontent = encryptcontent.replace('!encrypt', '')
        def encryptionprocess():
            print('')
            for eachletter in encryptioncontent:
                if eachletter in uppercase_index:
                    crypt = uppercase_index.index(eachletter)
                    encryption = ((0 + 25) - crypt)
                    encryptedvalues.append(encryption)
                    newcharacter = uppercase_index[encryption]
                    encryptedtext.append(newcharacter)
                elif eachletter in lowercase_index:
                    crypt = lowercase_index.index(eachletter)
                    encryption = ((0 + 25) - crypt)
                    encryptedvalues.append(encryption)
                    newcharacter = lowercase_index[encryption]
                    encryptedtext.append(newcharacter)
                elif eachletter in special_index:
                    crypt = special_index.index(eachletter)
                    encryption = (crypt + 0)
                    encryptedvalues.append(encryption)
                    newcharacter = special_index[encryption]
                    encryptedtext.append(newcharacter)

        # Decryption function declaration
        def decryptionprocess():
            print('')
            for eachletter in encryptioncontent:
                if eachletter in uppercase_index:
                    decipher = uppercase_index.index(eachletter)
                    decryption = ((0 + 25) - decipher)
                    decryptedvalues.append(decryption)
                    newcharacter = uppercase_index[decryption]
                    decryptedtext.append(newcharacter)
                elif eachletter in lowercase_index:
                    decipher = lowercase_index.index(eachletter)
                    decryption = ((0 + 25) - decipher)
                    decryptedvalues.append(decryption)
                    newcharacter = lowercase_index[decryption]
                    decryptedtext.append(newcharacter)
                elif eachletter in special_index:
                    decipher = special_index.index(eachletter)
                    decryption = (decipher + 0)
                    decryptedvalues.append(decryption)
                    newcharacter = special_index[decryption]
                    decryptedtext.append(newcharacter)
        # Action as a a result of chosen process
        encryptionprocess()
        con_encryptedtext = ''.join(encryptedtext)
        await message.channel.send(con_encryptedtext)
        encryptedtext = []
        encryptedvalues = []
        decryptedtext = []
        decryptedvalues = []

    if message.content.startswith('!decrypt'):
        print('active')



@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    print(client.user.id)
    print('----------------------------')




client.run(TOKEN)