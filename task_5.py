import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def build_heap_tree(array):
    if not array:
        return None
    nodes = [Node(val) for val in array]
    for i in range(len(nodes)):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


def get_color(step, total):
    t = step / (total - 1) if total > 1 else 1
    r = int(0 + t * (212 - 0))
    g = int(31 + t * (230 - 31))
    b = int(91 + t * (241 - 91))
    return f"#{r:02x}{g:02x}{b:02x}"


def draw_tree(root, title):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def dfs(root):
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited


def bfs(root):
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited


def colorize_and_draw(root, traversal_fn, title):
    nodes = traversal_fn(root)
    total = len(nodes)
    for step, node in enumerate(nodes):
        node.color = get_color(step, total)
    draw_tree(root, title)


if __name__ == "__main__":
    data = [0, 4, 1, 5, 10, 3]
    heapq.heapify(data)

    root = build_heap_tree(data)
    colorize_and_draw(root, dfs, "DFS - обхід у глибину")

    root = build_heap_tree(data)
    colorize_and_draw(root, bfs, "BFS - обхід у ширину")
