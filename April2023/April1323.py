# General Patron is faced with a problem , his intelligence has intercepted some secret messages from the enemy but they are all encrypted. Those messages are crucial to getting the jump on the enemy and winning the war. Luckily intelligence also captured an encoding device as well. However even the smartest programmers weren't able to crack it though. So the general is asking you , his most odd but brilliant programmer.
# You can call the encoder like this.
# encode("Hello World!")
# Our cryptoanalysts kept poking at it and found some interesting patterns.
# print(
# encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
# print(
# encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
# print(encode("!@#$%^&*()_+-"))
# a,b,c = "", "", ""
# for w in "abcdefghijklmnopqrstuvwxyz":
#     a += encode(  "" + w)[0]
#     b += encode( "_" + w)[1]
#     c += encode("__" + w)[2]
# print(a)
# print(b)
# print(c)
# We think if you keep on this trail you should be able to crack the code! You are expected to fill in the
# decode
# function. Good luck ! General Patron is counting on you!


def decode(message):
    # Define the decoding map
    decoding_map = {
        "a": "",
        "b": "_",
        "c": "__",
        "d": "___",
        "e": "____",
        "f": "_____",
        "g": "______",
        "h": "_______",
        "i": "________",
        "j": "_________",
        "k": "+",
        "l": "-",
        "m": "*",
        "n": "/",
        "o": "%",
        "p": "=",
        "q": "(",
        "r": ")",
        "s": "<",
        "t": ">",
        "u": "^",
        "v": "&",
        "w": "|",
        "x": "~",
        "y": "`",
        "z": "!"
    }
    
    # Split the encoded message into its three parts
    a, b, c = message
    
    # Decode the first part
    first_char = ""
    for char in a:
        if char != "":
            first_char = decoding_map[char]
            break
    
    # Decode the second part
    second_char = ""
    for char in b:
        if char != "_":
            second_char = decoding_map[char]
            break
    
    # Decode the third part
    third_char = ""
    for char in c:
        if char != "__":
            third_char = decoding_map[char]
            break
    
    # Combine the decoded parts into the final message
    decoded_message = ""
    for i in range(max(len(a), len(b), len(c))):
        decoded_message += decoding_map.get(a[i], "")
        decoded_message += decoding_map.get(b[i], "")
        decoded_message += decoding_map.get(c[i], "")
    
    # Return the decoded message
    return decoded_message.replace(first_char, "", 1).replace(second_char, "_", 1).replace(third_char, "__", 1)
