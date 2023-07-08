from typing import Set

# puzzle = "./input_files/example_puzzle.txt"
puzzle = "./input_files/main_puzzle.txt"


class Graph:
    def __init__(self):
        self.nodes = []
        self.relations = {}
        self.relations_reversed = {}
        self.weights = {}
        self.weights_reversed = {}
        self.relations = {}

    @classmethod
    def init_with_nodes(cls, nodes: [str]):  # alternative constructor
        gr = cls()
        for node in nodes:
            gr.add_node(node)
        return gr

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            print(f"{node}: added")
            self.relations[node] = []
            self.relations_reversed[node] = []
        else:
            print(f"{node}: already in the list")

    def add_relation(self, source: str, dest: str, weight: int):
        if source not in self.nodes:
            print(f"{source}: not in nodes")
        elif dest not in self.nodes:
            print(f"{dest}: not in nodes")
        else:
            self.relations[source].append(dest)
            self.weights[(source, dest)] = weight
            self.relations_reversed[dest].append(source)
            self.weights_reversed[(dest, source)] = weight

    def print_graph(self):
        print(f"# of nodes: {len(self.nodes)}")
        print("Relations:")
        for k, v in self.relations.items():
            print(f"[{k}] -> {v}")
        print("Weights:")
        for k, v in self.weights.items():
            print(f"[{k}] -> {v}")

    def print_graph_reversed(self):
        print(f"# of nodes: {len(self.nodes)}")
        print("Relations reversed:")
        for k, v in self.relations_reversed.items():
            print(f"[{k}] -> {v}")
        print("Weights reversed:")
        for k, v in self.weights_reversed.items():
            print(f"[{k}] -> {v}")

    def can_contain(self, target_bag: str) -> int:
        count = -1
        to_be_inspected = [target_bag]
        inspected = []

        while len(to_be_inspected) > 0:
            current_bag = to_be_inspected.pop(0)
            if current_bag not in inspected:
                count += 1
                inspected.append(current_bag)
            else:
                continue

            if len(self.relations_reversed[current_bag]) > 0:
                to_be_inspected.extend(self.relations_reversed[current_bag])
        return count




def process_line(raw_line: str):
    line = raw_line.split(" bags contain ")
    source = line[0]
    raw_dest = line[1].split(", ")
    nodes = [source]
    destination = []
    weights = {}
    if raw_dest[0].isalpha():
        pass
    else:
        for dest in raw_dest:
            temp = dest.split()
            if temp[0] == "no":
                pass
            else:
                temp_dest = " ".join(temp[1:3])
                destination.append(temp_dest)
                nodes.append(temp_dest)
                weights[(source, temp_dest)] = int(temp[0])
    return {"all_nodes": nodes,
            "source": source,
            "destination": destination,
            "weights": weights}


if __name__ == "__main__":
    graph = Graph()

    with open(puzzle, "r") as file:
        for line in file:
            print(line.replace("\n", ""))
            temp_dict = process_line(line)

            for node in temp_dict["all_nodes"]:
                graph.add_node(node)
            for dest in temp_dict["destination"]:
                source = temp_dict["source"]
                graph.add_relation(source, dest, temp_dict["weights"][(source, dest)])
    graph.print_graph()
    graph.print_graph_reversed()
    result1 = graph.can_contain("shiny gold")

    print(f"Part 1 solution: {result1}")
