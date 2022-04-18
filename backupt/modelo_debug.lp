\ Model 5-path decomposition
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
 
Subject To
 each_color_has_maximum_degree_at_most_2: x[0,1,0] + x[0,3,0] + x[0,7,0]
   + x[0,8,0] + x[0,9,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,1] + x[0,3,1] + x[0,7,1]
   + x[0,8,1] + x[0,9,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,2] + x[0,3,2] + x[0,7,2]
   + x[0,8,2] + x[0,9,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,3] + x[0,3,3] + x[0,7,3]
   + x[0,8,3] + x[0,9,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,4] + x[0,3,4] + x[0,7,4]
   + x[0,8,4] + x[0,9,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,0] + x[1,5,0] + x[1,6,0]
   + x[1,8,0] + x[1,9,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,1] + x[1,5,1] + x[1,6,1]
   + x[1,8,1] + x[1,9,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,2] + x[1,5,2] + x[1,6,2]
   + x[1,8,2] + x[1,9,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,3] + x[1,5,3] + x[1,6,3]
   + x[1,8,3] + x[1,9,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,1,4] + x[1,5,4] + x[1,6,4]
   + x[1,8,4] + x[1,9,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,3,0] + x[2,4,0] + x[2,5,0]
   + x[2,7,0] + x[2,9,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,3,1] + x[2,4,1] + x[2,5,1]
   + x[2,7,1] + x[2,9,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,3,2] + x[2,4,2] + x[2,5,2]
   + x[2,7,2] + x[2,9,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,3,3] + x[2,4,3] + x[2,5,3]
   + x[2,7,3] + x[2,9,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,3,4] + x[2,4,4] + x[2,5,4]
   + x[2,7,4] + x[2,9,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,3,0] + x[2,3,0] + x[3,4,0]
   + x[3,6,0] + x[3,9,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,3,1] + x[2,3,1] + x[3,4,1]
   + x[3,6,1] + x[3,9,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,3,2] + x[2,3,2] + x[3,4,2]
   + x[3,6,2] + x[3,9,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,3,3] + x[2,3,3] + x[3,4,3]
   + x[3,6,3] + x[3,9,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,3,4] + x[2,3,4] + x[3,4,4]
   + x[3,6,4] + x[3,9,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,4,0] + x[3,4,0] + x[4,5,0]
   + x[4,7,0] + x[4,8,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,4,1] + x[3,4,1] + x[4,5,1]
   + x[4,7,1] + x[4,8,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,4,2] + x[3,4,2] + x[4,5,2]
   + x[4,7,2] + x[4,8,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,4,3] + x[3,4,3] + x[4,5,3]
   + x[4,7,3] + x[4,8,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[2,4,4] + x[3,4,4] + x[4,5,4]
   + x[4,7,4] + x[4,8,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,5,0] + x[2,5,0] + x[4,5,0]
   + x[5,7,0] + x[5,8,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,5,1] + x[2,5,1] + x[4,5,1]
   + x[5,7,1] + x[5,8,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,5,2] + x[2,5,2] + x[4,5,2]
   + x[5,7,2] + x[5,8,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,5,3] + x[2,5,3] + x[4,5,3]
   + x[5,7,3] + x[5,8,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,5,4] + x[2,5,4] + x[4,5,4]
   + x[5,7,4] + x[5,8,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,6,0] + x[3,6,0] + x[6,7,0]
   + x[6,8,0] + x[6,9,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,6,1] + x[3,6,1] + x[6,7,1]
   + x[6,8,1] + x[6,9,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,6,2] + x[3,6,2] + x[6,7,2]
   + x[6,8,2] + x[6,9,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,6,3] + x[3,6,3] + x[6,7,3]
   + x[6,8,3] + x[6,9,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[1,6,4] + x[3,6,4] + x[6,7,4]
   + x[6,8,4] + x[6,9,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,7,0] + x[2,7,0] + x[4,7,0]
   + x[5,7,0] + x[6,7,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,7,1] + x[2,7,1] + x[4,7,1]
   + x[5,7,1] + x[6,7,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,7,2] + x[2,7,2] + x[4,7,2]
   + x[5,7,2] + x[6,7,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,7,3] + x[2,7,3] + x[4,7,3]
   + x[5,7,3] + x[6,7,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,7,4] + x[2,7,4] + x[4,7,4]
   + x[5,7,4] + x[6,7,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,8,0] + x[1,8,0] + x[4,8,0]
   + x[5,8,0] + x[6,8,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,8,1] + x[1,8,1] + x[4,8,1]
   + x[5,8,1] + x[6,8,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,8,2] + x[1,8,2] + x[4,8,2]
   + x[5,8,2] + x[6,8,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,8,3] + x[1,8,3] + x[4,8,3]
   + x[5,8,3] + x[6,8,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,8,4] + x[1,8,4] + x[4,8,4]
   + x[5,8,4] + x[6,8,4] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,9,0] + x[1,9,0] + x[2,9,0]
   + x[3,9,0] + x[6,9,0] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,9,1] + x[1,9,1] + x[2,9,1]
   + x[3,9,1] + x[6,9,1] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,9,2] + x[1,9,2] + x[2,9,2]
   + x[3,9,2] + x[6,9,2] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,9,3] + x[1,9,3] + x[2,9,3]
   + x[3,9,3] + x[6,9,3] <= 2
 each_color_has_maximum_degree_at_most_2: x[0,9,4] + x[1,9,4] + x[2,9,4]
   + x[3,9,4] + x[6,9,4] <= 2
 each_color_has_five_edges: x[0,1,0] + x[0,3,0] + x[0,7,0] + x[0,8,0]
   + x[0,9,0] + x[1,5,0] + x[1,6,0] + x[1,8,0] + x[1,9,0] + x[2,3,0]
   + x[2,4,0] + x[2,5,0] + x[2,7,0] + x[2,9,0] + x[3,4,0] + x[3,6,0]
   + x[3,9,0] + x[4,5,0] + x[4,7,0] + x[4,8,0] + x[5,7,0] + x[5,8,0]
   + x[6,7,0] + x[6,8,0] + x[6,9,0] = 5
 each_color_has_five_edges: x[0,1,1] + x[0,3,1] + x[0,7,1] + x[0,8,1]
   + x[0,9,1] + x[1,5,1] + x[1,6,1] + x[1,8,1] + x[1,9,1] + x[2,3,1]
   + x[2,4,1] + x[2,5,1] + x[2,7,1] + x[2,9,1] + x[3,4,1] + x[3,6,1]
   + x[3,9,1] + x[4,5,1] + x[4,7,1] + x[4,8,1] + x[5,7,1] + x[5,8,1]
   + x[6,7,1] + x[6,8,1] + x[6,9,1] = 5
 each_color_has_five_edges: x[0,1,2] + x[0,3,2] + x[0,7,2] + x[0,8,2]
   + x[0,9,2] + x[1,5,2] + x[1,6,2] + x[1,8,2] + x[1,9,2] + x[2,3,2]
   + x[2,4,2] + x[2,5,2] + x[2,7,2] + x[2,9,2] + x[3,4,2] + x[3,6,2]
   + x[3,9,2] + x[4,5,2] + x[4,7,2] + x[4,8,2] + x[5,7,2] + x[5,8,2]
   + x[6,7,2] + x[6,8,2] + x[6,9,2] = 5
 each_color_has_five_edges: x[0,1,3] + x[0,3,3] + x[0,7,3] + x[0,8,3]
   + x[0,9,3] + x[1,5,3] + x[1,6,3] + x[1,8,3] + x[1,9,3] + x[2,3,3]
   + x[2,4,3] + x[2,5,3] + x[2,7,3] + x[2,9,3] + x[3,4,3] + x[3,6,3]
   + x[3,9,3] + x[4,5,3] + x[4,7,3] + x[4,8,3] + x[5,7,3] + x[5,8,3]
   + x[6,7,3] + x[6,8,3] + x[6,9,3] = 5
 each_color_has_five_edges: x[0,1,4] + x[0,3,4] + x[0,7,4] + x[0,8,4]
   + x[0,9,4] + x[1,5,4] + x[1,6,4] + x[1,8,4] + x[1,9,4] + x[2,3,4]
   + x[2,4,4] + x[2,5,4] + x[2,7,4] + x[2,9,4] + x[3,4,4] + x[3,6,4]
   + x[3,9,4] + x[4,5,4] + x[4,7,4] + x[4,8,4] + x[5,7,4] + x[5,8,4]
   + x[6,7,4] + x[6,8,4] + x[6,9,4] = 5
 each_edge_has_one_color: x[0,1,0] + x[0,1,1] + x[0,1,2] + x[0,1,3]
   + x[0,1,4] = 1
 each_edge_has_one_color: x[0,3,0] + x[0,3,1] + x[0,3,2] + x[0,3,3]
   + x[0,3,4] = 1
 each_edge_has_one_color: x[0,7,0] + x[0,7,1] + x[0,7,2] + x[0,7,3]
   + x[0,7,4] = 1
 each_edge_has_one_color: x[0,8,0] + x[0,8,1] + x[0,8,2] + x[0,8,3]
   + x[0,8,4] = 1
 each_edge_has_one_color: x[0,9,0] + x[0,9,1] + x[0,9,2] + x[0,9,3]
   + x[0,9,4] = 1
 each_edge_has_one_color: x[1,5,0] + x[1,5,1] + x[1,5,2] + x[1,5,3]
   + x[1,5,4] = 1
 each_edge_has_one_color: x[1,6,0] + x[1,6,1] + x[1,6,2] + x[1,6,3]
   + x[1,6,4] = 1
 each_edge_has_one_color: x[1,8,0] + x[1,8,1] + x[1,8,2] + x[1,8,3]
   + x[1,8,4] = 1
 each_edge_has_one_color: x[1,9,0] + x[1,9,1] + x[1,9,2] + x[1,9,3]
   + x[1,9,4] = 1
 each_edge_has_one_color: x[2,3,0] + x[2,3,1] + x[2,3,2] + x[2,3,3]
   + x[2,3,4] = 1
 each_edge_has_one_color: x[2,4,0] + x[2,4,1] + x[2,4,2] + x[2,4,3]
   + x[2,4,4] = 1
 each_edge_has_one_color: x[2,5,0] + x[2,5,1] + x[2,5,2] + x[2,5,3]
   + x[2,5,4] = 1
 each_edge_has_one_color: x[2,7,0] + x[2,7,1] + x[2,7,2] + x[2,7,3]
   + x[2,7,4] = 1
 each_edge_has_one_color: x[2,9,0] + x[2,9,1] + x[2,9,2] + x[2,9,3]
   + x[2,9,4] = 1
 each_edge_has_one_color: x[3,4,0] + x[3,4,1] + x[3,4,2] + x[3,4,3]
   + x[3,4,4] = 1
 each_edge_has_one_color: x[3,6,0] + x[3,6,1] + x[3,6,2] + x[3,6,3]
   + x[3,6,4] = 1
 each_edge_has_one_color: x[3,9,0] + x[3,9,1] + x[3,9,2] + x[3,9,3]
   + x[3,9,4] = 1
 each_edge_has_one_color: x[4,5,0] + x[4,5,1] + x[4,5,2] + x[4,5,3]
   + x[4,5,4] = 1
 each_edge_has_one_color: x[4,7,0] + x[4,7,1] + x[4,7,2] + x[4,7,3]
   + x[4,7,4] = 1
 each_edge_has_one_color: x[4,8,0] + x[4,8,1] + x[4,8,2] + x[4,8,3]
   + x[4,8,4] = 1
 each_edge_has_one_color: x[5,7,0] + x[5,7,1] + x[5,7,2] + x[5,7,3]
   + x[5,7,4] = 1
 each_edge_has_one_color: x[5,8,0] + x[5,8,1] + x[5,8,2] + x[5,8,3]
   + x[5,8,4] = 1
 each_edge_has_one_color: x[6,7,0] + x[6,7,1] + x[6,7,2] + x[6,7,3]
   + x[6,7,4] = 1
 each_edge_has_one_color: x[6,8,0] + x[6,8,1] + x[6,8,2] + x[6,8,3]
   + x[6,8,4] = 1
 each_edge_has_one_color: x[6,9,0] + x[6,9,1] + x[6,9,2] + x[6,9,3]
   + x[6,9,4] = 1
Bounds
Binaries
 x[0,1,0] x[0,1,1] x[0,1,2] x[0,1,3] x[0,1,4] x[0,3,0] x[0,3,1] x[0,3,2]
 x[0,3,3] x[0,3,4] x[0,7,0] x[0,7,1] x[0,7,2] x[0,7,3] x[0,7,4] x[0,8,0]
 x[0,8,1] x[0,8,2] x[0,8,3] x[0,8,4] x[0,9,0] x[0,9,1] x[0,9,2] x[0,9,3]
 x[0,9,4] x[1,5,0] x[1,5,1] x[1,5,2] x[1,5,3] x[1,5,4] x[1,6,0] x[1,6,1]
 x[1,6,2] x[1,6,3] x[1,6,4] x[1,8,0] x[1,8,1] x[1,8,2] x[1,8,3] x[1,8,4]
 x[1,9,0] x[1,9,1] x[1,9,2] x[1,9,3] x[1,9,4] x[2,3,0] x[2,3,1] x[2,3,2]
 x[2,3,3] x[2,3,4] x[2,4,0] x[2,4,1] x[2,4,2] x[2,4,3] x[2,4,4] x[2,5,0]
 x[2,5,1] x[2,5,2] x[2,5,3] x[2,5,4] x[2,7,0] x[2,7,1] x[2,7,2] x[2,7,3]
 x[2,7,4] x[2,9,0] x[2,9,1] x[2,9,2] x[2,9,3] x[2,9,4] x[3,4,0] x[3,4,1]
 x[3,4,2] x[3,4,3] x[3,4,4] x[3,6,0] x[3,6,1] x[3,6,2] x[3,6,3] x[3,6,4]
 x[3,9,0] x[3,9,1] x[3,9,2] x[3,9,3] x[3,9,4] x[4,5,0] x[4,5,1] x[4,5,2]
 x[4,5,3] x[4,5,4] x[4,7,0] x[4,7,1] x[4,7,2] x[4,7,3] x[4,7,4] x[4,8,0]
 x[4,8,1] x[4,8,2] x[4,8,3] x[4,8,4] x[5,7,0] x[5,7,1] x[5,7,2] x[5,7,3]
 x[5,7,4] x[5,8,0] x[5,8,1] x[5,8,2] x[5,8,3] x[5,8,4] x[6,7,0] x[6,7,1]
 x[6,7,2] x[6,7,3] x[6,7,4] x[6,8,0] x[6,8,1] x[6,8,2] x[6,8,3] x[6,8,4]
 x[6,9,0] x[6,9,1] x[6,9,2] x[6,9,3] x[6,9,4]
End
