RTT = float(input('what is the beginning est RTT (ms)? '))
totalRTTs = int(input('how many RTTs were recorded? '))
rttArr = []
for i in range(totalRTTs):
    curRTT = float(input('what is the RTT for trip %d (ms)?' % (i)))
    rttArr.append(curRTT)

# calc weighted moving average
# estRTT = (1 - weight) * prevEstRTT + weight * curRTT
# eRTT from lecture:
#   EstimatedRTT_n = (1-α)EstimatedRTT_(n-1) + (α)SampleRTT_new
weight = 0.4
prevRTT = RTT
# print all est RTTs, val = measured RTT
for val in rttArr:
    eRTT = (1-weight) * prevRTT + (weight * val)
    prevRTT = eRTT
    print('eRTT: ', eRTT)
