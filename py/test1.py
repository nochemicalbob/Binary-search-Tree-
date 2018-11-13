#2017038037 소프트웨어 김도연


#노드 구현, key, string 입력받아서 노드 구성. left, right 초기화
class Node:
    def __init__(self, key, string):
        self.val = key
        self.info = string
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = Node(None, None)
        self.preorder_list = []

    # 노드 추가
    def insert(self, key, string):
        if self.head.val is None:
            self.head.val = key
            self.head.info = string
        else:
            self.insert_sub(self.head, key, string)

    def insert_sub(self, cur, key, string):
        if cur.val > key:
            if cur.left is None:
                cur.left = Node(key, string)
            else:
                self.insert_sub(cur.left, key, string)
        else:
            if cur.right is None:
                cur.right = Node(key, string)
            else:
                self.insert_sub(cur.right, key, string)

    # 노드 찾기 , 찾으면 True, 없으면 False 반환
    def search(self, key):
        if self.head.val is None:
            return False
        else:
            return self.sub_search(self.head, key)

    def sub_search(self, cur, key):
        if cur is None:
            return False
        elif cur.val == key:
            return cur.info
        elif cur.val > key:
            return self.sub_search(cur.left, key)
        elif cur.val < key:
            return self.sub_search(cur.right, key)

    # 삭제
    def delete(self, key):
        if self.head.val is None:
            print("no key!")

        elif self.head.val == key:
            if self.head.left is None and self.head.right is None:
                self.head.val = None

            elif self.head.left is not None and self.head.right is None:
                self.head = self.head.left

            elif self.head.left is None and self.head.right is not None:
                self.head = self.head.right

            else:
                self.head.val = self.seach_left_node(self.head.right).val
                self.delete_node(self.head, self.head.right, self.head.val)
        else:
            if self.head.val > key:
                self.sub_delete(self.head, self.head.left, key)
            else:
                self.sub_delete(self.head, self.head.right, key)

    def sub_delete(self, parent, cur_node, key):
        if cur_node is None:
            print("no key!")

        elif cur_node.val == key:
            if cur_node.left is None and cur_node.right is None:
                if parent.left == cur_node:
                    parent.left = None
                else:
                    parent.right = None
            elif cur_node.left is not None and cur_node.right is None:
                if parent.left == cur_node:
                    parent.left = cur_node.left
                else:
                    parent.right = cur_node.left
            elif cur_node.left is None and cur_node.right is not None:
                if parent.left == cur_node:
                    parent.left = cur_node.right
                else:
                    parent.right = cur_node.right
            else:
                cur_node.val = self.seach_left_node(cur_node.right).val
                self.delete_node(cur_node, cur_node.right, cur_node.val)

        elif cur_node.val < key:
            self.sub_delete(cur_node, cur_node.right, key)

        else:
            self.sub_delete(cur_node, cur_node.left, key)

    def delete_node(self, parent, cur_node, key):
        if cur_node.val == key:
            if parent.left == cur_node:
                parent.left = None
            else:
                parent.right = None
        else:
            if cur_node.val > key:
                self.delete_node(cur_node, cur_node.left, key)
            else:
                self.delete_node(cur_node, cur_node.right, key)

    def seach_left_node(self, cur_node):
        if cur_node.left is None:
            return cur_node
        else:
            return self.seach_left_node(cur_node.left)

    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        print(cur.val, cur.info)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    def postorder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)
        if cur.right is not None:
            self.__postorder(cur.right)
        print(cur.val, cur.info)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)
        if cur.right is not None:
            self.__inorder(cur.right)
        print(cur.val, cur.info)
