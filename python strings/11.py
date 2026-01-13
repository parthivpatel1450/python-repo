from string import Template

# Defining template string
str = "Hello and Welcome to $name !"

# Creating Template object
templateObj = Template(str)

# now provide values
new_str = templateObj.substitute(name="Tutorialspoint")
print(new_str)