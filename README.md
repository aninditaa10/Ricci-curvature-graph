
# **Forman Ricci Curvature for a graph**

## **Overview**
The project computes the **Forman Ricci curvature** for a directed, weighted graph using **NetworkX** and the **GraphRicciCurvature** library. The graph is visualized with curvature values annotated on the edges.

## **Libraries Used**
To run this code, ensure you have the following libraries installed:  
- [`networkx`](https://networkx.org/) – Graph creation and manipulation.  
- [`GraphRicciCurvature`](https://pypi.org/project/GraphRicciCurvature/) – Computes Forman Ricci curvature for graph edges. The formula used in this case is for directed weighted graph.
- [`matplotlib`](https://matplotlib.org/) – Visualizing the graph with curvature annotations.  

## **Output Graph Structure**
- **Nodes:** Represent different points in the network.  
- **Edges:** Directed and weighted connections between nodes.  
- **Curvature Calculation:** Forman Ricci curvature is computed based on the connectivity of each edge, with higher values indicating tight connections and negative values indicating potential bottlenecks.  

## **How to Run**
1. **Install Dependencies**  
   ```bash
   pip install networkx GraphRicciCurvature matplotlib
   ```
2. **Run the Script**  
   ```bash
   python Forman_Ricci_Curvature_graph.py
   ```
3. **View the Output**  
   - The python code generates and displays a graph, where each edge is labeled with its computed curvature.  


## **Output**
 
![Ricci_Curvature_graph](https://github.com/user-attachments/assets/240f2ca1-261d-45d5-82f5-d99d2c7ff753)

---
