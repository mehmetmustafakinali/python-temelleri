#decorator 
#özellikleri değiştirmek için kullanılan bir fonksiyon türüdür.
#genelde iç içe fonksiyonlar ile birlikte kullanılır.
#örnek:
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function
#decorator kullanımı
@decorator_function
def display():
    print("Display function ran")

display()
#kimlik doğrulama (authentication) ve yetkilendirme (authorization)
def authentication_decorator(func):
    def wrapper(*args, **kwargs):
        user_authenticated = True  # Simulate user authentication
        if user_authenticated:
            return func(*args, **kwargs)
        else:
            print("User not authenticated!")
    return wrapper
def sensitive_operation():
    print("Performing a sensitive operation...")
@authentication_decorator
def perform_sensitive_operation():
    sensitive_operation()
print("-------------------------------")
#performans izleme (performance monitoring) için bir decorator örneği
def performance_monitoring_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper
