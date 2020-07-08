
"""Use cmd `.akmabc` to blast"""

from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.akmabc", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("A")
    await asyncio.sleep(0.2)
    await event.edit("B")
    await asyncio.sleep(0.2)
    await event.edit("C")
    await asyncio.sleep(0.2)
    await event.edit("D")
    await asyncio.sleep(0.2)
    await event.edit("E")
    await asyncio.sleep(0.2)
    await event.edit("F")
    await asyncio.sleep(1.2)
    await event.edit("G")
    await asyncio.sleep(0.2)
    await event.edit("H")
    await asyncio.sleep(0.2)
    await event.edit("I")
    await asyncio.sleep(0.2)
    await event.edit("J")
    await asyncio.sleep(0.2)
    await event.edit("K")
    await asyncio.sleep(0.2)
    await event.edit("L")
    await asyncio.sleep(0.2)
    await event.edit("M")
    await asyncio.sleep(0.2)
    await event.edit("N")
    await asyncio.sleep(0.2)
    await event.edit("O")
    await asyncio.sleep(0.2)
    await event.edit("P")
    await asyncio.sleep(0.2)
    await event.edit("Q")
    await asyncio.sleep(0.2)
    await event.edit("R")
    await asyncio.sleep(0.2)
    await event.edit("S")
    await asyncio.sleep(0.2)
    await event.edit("T")
    await asyncio.sleep(0.2)
    await event.edit("U")
    await asyncio.sleep(0.2)
    await event.edit("V")
    await asyncio.sleep(0.2)
    await event.edit("W")
    await asyncio.sleep(0.2)
    await event.edit("X")
    await asyncio.sleep(0.2)
    await event.edit("Y")
    await asyncio.sleep(0.2)
    await event.edit("Z")
    await asyncio.sleep(2)
    await event.delete()
    
    

    
