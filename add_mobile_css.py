import os

with open(r'd:\Sharm\assets\css\responsive.css', 'a', encoding='utf-8') as f:
    f.write("\n  .header-center {\n    position: static !important;\n    transform: none !important;\n    margin: 0 auto;\n  }\n")
    
print("Added header-center mobile styles.")
