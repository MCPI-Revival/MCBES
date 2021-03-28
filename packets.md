# Packets \(WIP)

## What is this for?
This file is to explain the packet protocols that *Minecraft Pi* and *Minecraft Bedrock* use, and how we can change one to the other (will be updated as we learn more).

## wiki.vg links
[*Pi Protocol*](https://wiki.vg/Pocket_Minecraft_Protocol)

[*Bedrock Protocol*](https://wiki.vg/Bedrock_Protocol)

## Data Types
Name | Size | Range | Notes
---- | ---- | ----- | -----
byte | 1 | -128 to 127 | Signed, two's complement
Unsigned byte | 1 | 0 to 255 | 
int32 | 4 | -2147483648 to 2147483647 | Signed, two's complement
int64 | 8 |  | Maybe a double?
MAGIC | 16 |  | 0x00ffff00fefefefefdfdfdfd12345678 always those hex bytes, corresponding to RakNet's default OFFLINE_MESSAGE_DATA_ID
string, String| = 1 | N/A | Prefixed by a short containing the length of the string in characters. It appears that only the following ASCII characters can be displayed: !"#$%&'()\*+,-./0123456789:;<=\>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^\_\`abcdefghijklmnopqrstuvwxyz{\|}~
Boolean | 1 | 0 or 1 | A Byte treated as boolean, 0 is false but anything greater then that is true
Short | 2 | -32768 to 32767 | Unsigned
Unsigned Short | 2| 0 to 65535 | Signed
Int | 4 | -2147483648 to 2147483647 | Signed little-endian 32-bit Integer
Int (big endian) | 4 | -2147483648 to 2147483647 | Signed big-endian 32-bit Integer
Unsigned Int | 4 | 0 to 4294967295 | Unsigned 32-bit Integer
Long | 8 | -2^63 to 2^63-1 | Signed 64-bit Integer
Unsigned Long | 8 | 2^64-1 | Unsigned 64-bit Integer
Float | 4 |  |  A single-precision 32-bit IEEE 754 Floating point number
Double|  8 | |  A Double-precision 64-bit IEEE 754 Floating point number
VarInt |  ≥ 1, ≤ 5 | 0 to 4294967295 |  
SignedVarInt | ≥ 1, ≤ 5 | -2147483648 and 2147483647 
VarLong | ≥ 1, ≤ 10 | |  
SignedVarLong | ≥ 1, ≤ 10|  -2^63 and 2^63-1 | 
Vector3 | 12 | |  Three Float values (X, Y and Z respectively)
Vector2 |  8 | | Two Float values (X and Y respectively)
NBT | | | The data representing a block or an enity's state
ByteArray  | | |  An arbitrary array of Bytes prefixed with its size in Bytes as a VarInt.
BlockCoordinates | ≥ 3, ≤ 15 | |  A SignedVarInt, a normal VarInt and another SignedVarInt (X, Y and Z respectively)
PlayerLocation | 15 | |  Three Float values (X, Y and Z respectively), followed by three Bytes (pitch, head yaw and yaw respectively). To convert the Bytes to normal pitch and yaw values divide them by 0.71
UUID | 16 | | A UUID Encoded as two unsigned 64-bit Integers: the most significant 64 bits and the least significant 64 bits
Item | | | 
ItemStacks | | | 
Itemstates | | | 
EntityAttributes | | | 
PlayerAttributes | | | 
Skin | | |
Recipes | | |
GameRules | | |
Transaction | | |
BlockPalette | | |
ScoreEntries | | |
MapInfo | | |
PlayerRecords | | |
ScoreboardIdentityEntries | | |
MetadataDictionary | | |
PotionTypeRecipe | | |
PotionContainerChangeRecipe  | | | 
ResourcePackInfos | | |
ResourcePackIdVersions  | | | 
ResourcePackIds | | |

## Packets 
### Minecraft Bedrock
#### List Of All Packets
| Packet ID | Headed To | Field Name | Type of Field | Notes |
| ----------- | ------------- | ------------- | --------------| --------- |
|0x01 | Server | <table> <tr><td>  Protocol Version </td> </tr> <tr> <td> Chain Data </td>  </tr> <tr> <td> Skin Data</td>  </tr> </table> | <table> <tr> <td> int </td> </tr> <tr> <td> json array of JWT data </td> </tr> <tr> <td> JWT data </td> </tr> </table> | <table> <tr>  <td>N/A</td> </tr> <tr> <td> Contains the display name, UUID and XUID </td> </tr> <tr> <td> N/A</td>  </tr> </table> |


### Minecraft Pi
#### List Of All Packets
WIP

### Comparisons
WIP


## FAQ
### What is a signed number?
A signed number is one that has the potential to be both positive and negative. A signed number uses one bit to represent if it is positive or negative. An unsigned object can store more data because it doen't use that bit to store whether it is positive or negative. 



### Copyright MCPI-Revival 2021. (apache license)
