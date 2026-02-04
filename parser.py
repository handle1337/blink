

# Because CDS only produces files with non CSV separators we parse them


import re

spaces = re.compile(r";+")

with open(".\\notebooks\\training_dataset.csv", 'w+') as e:

    with open(".\\notebooks\\asu.tsv",'r') as f:
        f_lines = list(f)[55:]
  
        for line in f_lines:
            
            newline = spaces.sub(',' , line).strip()
            print(newline)
            e.write(f"{newline}\n")


