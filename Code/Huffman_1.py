# Huffman Coding

class node:
    def __init__(self, freq, symbol, left = None, right = None):
        # tan so / taN suat cua ky hieu
        self.freq = freq

        # ten ky hieu 
        self.symbol = symbol

        # nut ben trai cua nut hien tai
        self.left = left

        # nut ben phai cua nut hien tai
        self.right = right

        # dat ki hieu (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Ham in ma Huffman cho tat ca cac 
# ky hieu trong cay Huffman moi
# duoc tao
def printNodes(node, val = ''):
    # ma Huffman trong ma hien tai
    newVal = val + str(node.huff)

    # neu nut khong phai la nut canh 
    # thi di qua no
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

    # neu nut la nut canh no 
    # thi hien thi ma huffman
    # cua no
    if (not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")

# ky hieu trong cay huffman -- chars --
# tan so / tan suat cua ky hieu -- freq --

# Cac vi du minh hoa
# chars = ['f', 'e', 'd', 'c', 'b', 'a']
# freq = [45, 16, 13, 12, 9, 5]

# chars = ['S0', 'S1', 'S2', 'S3', 'S4']
# freq = [0.4, 0.2, 0.2, 0.1, 0.1]

chars = ['25', '24', '26', '23', '27', '22', '28', '21', '29', '20', '30']
freq = [0.21, 0.17, 0.15, 0.12, 0.1, 0.06, 0.05, 0.05, 0.04, 0.03, 0.02]

# chars = ['30', '20', '29', '21', '28', '22', '27', '23', '26', '24', '25']
# freq = [0.02, 0.03, 0.04, 0.05, 0.05, 0.06, 0.1, 0.12, 0.15, 0.17, 0.21]

# chars = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9']
# freq = [0.3, 0.25, 0.2, 0.05, 0.05, 0.05, 0.05, 0.02, 0.02, 0.01]

# tao danh sach 
nodes = []

# chuyen doi cac ky tu va tan so
# thanh cac nut trong cay huffman
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

nodes.sort(reverse = True)

while len(nodes) > 1:
    # sap xep tat ca cac nut theo thu tu 
    # giam dan dua tren tan so / tan suat 
    # cua chung
    right = nodes.pop()
    left = nodes.pop()

    # gan gia tri dinh huong cho cac nut nay
    if (left.freq < right.freq):
        left.huff = 1
        right.huff = 0
    else:
        left.huff = 0
        right.huff = 1

    # ket hop 2 nut nho nhat de tao nut moi 
    # lam nut cha cua chung
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    freq_current = left.freq + right.freq

    for i in range(len(nodes)):
        if freq_current >= nodes[i].freq:
            count = i
            break
        else: 
            continue

    nodes.insert(i, newNode)

# In ra ma Huffman cho tung ky hieu
printNodes(nodes[0])