from torchvision import models
import torch
model = models.densenet161(pretrained=True)
sm = torch.jit.script(model)
sm.save("my_fancy_model.pt")
