def hangman(word):
    # syokisettei
     hang=["________________",
           "       |        ",
           "       o        ",
           "      /|\       ",
           "      / \       "
           ]
     letters=list(word)
     question=["_"]*len(word)
     wrong=0
     win=False

    #rupe
     while wrong<len(hang)+1:
         print("".join(question))
         print("\n".join(hang[0:wrong]))
         ask="Type a letter:"
         ans=input(ask)

         if ans in letters:
             print("Correct!")
             num=letters.index(ans)
             letters[num]="$"
             question[num]=ans

         else:
             print("wrong")
             wrong+=1

         if "_" not in question:
             print("you win")
             win=True
             break

    # haiboku
     if not win:
          print("you lose")
          print(word)
 
