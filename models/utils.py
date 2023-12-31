
def freeze_network(model, requires_grad=True):
    for param in model.parameters():
        param.requires_grad = requires_grad

    return model