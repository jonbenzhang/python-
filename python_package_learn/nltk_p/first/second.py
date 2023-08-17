import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
nltk.download("punkt")

# Initialize Python porter stemmer
ps = PorterStemmer()

example_sentence = "Python programmers often tend like programming in python because it's like english. We call people who program in python pythonistas."
a = "This layer includes the protocols used to describe the local network topology and the interfaces needed to affect the transmission of Internet layer datagrams to next-neighbor hosts"
example_sentence = a
# Remove punctuation
example_sentence_no_punct = example_sentence.translate(str.maketrans("", "", string.punctuation))

# Create tokens
word_tokens = word_tokenize(example_sentence_no_punct)

# Perform stemming
print("{0:20}{1:20}".format("--Word--","--Stem--"))
for word in word_tokens:
    print ("{0:20}{1:20}".format(word, ps.stem(word)))

"""
--Word--            --Stem--            
Python              python              
programmers         programm            
often               often               
tend                tend                
like                like                
programming         program             
in                  in                  
python              python              
because             becaus              
its                 it                  
like                like                
english             english             
We                  we                  
call                call                
people              peopl               
who                 who                 
program             program             
in                  in                  
python              python              
pythonistas         pythonista
"""