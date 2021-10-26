"""
Bonus Challenge:
Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.
word -> emoticon
---
smile -> :)
grin -> :D
sad -> :(
mad	-> :P
Examples:
- emotify("Make me smile") ➞ "Make me :)"
- emotify("Make me grin") ➞ "Make me :D"
- emotify("Make me sad") ➞ "Make me :("
Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.

- replace all occurences of smile with :)
- replace all occurences of grin with :D
- replace all occurences of sad with :(
- replace all occurences of mad with :P

"""


def emotify(txt):
    emotes = {
        "smile": ":)",
        "grin": ":D",
        "sad": ":(",
        "mad": ":P"
    }

    # for k, v in emotes.items():
    #   txt = txt.replace(k, v)
    # return txt

    return f"Make me {emotes[txt[8:]]}"


print(emotify("Make me smile"))  # ➞ "Make me :)"
print(emotify("Make me grin"))  # ➞ "Make me :D"
print(emotify("Make me sad"))  # ➞ "Make me :("
print(emotify("Make me mad"))  # ➞ "Make me :P"
