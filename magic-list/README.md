# magic_list

A class that implements a simplified list by skipping boundary checks when possible

You can use it as list by using:
```python
new_list = MagicList()
new_list[0] = 28
new_list[1] = 124
.
.
.  

```

Or by using a cls_type by running:

```python
new_list = MagicList(cls_type=Person)
new_list[0].age = 28
new_list[1]weight = 124
.
.
.  

```
 