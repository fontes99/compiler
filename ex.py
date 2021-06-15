x = {
    'a' : {
        'value' : 12,
        'type' : 'int'
    },
    'b' : {
        'value' : 13,
        'type' : 'int'
    },
    'c' : {
        'value' : 14,
        'type' : 'int'
    }
}

params = x.keys()
it_params = iter(params)

print(next(it_params))