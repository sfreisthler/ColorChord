# ColorChord

### Workflow
1. Run `source start_env.sh`
2. If you change dependencies, run `bash update_dependencies.sh`
3. `deactivate` gets you out of the virtual environment

### Local Testing 
1. Change src/index.js and src/processed.js from deployedBackend to local backend 
    DONT FORGET TO CHANGE THIS BACK WHEN YOU PUSH 
2. run server.py 

### Project Overview
1. Upload Photo
2. User sets number of slices -> determine window size
3. For each slice process slice (core algorithm)
4. Concatenate sounds
5. Play sound

### Core Algorithm
1. Determine primary color in slice -> determines which sample library to pull from
2. 2D FFT image slage
3. For each sound sample, compute correlation score
4. Pick sample with highest correlation


### Notes 
Dont forget to push samples.json to github when it is finished. 


