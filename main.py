import os, random, sys
sex =random.choice(os.listdir("/Users/etudiant/Programming/make it hess/memes")) #change dir name to whatever

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("memes/"+sex)
imgplot = plt.imshow(img)
plt.xlabel("Take a good look, then close this window and enter your caption in the terminal.")
plt.xticks([])
plt.yticks([])
plt.show()
cum = input("Enter caption: ")
img = mpimg.imread("memes/"+sex)
imgplot = plt.imshow(img)
plt.xlabel(cum)
plt.xticks([])
plt.yticks([])
plt.show()
penis = input("Do you wish to save this meme? (y/n): ")
if penis.lower() == "y":
    img = mpimg.imread("memes/"+sex)
    imgplot = plt.imshow(img)
    plt.xlabel(cum)
    plt.xticks([])
    plt.yticks([])
    randomnum = random.randint(0,10000000000)
    plt.savefig(f"saved memes/meme{randomnum}.png")
    sys.exit()