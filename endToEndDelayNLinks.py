links = int(input('Routers between hosts: '))
R = input('transmission rate (Mbps): ')
d = input('distance packet will travel (km): ')
s = float(input('speed travelled along wire (*10^8): '))*(10**8)
L = input('packet size (Bytes): ')

# add initial uplink
links += 1
# convert rate to bps
KbPerMb = 1000
bPerKb = 1000
R = float(R) * KbPerMb * bPerKb
# convert packet to bits
L = float(L) * 8
# convert distance to meters
d = float(d)*1000

delayT = L/R * links
delayP = d/s

# add delays to get end to end delay
delayETE = delayT + delayP

print('end to end delay: ', delayETE, ' sec')
print('end to end delay: ', delayETE*1000, ' ms')
