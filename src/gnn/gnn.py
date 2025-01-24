import torch
import torch.nn.functional as F
from torch_geometric.nn import NNConv, global_mean_pool
from torch_geometric.data import Data

class GCNWithEdgeFeatures(torch.nn.Module):
    def __init__(self):
        super(GCNWithEdgeFeatures, self).__init__()
        # Definindo o tamanho de entrada para as features de vértice e aresta
        node_in_channels = 2  # Grau e proximidade de troca de cores
        edge_in_channels = 2  # Cor da aresta e progresso da decomposição
        hidden_channels = 32  # Número de canais intermediários
        
        self.edge_mlp1 = torch.nn.Linear(edge_in_channels, node_in_channels * hidden_channels)
        
        # Definindo as camadas de convolução com NNConv
        self.conv1 = NNConv(node_in_channels, hidden_channels, nn=self.edge_mlp1)
        self.conv2 = NNConv(hidden_channels, 64, nn=torch.nn.Linear(edge_in_channels, hidden_channels*64))


    def forward(self, data: Data):
        x, edge_index, edge_attr, batch = data.x, data.edge_index, data.edge_attr, data.batch
        
        # Camada convolucional 1
        x = self.conv1(x, edge_index, edge_attr)
        x = F.relu(x)
        # Camada convolucional 2
        x = self.conv2(x, edge_index, edge_attr)
        # Aplicar pooling global para agregar as informações
        batch = torch.zeros(len(x), dtype=torch.long)
        x = global_mean_pool(x, batch)  # Pode usar também global_max_pool para outra estratégia de agregação
        return x
