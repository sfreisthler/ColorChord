# ColorChord

NOTE: will probably need to install ffmpeg on backend server

### Workflow
1. Run `source start_env.sh`
2. If you change dependencies, run `bash update_dependencies.sh`
3. `deactivate` gets you out of the virtual environment

### Project Overview
1. Upload Photo
2. User sets number of slices -> determine window size
3. For each slice process slice (core algorithm)
4. Concatenate sounds
5. Play sound

### Core Algorithm
1. Determine primary color in slice -> determines which sample library to pull from
2. 2D FFT image slice
3. For each sound sample, compute correlation score
4. Pick sample with highest correlation

### To Dos (in order of attack)
- [x] Setup user input website
- [ ] Assemble (mini) sample library
- [ ] Compute correlation for mini sample library for each slice in image
- [ ] Assemble samples and output sound
- [ ] Add more sample sounds
- [ ] Add color component
- [ ] Make website cute
