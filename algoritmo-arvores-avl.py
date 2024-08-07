!pip install graphviz



from graphviz import Digraph

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        # Realiza a inserção normal de uma BST
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Atualiza a altura do nó ancestral
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Obtém o fator de balanceamento
        balance = self.get_balance(root)

        # Se o nó estiver desbalanceado, há 4 casos a considerar

        # Caso Esquerda-Esquerda
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Caso Direita-Direita
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Caso Esquerda-Direita
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Caso Direita-Esquerda
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Realiza a rotação
        y.left = z
        z.right = T2

        # Atualiza as alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Realiza a rotação
        y.right = z
        z.left = T3

        # Atualiza as alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def visualize(self, root):
        dot = Digraph()
        self._add_nodes_edges(root, dot)
        return dot

    def _add_nodes_edges(self, root, dot, parent=None):
        if not root:
            return
        dot.node(str(root.key))
        if parent:
            dot.edge(str(parent.key), str(root.key))
        self._add_nodes_edges(root.left, dot, root)
        self._add_nodes_edges(root.right, dot, root)

# Função para inserção e visualização passo a passo
def insert_and_visualize(keys):
    avl_tree = AVLTree()
    root = None
    for key in keys:
        print(f"Inserindo {key}")
        root = avl_tree.insert(root, key)
        display(avl_tree.visualize(root))

# Inserção das chaves do conjunto (a)
print("Conjunto (a):")
keys_a = [50, 30, 20, 70, 40, 35, 37, 38, 10, 32, 45, 42, 25, 47, 36]
insert_and_visualize(keys_a)

# Inserção das chaves do conjunto (b)
print("Conjunto (b):")
keys_b = [100, 80, 60, 40, 20, 70, 30, 50, 35, 45, 55, 75, 65, 73, 77]
insert_and_visualize(keys_b)

# Inserção das chaves do conjunto (c)
print("Conjunto (c):")
keys_c = [41, 38, 31, 12, 19, 8, 27, 49]
insert_and_visualize(keys_c)

# Inserção das chaves do conjunto (d)
print("Conjunto (d):")
keys_d = [10, 21, 15, 17, 16, 19, 20]
insert_and_visualize(keys_d)
