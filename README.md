# Module Persistency 4 PyTorch

[![PyPI](https://img.shields.io/pypi/v/torch_model_persistency.svg)](https://pypi.python.org/pypi/torch-model-persistency)
[![Downloads](https://pepy.tech/badge/torch-model-persistency/week)](https://pepy.tech/project/torch-model-persistency) 


Save model state without suffering.

- [Install](#install)
- [Issues](#issues)
- [Tutorial](#tutorial)
- [Our Websites](#our-websites)
- [License](#license)



## Install

```
pip install torch-model-persistency
```



## Issues

This project is currently developed and maintained by [EyeCU Software Team](https://github.com/Eye-C-U). If you want any issue, you are very welcomed to send email to [head of the developer team](mailto:ovuruska@eyecuvision.com). It is always nice to hear from you people. Stay safe! 






## Tutorial

```python
from torch_persistency import ModulePersistency as MP
  

if __name__ == "__main__":
  
    # Training code
   
    mp = MP("checkpoint") 
    train_step(model)
    mp.save(model,epoch)

```


## Our Websites

[EyeCU Vision](https://eyecuvision.com/) \
[EyeCU Future](https://eyecufuture.com/) 


## License
 has MIT license. You can find further details in [LICENSE](LICENSE).
