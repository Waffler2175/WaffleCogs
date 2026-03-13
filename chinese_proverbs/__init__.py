from .mycog import ProverbsCog


async def setup(bot):
    await bot.add_cog(ProverbsCog(bot))
