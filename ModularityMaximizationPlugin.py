import sys
import math
#import numpy
from Clusterize.ClusterizePlugin import *

# Note: This does NOT take into account edge weights
class ModularityMaximizationPlugin(ClusterizePlugin):
   def input(self, filename):
      ClusterizePlugin.input(self, filename)

   def output(self, filename):
      nodepairs = (self.n*(self.n-1)) / 2
      q = 0
      for i in range(len(self.clusters)):
         if (len(self.clusters[i]) > 1):  # Do not count a singleton
            q += 1
      same = 0.0
      diff = 0.0
      for i in range(self.n):
         for j in range(i+1, self.n):
            # TMC small modification here to work with signs
            # Positive edges *should* be between nodes in the same cluster
            # Negative edges *should* be between nodes in different clusters
            # For negatives, simply flipped the check but added one to same and diff
            if (self.ADJ[i][j] > 0):
               if (inSameCluster(self.bacteria[i], self.bacteria[j], self.clusters)):
                  same += 1
               else:
                  diff += 1
            elif (self.ADJ[i][j] < 0):
               if (inSameCluster(self.bacteria[i], self.bacteria[j], self.clusters)):
                  diff += 1
               else:
                  same += 1
      
      # Note assuming no output file, just text
      pin = same / nodepairs
      pout = diff / nodepairs
      cin = self.n*pin
      cout = self.n*pout
      difference = cin - cout
      threshold = math.sqrt(q*(cin + (q-1)*cout))
      print "Number of Clusters: ", q
      print "Threshold: ", threshold
      print "Cin: ", cin
      print "Cout: ", cout
      print "Difference: ", difference
      if (difference > threshold):
         print "Community structure is reliable"
      else:
         print "Community structure is unreliable"



