# Network-Traffic-Data-Analysis

EDA and Unsupervised K-means Clustering on Network Traffic Data of more than 6 Million Packets.
 - Exract network traffic packet data from pcap file of millions of packets using Scapy tool and convert the same to Pandas Data Frame.
 - Using SME knowledge in networking, find insights about different types of hosts in the network - Servers, Clients, Bad hosts targeting servers in the network etc.
 - Apply ML PCA and Clustering technique to group and find interesting patterns of hundreds of hosts in the network.
 
Data Source : 
The packet data analysed here is taken from https://www.netresec.com/?page=MACCDC
File : maccdc2012_00000.pcap.gz
 
Run the notebooks in the following order: 
 1. PCAP_Network_Traffic-Data_Extraction.ipynb
 2. Network_Traffic-Data_Analysis-1.ipynb
 3. Network_Traffic-Data_Analysis-2.ipynb
 
Thanks to "Data Analytics For IT Networks" book by John Garret which guided me in this exercise.  

 
