### algorithms

- file operations
    - `with open(filename) as f`
        - file modes: `r`, `rb`, `w`, `wb`
        - text mode vs binary mode
        - open vs. closed files
            - what happens when you try and do something with f outside the with block?
    - `f.read()`, `f.readline()`
    - `f.write()`, newline character `\n`
    - `f.seek()`
    - `os.path.join()`, `split()`, `splitext()`
    - JSON format for data storage/exchange
        - human readable, easy for computers to parse, supported by lots of different
        programming languages
        ```python
        import json
        # save to .json file:
        with open('outputfile.json') as jf:
            json.dump(something, jf)
        # load from .json file:
        with open('inputfile.json') as jf:
            something = json.load(jf)
        ````

- numpy
    - some linalg?
- scipy
    - stats
    - loadmat, savemat, .mat versions
    - ndimage
    - signal
        - filtering
        - fft
        - spectrograms
    - generate some audio! or write to .wav file and then listen to it
- sklearn, MDP
    - PCA, ICA
- talk a bit about math concepts
- opencv somewhere?
- jupyter notebook for interactive exploration of parameters and effect on resulting plots
    - lorenz attractor example looks nice!
