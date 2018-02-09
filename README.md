# ModularityMaximization
# Language: Python
# Input: prefix (for network and cluster CSV files)
# Output: none (screen only)
# Dependency: ClusterizePlugin (Available at: https://github.com/movingpictures83/Clusterize)
# Tested with: PluMA 1.0, Python 2.7

PluMA plugin that runs Modularity Maximization (Newman, 2006) for community detection.
Modularity Maximization requires both a weighted network and a set of clusters to run,
and therefore accepts input in the form of a prefix for both files, each of which should
be in CSV format.  It will assume the filenames are prefix.csv (network) and prefix.clusters.csv (clusters).
The network file should contain rows and columns representing nodes with entry (i, j) corresponding
to the weight of the edge from node i to node j.  The clusters file should be in the following format:

"","x"
"1","Family.Lachnospiraceae.0001"
"2","Family.Ruminococcaceae.0003"
"3","Family.Lachnospiraceae.0029"
"4","Family.Lachnospiraceae.0043"
"5","Family.Ruminococcaceae.0019"
"6","Family.Lachnospiraceae.0095"
"","x"
"1","Family.Porphyromonadaceae.0005"
"2","Family.Porphyromonadaceae.0006"
"3","Family.Lachnospiraceae.0045"
"4","Order.Clostridiales.0007"
"","x"
"1","Kingdom.Bacteria.0001"
"2","Family.Porphyromonadaceae.0013"
"3","Phylum.Firmicutes.0004"

Note the line "","x" denotes a new cluster.

All output produced by this plugin gets generated to the screen, since Modularity Maximization
is ultimately a measure of community detection.  The plugin will generate a few statistics relevant
to the algorithm, followed by an estimate as to whether or not the community structure is reliable based on the algorithm.  

