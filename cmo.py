from colorama import Fore,Style
print(Fore.RED + "cmo text version 1.0")
print("coded by 0x.sweat")
print("program.cmo.quit closes the text editor \nit also saves the file unless you don't want to, if you don't then leave the save blank")
contents = []
code = ''

new_lines = ''
linespace = "\n"
def save ():
    fname = input("file to write : ")
    with open(fname, "w+") as f:
        f.write((code))
        f.close()

while new_lines != 'program.cmo.quit':
        new_lines = input("# ")
        if new_lines != 'program.cmo.quit':
                contents.append(new_lines)
                contents.append(linespace)
code = ''.join(contents)
save()
