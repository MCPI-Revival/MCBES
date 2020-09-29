# Packets

## What is this for?
This file is to explain the packet protocols that *Minecraft Pi* and *Minecraft Bedrock* use, and how we can change one to the other (will be updated as we learn more).

## wiki.vg links
[*Pi Protocol*](https://wiki.vg/Pocket_Minecraft_Protocol)

[*Bedrock Protocol*](https://wiki.vg/Bedrock_Protocol)

## Data Types
Name | Size | Range | Notes
---- | ---- | ----- | -----
byte | 1 | -128 to 127 | Signed, two's complement
short	| 2	| -32768 to 32767	| Signed, two's complement
int32	| 4	| -2147483648 to 2147483647	| Signed, two's complement
int64	| 8	|  | Maybe a double?
MAGIC	| 16 |  | 0x00ffff00fefefefefdfdfdfd12345678	always those hex bytes, corresponding to RakNet's default OFFLINE_MESSAGE_DATA_ID
string|	= 1	| N/A	| Prefixed by a short containing the length of the string in characters. It appears that only the following ASCII characters can be displayed: !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{\|}~
