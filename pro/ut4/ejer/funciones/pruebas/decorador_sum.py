def sum_lists(func):
    def wrapper (*args,**kwargs):
        result = sum([sum(i)for i in func(*args,**kwargs)])
        return result
    return wrapper
@sum_lists
def run_func(*args:list):
    return args
print(run_func([1,3,4],[5,1,4]))