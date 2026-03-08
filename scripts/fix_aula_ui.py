import os
import re

directory = r'D:\SourceCode\REPOS\github.io\ads_mod_07_backends_e_apis\docs\aulas'

for filename in os.listdir(directory):
    if filename.startswith('aula-') and filename.endswith('.md'):
        if filename == 'aula-01.md': continue  # Already fixed
        
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine tags based on filename/content
        lesson_num = filename.split('-')[1].split('.')[0]
        tags = "[API, Backend, Módulo 07]" # Default tags for this repo
        
        # Check if title has icon at the end and move it to the prefix
        # Pattern: # Title 🌐
        match = re.search(r'^# (Aula \d+ - .*?) (🌐|💻|🧠|📊|📝|⚡)', content, re.MULTILINE)
        if match:
            full_title = match.group(0)
            title_text = match.group(1)
            icon = match.group(2)
            new_title = f"# {icon} {title_text}"
            content = content.replace(full_title, new_title)
        
        # Add frontmatter if not present
        if not content.startswith('---'):
            frontmatter = f"---\ntags: {tags}\n---\n\n"
            content = frontmatter + content
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
