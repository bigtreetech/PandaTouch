import os
import sys
from ruamel.yaml import YAML

def sync_yml_files(master_file='en-GB.yml'):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096  # To avoid wrapping long lines

    try:
        # Get the root of the repository
        repo_root = os.environ.get('GITHUB_WORKSPACE', '')
        
        # Set the working directory to the Translations folder
        working_dir = os.path.join(repo_root, 'Translations')
        os.chdir(working_dir)

        # Read the master file
        with open(master_file, 'r') as f:
            master_data = yaml.load(f)

        # Get the first level key of the master file
        master_key = list(master_data.keys())[0]

        # Walk through subdirectories
        for root, dirs, files in os.walk('.'):
            if root == '.':
                continue  # Skip the current directory

            for file in files:
                if file.endswith('.yml'):
                    target_file = os.path.join(root, file)
                    
                    # Read the target file
                    with open(target_file, 'r') as f:
                        target_data = yaml.load(f)

                    # Get the first level key of the target file
                    target_key = list(target_data.keys())[0]

                    # Update master dictionary with values from target dictionary
                    for key, value in target_data[target_key].items():
                        if key in master_data[master_key]:
                            master_data[master_key][key] = value

                    # Replace first level key in master_data with the one from target_data
                    new_master_data = {target_key: master_data[master_key]}

                    # Write the modified master dictionary to the target file
                    with open(target_file, 'w') as f:
                        yaml.dump(new_master_data, f)

        print("Synchronization complete.")
        return 0  # Successful execution

    except Exception as e:
        print(f"YML sync failure with exception: {str(e)}", file=sys.stderr)
        return 1  # Non-zero exit code to indicate failure

if __name__ == "__main__":
    exit_code = sync_yml_files()
    sys.exit(exit_code)