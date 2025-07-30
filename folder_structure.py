import os

def print_dir_structure(path, indent=0):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        print("    " * indent + "|-- " + item)
        if os.path.isdir(item_path):
            print_dir_structure(item_path, indent + 1)

# Example usage
print_dir_structure("/Users/ankitnayan/Downloads/final_web_v1/web_crawl")
