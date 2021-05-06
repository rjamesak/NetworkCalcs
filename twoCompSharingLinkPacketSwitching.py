from math import floor, ceil

R = float(input('max trans rate (Mbps): '))
Afile = int(input('file size A (Bytes): '))
Bfile = int(input('file size B (bytes): '))
Ldata = int(input('packet payload size (bytes): '))
Lheader = int(input('packet header size (bytes): '))

# convert file sizes to bits
Afile = Afile*8
Bfile = Bfile*8
# convert rate to bps
KbPerMb = 1000
bPerKb = 1000
R = R * KbPerMb * bPerKb
# convert packet size and header to bits
Ldata *= 8
Lheader *= 8
# find how many packets needed for each file
Apackets = ceil(Afile/Ldata)
Bpackets = ceil(Bfile/Ldata)
# determing packets needed to complete, assume interleaving
ATotalPackets = 0
BTotalPackets = 0
if Apackets < Bpackets:
    ATotalPackets = Apackets * 2
    BTotalPackets = Bpackets + Apackets
else:
    BTotalPackets = Bpackets * 2
    ATotalPackets = Apackets + Bpackets

# add header to packet size
L = Ldata + Lheader

# calc delay
timeB = (L/R) * BTotalPackets
timeA = (L/R) * ATotalPackets

print('time for A to finish: ', timeA, ' sec')
print('time for B to finish: ', timeB, ' sec')
