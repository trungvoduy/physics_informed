import torch.nn.functional as F


def add_padding(x, num_pad):
    if num_pad > 0:
        res = F.pad(x, (0, num_pad), 'constant', 0)
    else:
        res = x
    return res


def remove_padding(x, num_pad):
    if num_pad > 0:
        res = x[:, :, :, :, :-num_pad]
    else:
        res = x
    return res


def _get_act(act):
    if act == 'tanh':
        func = F.tanh
    elif act == 'gelu':
        func = F.gelu
    elif act == 'relu':
        func = F.relu_
    elif act == 'elu':
        func = F.elu_
    elif act == 'leaky_relu':
        func = F.leaky_relu_
    else:
        raise ValueError(f'{act} is not supported')
    return func

