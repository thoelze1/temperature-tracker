import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter:

  n = 100
  readings = []

  trueStart = 70.0
  trueVelocity = 0
  trueAcceleration = 0
  trueOscillationA = 0
  trueOscillationR = 0

  # Get sensor outputs
  def sensorOutputs(self):
    output = []
    for k in range(self.n):
      noise = 5.0*(2*np.random.random()-1)
      temp = (self.trueStart +
              self.trueVelocity*k +
	      self.trueAcceleration*k*k/2 +
	      self.trueOscillationA*np.sin(2*np.pi*self.trueOscillationR*k) +
	      noise)
      output.append(temp)
    return output

  # Run filter based on average
  def movingAverage(self):
    output = []
    interval = 100
    for k in range(self.n):
      output.append(sum(self.readings[k-interval:k])/interval)
    return output

  # Run filter with position based prediction
  def positionFilter(self):
    output = []
    q = 0.0001
    r = 1000.0
    Q = np.matrix(q)
    R = np.matrix(r)
    X = np.matrix(0.0)
    P = np.matrix(1000*r)
    for k in range(self.n):
      # Measure
      z = np.matrix(self.readings[k])
      # Predict
      x = X
      p = P+Q
      # Correct
      K = p*(p+R).I
      X = x+(K*(z-x))
      P = (1-K)*p
      # Save
      output.append(X.item(0, 0))
    return output
  
  # Run filter with velocity based prediction
  def velocityFilter(self):
    output = []
    # Converges well after a long time: q = 0.000001, r = 10000000
    q = 0.000001
    r = 10000000.0
    I = np.matrix(np.identity(2))
    H = np.matrix([[1,0]])
    HT = H.T
    F = np.matrix([[1,1],[0,1]])
    FT = F.T
    Q = np.matrix([[q/3,q/2],[q/2,q/1]])
    R = np.matrix([[r]])
    X = np.matrix([[0.0],[0.0]])
    P = np.matrix([[1000*r,0],[0,1000*r]])
    for k in range(self.n):
      # Measure
      z = np.matrix([[self.readings[k]]])
      # Predict
      x = F*X
      p = F*P*FT+Q
      # Correct
      K = p*HT*(H*p*HT+R).I
      X = x+(K*(z-H*x))
      P = (I-K*H)*p
      # Save
      output.append(X.item(0, 0))
    return output

  # Run filter with acceleration based prediction
  def accelerationFilter(self):
    output = []
    q = 0.000001
    r = 10000000.0
    I = np.matrix(np.identity(3))
    H = np.matrix([[1.,0.,0.]])
    HT = H.T
    F = np.matrix([[1.,1.,1./2.],[0.,1.,1.],[0.,0.,1.]])
    FT = F.T
    Q = np.matrix([[q/20,q/8,q/6],[q/8,q/3,q/2],[q/6,q/2,q/1]])
    R = np.matrix([[r]])
    X = np.matrix([[0.],[0.],[0.]])
    P = np.matrix([[1000*r,0,0],[0,1000*r,0],[0,0,1000*r]])
    for k in range(self.n):
      # Measure
      z = np.matrix([[self.readings[k]]])
      # Predict
      x = F*X
      p = F*P*FT+Q
      # Correct
      K = p*HT*(H*p*HT+R).I
      X = x+(K*(z-H*x))
      P = (I-K*H)*p
      # Save
      output.append(X.item(0, 0))
    return output

  # Plot results
  def plotResults(self):
    self.readings = self.sensorOutputs()
    plt.axis([0, 100, 60, 80])
    plt.plot(range(self.n),self.readings,color='black')
    plt.plot(range(self.n),self.positionFilter(),color='red')
    # plt.plot(range(self.n),self.movingAverage(),color='orange')
    # plt.plot(range(self.n),self.velocityFilter(),color='blue')
    # plt.plot(range(self.n),self.accelerationFilter(),color='yellow')
    plt.show()

if __name__ == "__main__":
  f = KalmanFilter()
  f.plotResults()
