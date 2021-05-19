Possible Errors
================

The package is written to run on several cores via 
`concurrent.futures.ProcessPoolExecutor(max_workers=n)`
sometimes there is a `BrokenProcessPool: A process in the process pool 
was terminated abruptly while the future was running or pending.`

Possible reasons:

Memory shortage:
- close all other programs running on the cores
- reduce the number of cores for running the package (cores_number)
- check the usage for Windows: 
    The calling of the function on Windows does not include
    if __name__ == '__main__':
		 main() 

The memory issue might be fixed in the future, do not forget to update 
the package from time to time.
