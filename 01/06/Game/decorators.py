from datetime import datetime

# def logger(func):
    # print(f"Line number {1}")
# 
    # def wrapped_func(*args, **kwargs):
        # print(f"Line number {3}")
        # return func(*args, **kwargs)
    # 
    # print(f"Line number {2}")
    # 
    # return wrapped_func
# 
# @logger
# def pow2(num): # def wrapped_func(12) -> wrapped : pow2
    # print(f"Line number {4}")
    # return num ** 2
# 
# 
# @logger
# def is_even(num): # def wrapped_func(13) -> wrapped : is_even
    # return num % 2 == 0


def log_time(func):

    def wrap_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)  # run mai
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print(
            f"Elapsed time: {hours}: {minutes}: {seconds}",
        )
        return result

    return wrap_function