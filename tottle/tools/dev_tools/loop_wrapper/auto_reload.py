import os
import sys

from watchgod import awatch

from loguru import logger

_startup_cwd = os.getcwd()


def restart():
    args = sys.argv[:]
    logger.debug("Restarting: %s" % " ".join(args))
    args.insert(0, sys.executable)
    if sys.platform == "win32":
        args = ['"%s"' % arg for arg in args]

    os.chdir(_startup_cwd)
    os.execv(sys.executable, args)


async def watch_to_reload(check_dir: str):
    async for _ in awatch(check_dir):
        logger.info("Changes were found. Restarting...")
        restart()
