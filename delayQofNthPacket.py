N = int(input('find delay of which packet? '))
L = input('packet size (Bytes): ')
R = input('rate of transmission (Mbps): ')

# convert packet to bits
L = int(L)*8
# convert rate to bps
KbPerMb = 1000
bPerKb = 1000
R = int(R)*KbPerMb*bPerKb
delayQ = (N-1)*(L/R)

print("queueing delay of ", N, 'th packet: ', delayQ, ' sec')
print("queueing delay of ", N, 'th packet: ', delayQ*1000, ' ms')
