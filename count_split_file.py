import os, sys
import json

def load_json(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    data = data['ShapeNetV2']
    data = data[list(data.keys())[0]]
    return data

if __name__ == '__main__':
    class_name = 'car'
    fname_train = 'examples/splits/sv2_{}s_train.json'.format(class_name)
    fname_test = 'examples/splits/sv2_{}s_test.json'.format(class_name)

    data_train = load_json(fname_train)
    data_test = load_json(fname_test)

    num_train, num_test = len(data_train), len(data_test)
    print('num_train: {0}, num_test: {1}'.format(num_train, num_test))

