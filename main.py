import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

async def load_extensions():
    if not os.path.exists('./cogs'):
        print("❌ 'cogs' is not found")
        return

    print(f"🔄 {bot.user} Cogs load...\n" + "-"*30)
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_name = f'cogs.{filename[:-3]}'
            try:
                await bot.load_extension(cog_name)
                print(f"✅ Loaded: {cog_name}")
            except Exception as e:
                print(f"❌ Failed to load: {cog_name}")
                print(f"   Error: {e}")
                
    print("-"*30 + "\n🚀 Cogs loading process complete!")

@bot.event
async def on_ready():
    print(f'✅ Bot is online and ready! Logged in as {bot.user}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start('MTUyNzY5MDAyMzk1MDg3Njg4NQ.G8PiRV.nq_abStAuWJmnFbzmPS0mcdRqyT86A2yBq2yyE')

if __name__ == '__main__':
    asyncio.run(main())