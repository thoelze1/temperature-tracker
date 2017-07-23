import random, matplotlib.pyplot as plt

class TemperatureFilter:

  # Filter parameters
  Q = 0.0001
  R = 1000.0

  # State representation
  X = 0
  P = 1000 * R

  # Animation parameters
  n = 1000
  tHistory = []
  zHistory = []
  XHistory = []

  # Run filter
  def runFilter(self):
    for k in range(self.n):
      # Measure
      z = self.readTemperature()
      # Predict
      x = self.X
      p = self.P + self.Q
      # Correct
      K = p / (p + self.R)
      self.X = x + K * (z - x)
      self.P = (1 - K) * p
      # Save
      self.tHistory.append(k)
      self.zHistory.append(z)
      self.XHistory.append(self.X)

  # Get noisy measurement
  def readTemperature(self):
    noise = random.random() * 10 - 5
    degrees = 70 + noise
    return degrees

if __name__ == "__main__":
  # New filter
  f = TemperatureFilter()
  # Run the filter
  f.runFilter()
  # Plot the results
  plt.plot(f.tHistory,f.zHistory)
  plt.plot(f.tHistory,f.XHistory)
  plt.show()
