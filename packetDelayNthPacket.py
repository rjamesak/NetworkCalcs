
d = input('distance packet will travel (km): ')
s = float(input('speed packet travels along wire (m/s): '))*(10**8)
L = input('packet size (Bytes): ')
R = input('transmission rate (Mbps): ')
N = int(input('find delay of which packet? '))

# convert d to meters
d = float(d) * 1000
# convert packet to bits
L = float(L) * 8
# convert rate to bps
KbPerMb = 1000
bPerKb = 1000
R = float(R) * KbPerMb * bPerKb
delayT = L/R
delayQ = (N-1) * delayT
delayP = d/s

# end to end delay for Nth packet
# add all the delays
delayETE = delayT + delayQ + delayP


print('distance = ', d, ' meters')
print('speed = ', s, ' m/s')
print('L = ', L, ' bits')
print('R = ', R, ' bps')
print('N = ', N)
print('End to end delay for ', N, 'th packet: ', delayETE, ' sec')
print('End to end delay for ', N, 'th packet: ', delayETE*1000, ' ms')
