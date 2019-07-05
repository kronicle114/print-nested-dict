import json

## compare & contrasts 
dict1 = {
    'a': 'apple',
    'b': 12,
    'c': 'stff'
}

dict2 = {
    'a': 'apple',
    'b': 12,
    'd': {'rei': 123},
    'c': 'stff'   
}

def common_keys(obj1, obj2):
    comkeys = obj1.keys() & obj2.keys()
    print('common keys: ', comkeys)

# common_keys(dict1, dict2)

def unique_keys(obj1, obj2):
    ## find a key keys that dont exist on the other = ORDER MATTERS
    ## Take a set of keys from obj2 and ask this question: 
    ## Are there any keys that are in obj2 that are not in obj1?
    unikeys = obj2.keys() - obj1.keys()
    print('new keys on obj2: ', unikeys)

# unique_keys(dict1, dict2)

def subset_exists(obj1, obj2):
    ## do all the keys in obj1 exist in 2?
    print('Do all of the keys from obj1 exists in obj2? ', set(obj1) <= set(obj2))

# subset_exists(dict1, dict2)

## if subset_exist, then run the unique keys  

## Does dict1 contain all the keys in dict2 => superset
def superset_exist(obj1, obj2):
    print(set(obj1) >= set(obj2))

def dict_equal(obj1, obj2):
    print('are dicts equal?', obj1 == obj2)

dict_equal(dict1, dict2)

## if dict arent equal => find the difference

def match(d1, d2):
    return json.dumps(d1, sort_keys=True) == json.dumps(d2, sort_keys=True)

print('asd', match (dict1, dict2))