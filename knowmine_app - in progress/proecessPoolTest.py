import concurrent.futures

nums = [1,2,3,4,5,6,7,8,9,10]

b = 2


def f(x,b):
    
    return (x * x)

def main():
    # Make sure the map and function are working
    args = ((a, b) for a in nums)
    # Test to make sure concurrent map is working
    with concurrent.futures.ThreadPoolExecutor() as executor:
         res = executor.map(lambda p: f(*p), args)
                
         for result in res:
             print(result)
               

if __name__ == '__main__':
    main()
