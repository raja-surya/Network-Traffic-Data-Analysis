
def host_packet_proto_info(df, sourceip):
    
        print("\nProtocol-wise break-up of packets sent from this host :\n")
    
        a=df[df.isrc==sourceip].tsport.value_counts().sum()
        print(sourceip + " TCP Packets: " + str(a))
        b=df[df.isrc==sourceip].utsport.value_counts().sum()
        print(sourceip + " UDP Packets: " + str(b))
        c=df[df.isrc==sourceip].icmpcode.value_counts().sum()
        print(sourceip + " ICMP Packets: " + str(c))
        d=df[df.isrc==sourceip].arpsrc.value_counts().sum()
        print(sourceip + " ARP Packets: " + str(d))
        print()
        e=df[df.isrc==sourceip].dnsopcode.value_counts().sum()
        print(sourceip + " DNS Packets: " + str(e))
        f=df[df.isrc==sourceip].bootpop.value_counts().sum()
        print(sourceip + " BOOTP Packets: " + str(f))

       # g=df[df.isrc==sourceip].snmpcommunity.value_counts().sum()
       # print(sourceip + " SNMP Packets: " + str(g))
        
        
    
    # Function to print the destination ip adresses which any given source host talks to

def top_dests_italk_to(df, me, head=10):
        #print("I talk to:")
        print("\nTop Destinations this host talked to:\n")
        print(df[df.isrc==me].groupby(['isrc','idst'])\
                .size().sort_values(ascending=False).head(head))
    
    
    
def host_profile(df, sourceip):
        print("Profile of Host "+ sourceip + " : \n")
    
        print("Total Number of Packets Sent : " + str(len(df[df.isrc==sourceip])) +"\n")
    
        dests=df[df.isrc==sourceip].idst.value_counts().count()
        print(sourceip + " Destinations: " + str(dests))
    
        tsrcs=df[df.isrc==sourceip].tsport.value_counts().count()
        print(sourceip + " TCP Port Sources: " + str(tsrcs))
    
        tdests=df[df.isrc==sourceip].tdport.value_counts().count()
        print(sourceip + " TCP Port Destinations: " + str(tdests))
    
        usrcs=df[df.isrc==sourceip].utsport.value_counts().count()
        print(sourceip + " UDP Port Sources: " + str(usrcs))
    
        udests=df[df.isrc==sourceip].utdport.value_counts().count()
        print(sourceip + " UDP Port Destinations: " + str(udests))

        print()
        host_packet_proto_info(df, sourceip)
        print()
        top_dests_italk_to(df, sourceip)
        
        
    
    
def port_info(df, sourceip, dstip=''):
    
        print("\nPort wise breakup of packets :")
    
        if not dstip: 
            print()
            print(sourceip + " TOP TCP Source Ports -----------------\n")
            print(df[df.isrc==sourceip].tsport.value_counts())
            print()
            print(sourceip + " TOP TCP Destination Ports -----------------\n")
            print(df[df.isrc==sourceip].tdport.value_counts())
            print()
            print(sourceip + " TOP UDP Source Ports -----------------\n")
            print(df[df.isrc==sourceip].utsport.value_counts())
            print()
            print(sourceip + " TOP UDP Destination Ports -----------------\n")
            print(df[df.isrc==sourceip].utdport.value_counts())
        
        else:
            print()
            print(sourceip + " to " + dstip + " TOP TCP Source Ports -----------------\n")
            print(df.loc[(df.isrc==sourceip) & (df.idst==dstip)].tsport.value_counts())
            print()
            print(sourceip + " to " + dstip + " TOP TCP Destination Ports -----------------\n")
            print(df.loc[(df.isrc==sourceip) & (df.idst==dstip)].tdport.value_counts())
            print()
            print(sourceip + " to " + dstip + " TOP UDP Source Ports -----------------\n")
            print(df.loc[(df.isrc==sourceip) & (df.idst==dstip)].utsport.value_counts())
            print()
            print(sourceip + " to " + dstip + " TOP UDP Destination Ports -----------------\n")
            print(df.loc[(df.isrc==sourceip) & (df.idst==dstip)].utdport.value_counts())   
            
            
            