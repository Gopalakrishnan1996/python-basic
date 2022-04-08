def reverserWords(string):
    st = list()
    st1 = list()
    # Traverse given string and push all characters
    # to stack until we see a space.
    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])
        # When we see a space, we print
        # contents of stack.
        else:
            while len(st) > 0:
                print(st[-1], end="")
                st.pop()
            print(end=" ")
    # Since there may not be space after
    # last word.
    while len(st) > 0:
        # print(st[-1], end="")
        st1.append(st[-1])
        st.pop()

    print(st1)    

str = input('enter a input string here:')
reverserWords(str)        