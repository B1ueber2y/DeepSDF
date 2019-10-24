import os, sys
import random
import json
import glob

def save_json(fname, data_list, class_id):
    data = {}
    data['ShapeNetV2'] = {}
    data['ShapeNetV2'][class_id] = data_list
    print(fname, len(data_list))
    with open(fname, 'w') as f:
        json.dump(data, f)

def filter_list(basedir, shape_id_list):
    new_list = []
    for shape_id in shape_id_list:
        fname_list = list(glob.iglob(os.path.join(basedir, shape_id) + '/**/*.obj')) + list(glob.iglob(os.path.join(basedir, shape_id) + '/*.obj'))
        if len(fname_list) == 0:
            continue
        new_list.append(shape_id)
    return new_list

def get_split_file(shapenet_dir, class_info, style='normal'):
    class_name, class_id = class_info
    path = os.path.join(shapenet_dir, class_id)

    shape_id_list = os.listdir(path)
    num_shapes = len(shape_id_list)

    if style == 'normal':
        num_train = int(num_shapes * 0.8)
        data_train = shape_id_list[:num_train]
        data_test = shape_id_list[num_train:]
    elif style == 'random':
        random.shuffle(shape_id_list)
        num_train = int(num_shapes * 0.8)
        data_train = shape_id_list[:num_train]
        data_test = shape_id_list[num_train:]
    else:
        raise NotImplementedError
    data_train = filter_list(path, data_train)
    data_test = filter_list(path, data_test)

    fname_train = os.path.join('examples/splits/sv2_{}s_train.json'.format(class_name))
    fname_test = os.path.join('examples/splits/sv2_{}s_test.json'.format(class_name))
    save_json(fname_train, data_train, class_id)
    save_json(fname_test, data_test, class_id)

if __name__ == '__main__':
    shapenet_dir = os.path.expanduser('~/data/ShapeNet/ShapeNetCore.v2')
    class_info_list = [('car', '02958343')] 
    for class_info in class_info_list:
        get_split_file(shapenet_dir, class_info)

