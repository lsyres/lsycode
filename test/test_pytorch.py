import torch
x = torch.tensor(2.1,requires_grad=True)
y = (x-3)*(x-2)*(x-1)*x*(x+1)*(x+2)*(x+3)

y.backward()
print(x.grad)
