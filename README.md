# RFID-card
Script for getting EM-number from NTNU access card

The NTNU access cards have two different chips in them. A 13.56 MHz Mifare Classic 1K and a 125 KHz chip. From these chips one can read out the M- and EM-numbers respectively. This script finds the EM number.

I used a Raspberry Pi and an UART enabled 125 KHz rfid reader bought at [Omega Verksted](omegav.no). 

The card emits 10 bytes when read. These are on the format

| Start | Length | Type   | ID          | Parity | Stop |
|-------|--------|--------|-------------|--------|------|
| 0x02  | 0x0A   | 0x0201 | 0xXXXX XXXX | 0xXX   | 0x03 |

If each byte in the the 4 byte ID is reversed and converted to decimal you get the EM-number printed at the bottom of the backside of your card.

The EM-number itself does not seem to have any check sums and are likely just incremented for each card issued.


The information at https://dvikan.no/hvordan-fungerer-ntnu-adgangskortene has been useful. He also gives some information about the Mifare chips. 
