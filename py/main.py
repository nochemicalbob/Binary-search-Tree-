# 2017038037 김도연
# 소프트웨어 2학년 알고리즘 과제
# 파이썬 3.5.5 개발 환경 : anaconda
# git에서 자료들을 fork해서 사용하였습니다.

import test1 as doyeon
import os
import re

#기본세팅, 파일가져오기(파일 위치를 읽어서 가져옵니다)
bst = doyeon.BinarySearchTree()
address_for_you = os.getcwd()
print(address_for_you)
input_file = open("%s\\2017038037.txt" % address_for_you, 'r')
lines = input_file.readlines()
input_file.close()

#파일 읽고 정규표현식으로 문자, 숫자 나누기, 숫자는 key, 문자는 value 입니다
for element in lines:
    var = re.findall("\d+", element)
    var = int(''.join(var))
    string = re.findall("\D+", element)
    bst.insert(var, string)

#메뉴
def print_menu():
    print("1. inorder walk")
    print("2. preorder walk")
    print("3. postorder walk")
    print("4. insert")
    print("5. delete")
    print("6. search")
    print("7. quittt")
    menu = input('select your option : ')
    return int(menu)


def run():
    while True:
        menu = print_menu()
        if menu == 1:
            bst.inorder_traverse()
        elif menu == 2:
            bst.preorder_traverse()
        elif menu == 3:
            bst.postorder_traverse()
        elif menu == 4:
            var = int(input("inset the key(number) : "))
            string = input("insert the value(word) : ")
            bst.insert(var, string)
        elif menu == 5:
            del_key = int(input('input the key that you want to delete : '))
            bst.delete(del_key)
        elif menu == 6:
            ser_key = int(input('input the key that you want to find : '))
            print(bst.search(ser_key))
        elif menu == 7:
            break

if __name__ == "__main__":
    run()
