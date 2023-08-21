from types import MappingProxyType
d={1:'a'}
d_proxy = MappingProxyType(d)
print(d_proxy)