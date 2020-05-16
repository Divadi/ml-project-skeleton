This is a "default" ML file system for me. My ML projects will extend this structure.

checkpoints/ - will contain folders with model weights, specific to each experiment. Not sent to github.
configs/ - will contain .yaml config files that work with the YACS CfgNode.
src/
    config/ - contains the CfgNode class and default config. defaults.py should be modified based on the project.
    modeling/ - contains all model modules
    runners/ - contains python files for training, eval, etc.
    solver/ - contains optimizers, schedules, etc
    utils/
        ... - any project-specific utilities
        data/ - data-specific utilities.
        misc/ - general utilities. Ideally, this should not change between projects.
scripts/ - contains scripts that use src/runners to train, eval, etc.