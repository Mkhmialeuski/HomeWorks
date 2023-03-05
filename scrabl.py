english = {1: ['a','e','i','o','u','l','n','s','t','r'],
           2: ['d','g'],
           3: ['b','c','m','p'],
           4: ['f', 'h', 'v', 'w', 'y'],
           5: ['k'],
           8: ['j','x'],
           10: ['q', 'z']}
russian = {1:['а','в','е','и','н','о','р','с','т'],
           2: ['д','к','л','м','п','у'],
           3: ['б','г','ё','ь','я'],
           4: ['й', 'ы'],
           5: ['ж','з','х','ц','ч'],
           8: ['ш','э','ю'],
           10: ['ф', 'щ', 'ъ']}
count = 0
word = input()
for i in word:
    for keys,valeu in english.items():
        if i in valeu:
            count += keys
for i in word:
    for keys,valeu in russian.items():
        if i in valeu:
            count += keys
print(count)
