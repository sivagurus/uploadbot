#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


import asyncio
import os
import time
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser



async def converlt_video(video_file, output_directory):
    out_put_file_name = output_directory + \
        "/" + str(round(time.time())) + ".mp4"
    file_genertor_command = [
        "ffmpeg",
        " -i ",
        video_file,
        " -c:v libx264",
        " -c:a copy"
        " -preset veryslow ",
        out_put_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,a=await bot.send_message(chat_id=update.chat.id,text=Translation.CVTD_SUCESSFULL,reply_to_message_id=update.message_id),
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    else:
        return None
