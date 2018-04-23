inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
listkey=['seashell', 'strange berry', 'lint']
inventory["pocket"]=listkey
backpack=(inventory["backpack"])
backpack.remove("dagger")
print(backpack)
inventory["gold"]=inventory["gold"]+50
print(inventory["gold"])
