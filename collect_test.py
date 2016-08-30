query = []
nodes = {}
for row in query:
    if row.node_id not in nodes:
        nodes[row.node_id] = []
    nodes[row.node_id].append({key: getattr(query, key) for key in ('node_name', 'type', 'name')})
