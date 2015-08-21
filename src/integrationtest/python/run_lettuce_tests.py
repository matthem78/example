import lettuce.bin
import os

if __name__ == '__main__':
    # - lettuce uses a feature file directory path relative to this working directory
    WORKING_DIR = 'src/integrationtest/python'
    FEATURE_FILE_DIR = 'features' # relative to working directory
    os.chdir(WORKING_DIR)

    # Run lettuce with feature files and steps at location provided
    lettuce.bin.main([FEATURE_FILE_DIR])
