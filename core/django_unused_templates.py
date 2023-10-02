import os
import subprocess

# Set your Django project directory here
PROJECT_DIRECTORY = '.'

def find_unused_python_functions():
    # Use pyflakes to find unused Python functions in your project directory
    result = subprocess.run(['pyflakes', PROJECT_DIRECTORY], capture_output=True, text=True)
    output = result.stdout
    unused_functions = []
    
    for line in output.splitlines():
        if line.startswith(PROJECT_DIRECTORY):
            parts = line.strip().split(':', 2)
            if len(parts) == 3:
                file_path, line_number, message = parts
                unused_functions.append({
                    'file_path': file_path.strip(),
                    'line_number': int(line_number.strip()),
                    'message': message.strip(),
                })

    return unused_functions

def find_unused_templates():
    # Walk through the templates directory and check for unreferenced templates
    referenced_templates = set()
    
    for root, _, files in os.walk(os.path.join(PROJECT_DIRECTORY, 'templates')):
        for file in files:
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                # You may need to adjust this regex pattern depending on how you reference templates
                template_refs = re.findall(r'{%\s*include\s+"(.*?)"', content)
                referenced_templates.update(template_refs)

    # Get a list of all templates in the templates directory
    all_templates = set()
    
    for root, _, files in os.walk(os.path.join(PROJECT_DIRECTORY, 'templates')):
        for file in files:
            template_path = os.path.relpath(os.path.join(root, file), PROJECT_DIRECTORY)
            all_templates.add(template_path)

    # Find templates that are not referenced
    unused_templates = all_templates - referenced_templates

    return unused_templates

if __name__ == '__main__':
    import re
    
    unused_functions = find_unused_python_functions()
    unused_templates = find_unused_templates()

    print("Unused Python Functions:")
    for func in unused_functions:
        print(f"{func['file_path']}:{func['line_number']} - {func['message']}")

    print("\nUnused Templates:")
    for template in unused_templates:
        print(template)
