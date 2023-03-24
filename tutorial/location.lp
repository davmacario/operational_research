\ Model set_covering
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  X[0] + X[1] + X[2] + X[3]
Subject To
 covering_node_[0]: X[0] + X[1] + X[2] + X[3] >= 1
 covering_node_[1]: X[1] + X[2] >= 1
 covering_node_[2]: X[2] + X[3] >= 1
 covering_node_[3]: X[1] + X[3] >= 1
Bounds
Binaries
 X[0] X[1] X[2] X[3]
End
