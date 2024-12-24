initials, edges = open("day24/day24_input.txt").read().strip().split("\n\n")

class Node:
    def __init__(self, key):
        self.value = None
        self.key = key

        self.edges = []

        self.inbound = None

    def add_edge(self, coorigin, destination, operator):
        self.edges.append((coorigin, destination, operator))

    def do_op(self, other, op):
        OPS = {
            "AND": lambda x, y : x.value & y.value,
            "OR": lambda x, y : x.value | y.value,
            "XOR": lambda x, y : x.value ^ y.value 
        }

        return OPS[op](self, other)

    def set_value(self, value):
        self.value = value

        for coorigin, destination, operator in self.edges:
            if destination.value is not None or coorigin.value is None:
                continue

            destination.set_value(self.do_op(coorigin, operator))

    def has_in_type(self, op):
        return self.inbound is not None and self.inbound[2] == op
    
    def out_with_type_and_operand_or_default(self, operand, operator):
        for coorigin, destination, op in self.edges:
            if operand == coorigin and operator == op:
                return destination
            
        return None

    def get_expression(self):
        if self.inbound is None:
            return self.key
        
        f0, f1, o = self.inbound

        return f"({f0.get_expression()} {o} {f1.get_expression()})" 

    def identify_and_validate(self, expected_carry_in):
        print("\nRunning identify_and_validate on", self.key)
        f0, f1, o = self.inbound
        print("Inbound operator is", o)
        if o != 'XOR':
            print("ERROR")
            return
        
        # Try to find operands
        bitid = self.key[1:]
        opkeys = ["x"+bitid, "y"+bitid]
        found = False

        if f0.has_in_type("XOR"):
            a, b, _ = f0.inbound

            if sorted([a.key, b.key]) == opkeys:
                print("Found operands, xoring at", f0.key)
                opxor = f0
                carryin = f1
                found = True
                print("Carry in is provided by", f1.key)

        if not found and f1.has_in_type("XOR"):
            a, b, _ = f1.inbound

            if sorted([a.key, b.key]) == opkeys:
                print("Found operands, xoring at", f1.key)
                found = True
                opxor = f1
                carryin = f0
                print("Carry in is provided by", f0.key)

        if not found:
            print("ERROR")
            print("Failed to find operands", *opkeys, "assuming a normal full-adder")
            return
        
        if carryin != expected_carry_in:
            print("Expected carry in", expected_carry_in.key, "does not match!\nERROR")
            return
        
        # Find carryout
        # Inputs
        carry_temp_0 = opxor.out_with_type_and_operand_or_default(carryin, "AND")

        if carry_temp_0 is None:
            print("Carry temp 0 is none\nERROR")
            return
        
        print("Found carry temp 0", carry_temp_0.key)
        
        carry_temp_1 = a.out_with_type_and_operand_or_default(b, "AND")

        if carry_temp_1 is None:
            print("Carry temp 1 is none\nERROR")
            return
        
        print("Found carry temp 1", carry_temp_1.key)

        # Final step: or

        carryout = carry_temp_0.out_with_type_and_operand_or_default(carry_temp_1, "OR")

        if carryout is None:
            print("Carry out is none!\nERROR")
            return
        
        print("Found carry out", carryout.key)

        return carryout
        

        

nodes = {}

def get_or_make_node(key):
    if key in nodes:
        return nodes[key]
    
    nodes[key] = Node(key)

    return nodes[key]


for el in edges.split("\n"):
    f0, o, f1, _, d = el.split()
    
    f0 = get_or_make_node(f0)
    f1 = get_or_make_node(f1)
    d = get_or_make_node(d)

    f0.add_edge(f1, d, o)
    f1.add_edge(f0, d, o)
    d.inbound = (f0, f1, o) 

next_carry_out = nodes['x00'].out_with_type_and_operand_or_default(nodes["y00"], "AND")

for k in sorted(nodes.keys()):
    if k[0] != 'z' or k == "z00":
        continue

    # print(nodes[k].get_expression())

    next_carry_out = nodes[k].identify_and_validate(next_carry_out)

    if next_carry_out is None:
        print("next_carry_out is None")
        break
    print()

