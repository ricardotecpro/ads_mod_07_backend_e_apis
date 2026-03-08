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
        
        # Move emoji from end to front
        # Pattern: # Aula XX - Title 🌐
        content = re.sub(r'^# (Aula \d+ - .*?)\s*([🌐💻🧠📊📝⚡])', r'# \2 \1', content, flags=re.MULTILINE)
        
        # Add frontmatter if not present
        if not content.startswith('---'):
            frontmatter = f"---\ntags: {tags}\n---\n\n"
            content = frontmatter + content
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
