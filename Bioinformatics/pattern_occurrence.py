import GST

#inputing file should be considered

def pattern():
    input1 = input("input:")
    st = GST.STree(input1)
    print("suffix tree generated!")
    patt = input("please enter pattern :")
    print("pattern occurs in :")
    print(st.find_all(patt))