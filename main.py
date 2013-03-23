import datahandler as dh
import nethandler as nh
from matplotlib import pyplot as pp

#Input Data
TRAINING = 2200
TESTING = 614
startdate = '20020101'  # YYYYMMDD

#Neural Network
INPUT = 1
HIDDEN = 20
OUTPUT = 1

#Training
ITERATIONS = 10
LRATE = 0.5
MOMENTUM = 0.2


#S&P 500
sp500 = dh.DataHandler()
sp500.load_index("%5EGSPC", startdate)

sp_net = nh.NetHandler(INPUT, HIDDEN, OUTPUT)
sp_net.create_training_data(sp500, TRAINING)
# train_errors, val_errors = sp_net.train(LRATE, MOMENTUM, ITERATIONS)
sp_net.train(LRATE, MOMENTUM, ITERATIONS)

out_ser = sp_net.get_output(TRAINING, TESTING)

print sp_net.change_tomorrow()

correct = 0
for i in xrange(1, len(out_ser)):
    actual = sp500.data.ix[out_ser.index, 0][i]
    predicted = out_ser[i]
    if (actual > 0 and predicted > 0) or (actual < 0 and predicted < 0):
        correct += 1
print "%.2f" % (float(correct) / float(len(out_ser) - 1) * 100.0),"% Accuracy"

pp.figure(0)
sp500.data.ix[:, 0].plot(style='b-')
out_ser.plot(style='r-')
pp.show()

# pp.figure(1)
# pp.plot(train_errors)
# pp.plot(val_errors)
# pp.show(1)



#NASDAQ COMPOSITE INDEX
#nasdaq = dh.DataHandler()
#nasdaq.load_index("%5EIXIC", startdate)

#MAJOR MARKET INDEX
#tot = dh.DataHandler()
#tot.load_index("%5EXMI", startdate)

#NYSE COMPOSITE INDEX
#nyse = dh.DataHandler()
#nyse.load_index("%5ENYA", startdate)