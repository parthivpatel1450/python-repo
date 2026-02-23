# Packing Example
def pack_example(*args):
    print("Packed arguments:", args)
pack_example(1, 2, 3, 'a', 'b')

# Unpacking Example
def unpack_example(a, b, c):
    print("Unpacked arguments:", a, b, c)
values = [1, 2, 3]
unpack_example(*values)