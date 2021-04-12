
import random
import os
import discord
from discord import client
from discord import voice_client
import datetime



TOKEN = str(os.environ.get('BOTTOKEN'))

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

reactionImages = ["https://cdn.discordapp.com/attachments/763590055948189696/788059504532389938/image0.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/808126193614323732/2Q.png", "https://cdn.discordapp.com/attachments/763590055948189696/804382226309185546/image0.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764638377246720/image0.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764638514872320/image1.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764638687494174/image2.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764638917394463/image3.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764639102074930/image4.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764639299469382/image5.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764639509315604/image6.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764639781421126/image7.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764640025346058/image8.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764640175816774/image9.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764715270504468/image0.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764715447582790/image1.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764715569479700/image2.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764715816157214/image3.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764715979341864/image4.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764716282380358/image5.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764716449759342/image6.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764716605472839/image7.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764716931973150/image8.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764717171441706/image9.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764799325536286/image0.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764799559761940/image1.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764799743787039/image2.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764799874203708/image3.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764800185368597/image4.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764800386564126/image5.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764800641892372/image6.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764800788168714/image7.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764801145077790/image8.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764801459388417/image9.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764849413128192/image0.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764849639751720/image1.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764849866768454/image2.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764850147393536/image3.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764850307301376/image4.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764850570756157/image5.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764850772213770/image6.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764851111559188/image7.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764851397427210/image8.jpg", "https://cdn.discordapp.com/attachments/763590055948189696/825764851593773107/image9.jpg"
]

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
    invite = await channel.create_invite()
    await member.create_dm
    await channel.send("Alright, come back now: " + invite)

@client.event
async def on_member_join(member):
    joinEvents = ["became a demon slayer.", "obtained the exaggerated swagger of a black teen.", "joined Logan's cult "
                                                                                                 "of degeneracy.",
                  "stopped his own heart with Star Platinum.", "became chickne snaddich.", "is being sponsored by "
                                                                                           "Raid: Shadow Legends.", "stole Hawks from Emmy", "stole Hak from Sarah.", ]
    joinEvent = random.choice(joinEvents)
    channel = client.get_channel(775941210119733269)
    await channel.send(f"{member.mention} {joinEvent}")
    role = discord.utils.get(member.server.roles, name=tumi)
    if member.id == 196762513172463617:
        await client.add_roles(member, role)

@client.event
async def on_member_update(before,after):
    if 'tumi' in str(after.roles):
        if 'tumi' in member.roles:
            await member.remove_roles('tumi')




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
    if len(message.attachments) >= 1:
        print ("Message: " + str(message.content))
        print ("Attachment(s): " + str(message.attachments))
        store.write("Message: " + str(message.content) + "\n")
        store.write("Attachment(s): " + str(message.attachments) + "\n")
    else:
        print ("Message: " + str(message.content))
        store.write("Message: " + message.content + "\n")
    print("")
    store.write("\n")
    store.close()

    if 'damn' in message.content.lower():
        if message.channel.id == 826796405293056030:
            if message.author.id != 779526567877541938:
                await message.delete()
            await message.channel.send('***damn***')

    if message.author == client.user:
        return

    if 'damn' in message.content.lower():
        await message.channel.send('***damn***')

    if 'Direct Message' in channelinuse:
        if authuser != 'MaximusWrath346#5386':
            user = client.get_user(196762513172463617)
            recieved_message = str(message.content)
            await user.send(authuser + ': ' + recieved_message)


    if channelinuse == 'Direct Message with MaximusWrath346#5386':
        channel = client.get_channel(775944103397163028)
        user = client.get_user(641267423604899870)
        message_send = message.content
        await channel.send(message_send)




    # Role Definition
    existingMembers = message.guild.members
    existingMembers = message.guild.members
    listedExistingMembers = []

    adminRole = discord.utils.get(user.guild.roles, name="tumi")

    beeMovieRole = discord.utils.get(user.guild.roles, name="tumi")


    if 'supercalifragilisticexpialidDMcius' in message.content:
        await message.channel.send("Hi! I don't really have much DM functionality right now, but my Creator is working on it!")

    if message.content.startswith('Hey son'):
        await message.channel.send('Hi Dad!')
    if message.content.startswith('hey son'):
        await message.channel.send('Hi Dad!')
    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.lower().startswith('gn'):
        await message.channel.send('Goodnight!')
    if message.content.lower().startswith('goodnight'):
        await message.channel.send('Goodnight!')
    if message.content.lower().startswith('good night'):
        await message.channel.send('Goodnight!')
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

    if 'Doug Dimmadome' in message.content:

        await message.channel.send( 'Doug Dimmadome?')
        await message.channel.send('Owner of the Dimmsdale Dimmadome?')

    if message.content.startswith('Yes, Doug Dimmadome, owner of the Dimmsdale Dimmadome'):
        await message.channel.send('Ah yes, Doug Dimmadome')
        await message.channel.send('Owner of the Dimmsdale Dimmadome')


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

    if 'sus' in message.content.lower():
        await message.channel.send('⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌ ⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌ '
                                   '⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌ ⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪ '
                                   '⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡ ⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐ '
                                   '⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔ ⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘ '
                                   '⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎ ⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗ '
                                   '⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷ ⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟ '
                                   '⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰ ⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊ '
                                   '⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌ ⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁ '
                                   '⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀ ⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀ '
                                   '⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟ ⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾ '
                                   '⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽')

    if 'amogus' in message.content:
        await message.channel.send('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⣀⣀.⣀⡀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠉⠉⠉⠉⠉⠉⠉⠙⠻⢶⣄⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⣠⣶⠛⠛⠛⠛⠛⠛⠳⣦⡀⠀⠘⣿⡄⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⢹⣿⣦⣀⣀⣀⣀⣀⣠⣼⡇⠀⠀⠸⣷⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠉⠛⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⣿⡄⣠ ⠀⠀⢀⣀⣀⣀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀ ⠿⠿⠟⠛⠛⠉⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀ ⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀ ⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀ ⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⣠⡶⠶⠿⠿⠿⠿⢷⣦⠀⠀⠀⠀⠀⠀⠀⣿⠀ ⠀⠀⣀⣀⣀⠀⣸⡇⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⠀ ⣠⡿⠛⠛⠛⠛⠻⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⣿⠀ ⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀⢀⣤⣤⣴⣿⠀⠀⠀⠀⠀⠀⠀⣿⠀ ⠈⠙⢷⣶⣦⣤⣤⣤⣴⣶⣾⠿⠛⠁⢀⣶⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀ ⢷⣶⣤⣀⠉⠉⠉⠉⠉⠄⠀⠀⠀⠀⠈⣿⣆⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡾⠃⠀ ⠀⠈⠉⠛⠿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢿⣿⣾⣿⡿⠿⠟⠋⠁⠀⠀⠀')

    if '**LittleHanger** and' in message.content:
        await message.channel.send("Hey Logan? Fuck you. That is all. Maybe you did something, maybe you didn't, but this is a preemptive measure.")
        await message.channel.send('-Tumi')

    if 'japanese cartoon' in message.content.lower():
        await message.channel.send('Shut it weeb')
    if 'gay' in message.content.lower():
        if message.author.id == 196762513172463617:
            if 'not gay' in message.content.lower():
                await message.channel.send('True that is indeed very much not gay.')
            else:
                await message.channel.send('Yes, very much gay')

        else:
            await message.channel.send('Yes, yes, we all know how gay you are now shut up')

    if 'am illiterate' in message.content.lower():
        await message.channel.send('Then go back to grade school')

    if message.content.startswith('!telltalegame'):
        await message.delete()
        await message.channel.send(f'{message.author.mention} *will remember that.*')


    if 'Am Illiterate' in message.content:
        await message.channel.send('Then go back to grade school')

    beeMovieRole = discord.utils.get(user.guild.roles, name="tumi")
    cbtRole = discord.utils.get(user.guild.roles, name="tumi")

    print (channelinuse)





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

    if 'my man' in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/attachments/775944001148813332/804373419751112716/Z.png')

    if 'pain' in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/attachments/775944001148813332/804373905501716541/Z.png')

    if message.content.lower().startswith('my man'):
        await message.channel.send('https://cdn.discordapp.com/attachments/775944001148813332/804373460394442772/Z.png')

    if message.content.lower().startswith('!reactionimage'):
        await message.delete()
        chosenReactionImage = random.choice(reactionImages)
        await message.channel.send(f"{message.author.mention}, here's your reaction image:")
        await message.channel.send(chosenReactionImage)

    if message.content.lower().startswith('!ri'):
        await message.delete()
        chosenReactionImage = random.choice(reactionImages)
        await message.channel.send(f"{message.author.mention}, here's your reaction image:")
        await message.channel.send(chosenReactionImage)

    if message.content.lower().startswith('I need a reaction image'):
        await message.delete()
        chosenReactionImage = random.choice(reactionImages)
        await message.channel.send(f"{message.author.mention}, here's your reaction image:")
        await message.channel.send(chosenReactionImage)

    if 'is for me' in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/attachments/763590055948189696/804382226309185546/image0.jpg')


    if adminRole in message.author.roles:
        if message.content.startswith('!speak'):
            speech = message.content
            speak = speech.replace('!speak', '')
            await message.delete()
            await message.channel.send(speak)
            return

    if message.content.lower().startswith('!ga'):
        givestuffmessage = message.content
        givestuffmessagebreakdown = givestuffmessage.replace('!ga', '')
        givelist = open('givelist.txt', 'a')
        givelist.write(givestuffmessagebreakdown + "\n")
        givelist.close()
        emoji = '✅'
        await message.add_reaction(emoji)
    if adminRole in message.author.roles:
        if message.content.lower().startswith('!gr'):
            giveremovemessage = message.content
            giveremovemessagebreakdown = giveremovemessage.replace('!gr', '')
            givelist = open('givelist.txt', 'r')
            if giveremovemessagebreakdown in givelist.read():
                lines = givelist.readlines()
                givelist.close()
                givelist = open('givelist.txt', 'a')
                for line in lines:
                    if line.strip("\n") == giveremovemessagebreakdown:
                        linetoberemoved = False
                    else:
                        givelist.write(line)
                givelist.close()
                emoji = '✅'
                await message.add_reaction(emoji)

    if adminRole in message.author.roles:
        if message.content.startswith('!gl'):
            givelist = open('givelist.txt', 'r')
            givelistcontent = givelist.read()
            for chunk in [givelistcontent[i:i + 2000] for i in range(0, len(givelistcontent), 2000)]:
                await message.channel.send(chunk)
            givelist.close()
            emoji = '✅'
            await message.add_reaction(emoji)



    if adminRole in message.author.roles:
        if message.content.lower().startswith('!kick'):
            kickrequest = message.content
            kickrequest = kickrequest.replace('!kick ', '')
            kickrequest = kickrequest.replace('<@!', '')
            kickrequest = kickrequest.replace('>', '')
            await message.delete()
            kickrequestuser = message.guild.get_member(int(kickrequest))
            await message.guild.kick(kickrequestuser)

    if adminRole in message.author.roles:
        if message.content.lower().startswith('!ban'):
            banrequest = message.content
            banrequest = banrequest.replace('!ban ', '')
            banrequest = banrequest.replace('<@!', '')
            banrequest = banrequest.replace('>', '')
            await message.delete()
            banrequestuser = message.guild.get_member(int(banrequest))
            await message.guild.ban(banrequestuser)

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
            await message.delete()
            cmdwatchingpresence = discord.Activity(type=discord.ActivityType.watching, name=watchingpresence)
            await client.change_presence(activity=cmdwatchingpresence)

    if adminRole in message.author.roles:
        if message.content.startswith('!changepresencestreaming'):
            streamingcontent = message.content
            streamingpresence = streamingcontent.replace('!changepresencestreaming', '')
            await message.delete()
            cmdstreamingpresence = discord.Activity(type=discord.ActivityType.streaming, name=streamingpresence)
            await client.change_presence(activity=cmdstreamingpresence)


    if message.content.lower().startswith('$ci'):
        await message.delete()

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
        if message.content.lower().startswith('$wish megumin'):
            await message.channel.send("ALERT! ALERT! LOGAN IS BEING A FUCKWAD")
            await message.channel.send('<@!196762513172463617>')
            await message.channel.send("ALERT! ALERT! LOGAN IS BEING A FUCKWAD")
            await message.channel.send('<@!196762513172463617>')
            await message.channel.send("ALERT! ALERT! LOGAN IS BEING A FUCKWAD")
            await message.channel.send('<@!196762513172463617>')
        if 'cuck' in message.content:
            await message.channel.send('Dictionary Definition:'
                                       'DEROGATORY•INFORMAL'
                                       '1. a weak or servile man (often used as a contemptuous term for a man with moderate or progressive political views).'
                                       '2. a man whose wife is sexually unfaithful; a cuckold.')
            await message.channel.send('Urban Definition:'
                                        'A man who lets his wife or girlfriend have sex with other men. Often the man lets her do whatever she wants and treat him like shit.'
                                        '(Short version of cuckold)')




    if 'dang' in message.content.lower():
        await message.channel.send('***dang***')

    if 'darn' in message.content.lower():
        await message.channel.send('***darn***')

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

    if '_' in message.content:
        if message.author.id == 251481402090979329:
            await message.channel.send('https://cdn.discordapp.com/attachments/763590055948189696/808126193614323732/2Q.png')

    if 'one piece' in message.content:
        if message.author.id == 224988545402535936:
            await user.kick()
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if '0ne p1ece' in message.content:
        if message.author.id == 224988545402535936:
            await user.kick()
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')


    if '1piece' in message.content:
        if message.author.id == 224988545402535936:
            await user.kick()
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if '1Piece' in message.content:
        if message.author.id == 224988545402535936:
            await user.kick()
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'one peice' in message.content:
        if message.author.id == 224988545402535936:
            await user.kick()
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'one b °C' in message.content:
        if message.author.id == 224988545402535936:
            await user.kick()
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if ' ice ' in message.content.lower():
        await message.channel.send(':cold_face:')

    if message.content.startswith('!suicide'):
        await user.kick()
        await message.channel.send('https://cdn.discordapp.com/attachments/775943975055130625/795858624656048128/image0.jpg')

    if message.content.startswith('op'):
        if message.author.id == 224988545402535936:
            await user.kick()
            await message.channel.send('https://cdn.discordapp.com/attachments/788121984327745546/788122182789365780/image1.jpg')

    if 'On3 P13c3' in message.content:
        if message.author.id == 224988545402535936:
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

    if message.content.lower().startswith('$top1000'):
        await message.delete()

    if 'lol' in message.content:
        await message.channel.send('https://media1.tenor.com/images/8305238eaf271487686de09c373b766b/tenor.gif?itemid=13864254')

    if 'tumiroll' in message.content:
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


    if ' cat  ' in message.content.lower():
        await message.channel.send('https://media.discordapp.net/attachments/775941210119733269/777561607839547402/image0.jpg?width=400&height=219')




    if message.content.lower().startswith('$m'):
        if message.content.lower() == '$m':
            await message.delete()
        if message.content.lower() == '$ma':
            await message.delete()
        if message.content.lower() == '$mg':
            await message.delete()

    if message.content.lower().startswith('$w'):
        if message.content.lower() == '$w':
            await message.delete()
        if message.content.lower() == '$wa':
            await message.delete()
        if message.content.lower() == '$wg':
            await message.delete()

    if message.content.lower().startswith('$h'):
        if message.content.lower() == '$h':
            await message.delete()
        if message.content.lower() == '$ha':
            await message.delete()
        if message.content.lower() == '$hg':
            await message.delete()

    if 'oatmeal raisin' in message.content:
        await message.channel.send('***dammit***')

    if 'Oatmeal Raisin' in message.content:
        await message.channel.send('***dammit***')

    if 'Oatmeal raisin' in message.content:
        await message.channel.send('***dammit***')



    if message.content.startswith('!time'):
        timenow = datetime.datetime.now()
        current_time = timenow.strftime("%H:%M:%S")
        await message.channel.send("Current Time - " + current_time)
        print(timenow)


    if message.channel.id == 775945092489805834:
        if message.author.id == 251481402090979329:
            await message.delete()
        if message.author.id == 432610292342587392:
            await message.delete()


    if message.author.id != 251481402090979329:
        if message.content.startswith('!wlcounter'):
            dafile = open('storage.txt', 'r')
            lines = list(dafile)
            dafile.close()
            wishcounter = 0
            tjwishcounter = 0
            natewishcounter = 0
            loganwishcounter = 0
            tumiwishcounter = 0
            emmywishcounter = 0
            sarahwishcounter = 0
            willwishcounter = 0
            for i in lines:
                if 'Wished by <@' in i:
                    wishcounter = wishcounter + 1
                    if '349682083922444298' in i:
                        tjwishcounter = tjwishcounter + 1
                    if '224988545402535936' in i:
                        natewishcounter = natewishcounter + 1
                    if '251481402090979329' in i:
                        loganwishcounter = loganwishcounter + 1
                    if '196762513172463617' in i:
                        tumiwishcounter = tumiwishcounter + 1
                    if '641267423604899870' in i:
                        emmywishcounter = emmywishcounter + 1
                    if '427287857909071872' in i:
                        sarahwishcounter = sarahwishcounter + 1
                    if '304609945549275139' in i:
                        willwishcounter = willwishcounter + 1
            await message.channel.send('Number of Characters Rolled While Wishlisted: ' + str(wishcounter))
            await message.channel.send("(Please keep in mind this is only characters who were actively on someone's wishlist when rolled)")
            await message.channel.send('TJ - ' + str(tjwishcounter))
            await message.channel.send('Nate - ' + str(natewishcounter))
            await message.channel.send('Logan - ' + str(loganwishcounter))
            await message.channel.send('Tumi - ' + str(tumiwishcounter))
            await message.channel.send('Emmy - ' + str(emmywishcounter))
            await message.channel.send('Sarah - ' + str(sarahwishcounter))
            await message.channel.send('Will - ' + str(willwishcounter))




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