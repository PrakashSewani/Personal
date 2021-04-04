import discord
from discord_webhook import DiscordWebhook, DiscordEmbed
import os
import time
import requests

client=discord.Client()
mainlist=[]

def Entry(mainlist,entry):
    datalist=mainlist
    datalist.append(entry)
    mainlist=datalist
    return

def Levelup(mainlist,attri):
    templist=mainlist
    for i in templist:
        if(i==attri):
            j=templist.index(attri)
            templist[j-1],templist[j]=templist[j],templist[j-1]
            break
        
        else:
            continue
    
    templist1=mainlist

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='$payment'))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content.startswith('$payment'):
        await message.channel.send('Here are the available payment methods!')
        embed=discord.Embed(title="Payment Methods",color=0xFF5733)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/740276750092861441/827793922729312306/1573626372546.jpg?width=242&height=464")
        embed.add_field(name="Googlepay and PhonePe", value="+91 75074 99218", inline=False)
        embed.add_field(name="Paytm", value="Image attached for UPI QR Code", inline=False)
        embed.add_field(name="UPI ID", value="mayurshah048@okicici", inline=True)
        await message.channel.send(embed=embed)
             
    if message.content.startswith('payment done'):
        await message.channel.send('We are processing your request')

    if message.content.startswith('add user'):
        cmd = message.content.split()[0].replace("_","")
        if len(message.content.split()) > 1:
            parameters = message.content.split()[0:]
        
        for i in parameters:
            if(i=='add' or i=='user'):
                continue
            else:
                await message.channel.send(i+' has been added to the queue!')
                Entry(mainlist,i)
    
    if message.content.startswith('level up'):
        cmd = message.content.split()[0].replace("_","")
        if len(message.content.split()) > 1:
            parameters = message.content.split()[0:]

        for i in parameters:
            if(i=='level' or i=='up'):
                continue
            else:
                Levelup(mainlist,i)
                await message.channel.send(i+' has been moved up to the queue by one position!')

    if message.content.startswith('reset'):
        await message.channel.send('The Queue has been reset!')
        mainlist.clear()
        #Reset(mainlist)
    
    if message.content.startswith('view queue'):
        await message.channel.send("Here is today's Queue!")
        for j in mainlist:
            await message.channel.send(j)

client.run('ODI3ODM1NzcyMTQ5MzAxMjY5.YGg0JA.MS39W__h-G0X5mzNCmr2b7upxdY')