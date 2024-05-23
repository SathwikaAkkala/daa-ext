import heapq

# Define a class for the nodes in the Huffman Tree
class Node:
    def __init__(self, frequency, symbol=None, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
    
    # Define less than operator for priority queue
    def __lt__(self, other):
        return self.frequency < other.frequency

# Function to build the Huffman Tree
def build_huffman_tree(symbols, frequencies):
    # Create a priority queue with initial nodes
    heap = [Node(frequencies[i], symbols[i]) for i in range(len(symbols))]
    heapq.heapify(heap)
    
    # Merge nodes until there's only one node left (the root of the Huffman Tree)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heap[0]

# Function to generate the Huffman codes by traversing the Huffman Tree
def generate_huffman_codes(node, code="", codebook={}):
    if node is not None:
        if node.symbol is not None:
            codebook[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", codebook)
        generate_huffman_codes(node.right, code + "1", codebook)
    return codebook

# Function to encode a message using the generated Huffman codes
def huffman_encode(message, huffman_codes):
    return ''.join(huffman_codes[symbol] for symbol in message)

# Function to decode a message using the Huffman Tree
def huffman_decode(encoded_message, huffman_tree):
    decoded_message = []
    node = huffman_tree
    for bit in encoded_message:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if node.symbol is not None:
            decoded_message.append(node.symbol)
            node = huffman_tree
    return ''.join(decoded_message)

# Example usage
symbols = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]

# Build the Huffman Tree
huffman_tree = build_huffman_tree(symbols, frequencies)

# Generate Huffman Codes
huffman_codes = generate_huffman_codes(huffman_tree)

# Encode a message
message = "abcdef"
encoded_message = huffman_encode(message, huffman_codes)
print(f"Encoded Message: {encoded_message}")

# Decode the message
decoded_message = huffman_decode(encoded_message, huffman_tree)
print(f"Decoded Message: {decoded_message}")
