Possible Errors
================

The package is parallelized via `concurrent.futures.ProcessPoolExecutor(max_workers=n)`.
Sometimes there is a `BrokenProcessPool: A process in the process pool 
was terminated abruptly while the future was running or pending.`

Possible solutions:

- close some or all other programs taking memory
- select all the code (Ctrl+A) and then run it(R9) 
  (instead of running the whole file)
- reduce the number of cores for running the package:
      find __init__ module in the installed package directory,
      change the number of max_workers n
   
The bug might be fixed in the future, do not forget to update 
the package from time to time.
