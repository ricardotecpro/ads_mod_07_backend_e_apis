import os
import glob

base = r"d:\SourceCode\REPOS\github.io\ads_mod_07_backends_e_apis\docs"

# Fix index files and other markdown files
for filepath in glob.glob(os.path.join(base, "**", "*.md"), recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix Jinja double braces which confused the macros plugin
    content = content.replace("{{ .md-button .md-button--primary }}", "{ .md-button .md-button--primary }")
    content = content.replace("{{ .md-button }}", "{ .md-button }")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Fix quizzes index
quiz_idx = os.path.join(base, "quizzes", "index.md")
if os.path.exists(quiz_idx):
    with open(quiz_idx, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("quizze-", "quiz-").replace("Quizze ", "Quiz ")
    with open(quiz_idx, "w", encoding="utf-8") as f:
        f.write(content)

print("Fix applied.")
