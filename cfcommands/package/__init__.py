import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

log = logging.getLogger("ballsdex.packages.cfcommands")


async def setup(bot: "BallsDexBot"):
    log.info("Loading CFCommands package...")
    from .cog import CFCommands

    await bot.add_cog(CFCommands(bot))
    log.info("CFCommands package loaded successfully!")
