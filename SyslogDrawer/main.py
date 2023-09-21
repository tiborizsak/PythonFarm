import re
import networkx as nx
import matplotlib.pyplot as plt


def parse_syslog_ng_conf(file_path):
    sources = set()
    destinations = set()
    log_links = []

    with open(file_path, 'r') as f:
        lines = f.readlines()

    current_log_block = []
    for line in lines:
        line = line.strip()
        if line.startswith('log {'):
            current_log_block = []
        elif line.endswith('};'):
            log_links.append(current_log_block)
            current_log_block = []
        else:
            match_source = re.search(r'source\((\w+)\)', line)
            match_dest = re.search(r'destination\((\w+)\)', line)

            if match_source:
                sources.add(match_source.group(1))
                current_log_block.append(('source', match_source.group(1)))

            if match_dest:
                destinations.add(match_dest.group(1))
                current_log_block.append(('destination', match_dest.group(1)))

    return sources, destinations, log_links


def plot_graph(sources, destinations, log_links):
    plt.figure(figsize=(12, 12), dpi=300)
    G = nx.DiGraph()

    for src in sources:
        G.add_node(src, color='blue')

    for dst in destinations:
        G.add_node(dst, color='green')

    for log_block in log_links:
        src_nodes = [node[1] for node in log_block if node[0] == 'source']
        dst_nodes = [node[1] for node in log_block if node[0] == 'destination']

        for src in src_nodes:
            for dst in dst_nodes:
                G.add_edge(src, dst)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=[G.nodes[node]['color'] for node in G])
    #plt.show()
    plt.savefig("graph.png")

if __name__ == "__main__":
    file_path = 'syslog-ng.conf'  # Replace with the path to your syslog-ng.conf file
    sources, destinations, log_links = parse_syslog_ng_conf(file_path)
    plot_graph(sources, destinations, log_links)
