from .ptz import PTZ

async def setup(bot):
    bot.add_cog(PTZ(bot))
