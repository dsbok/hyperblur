import os
import re

def fix_css():
    filepath = "/root/hyperblur/assets/css/base.css"
    with open(filepath, 'r') as f:
        content = f.read()
        
    content = content.replace('--color-background: #121212;', '--color-background: #000000;')
    content = content.replace('--color-top-level-card-bg: #1e1e1e;', '--color-top-level-card-bg: #000000;')
    
    with open(filepath, 'w') as f:
        f.write(content)

def fix_jinja():
    # Fix base.jinja SVGs
    base_file = "/root/hyperblur/src/templates/base.jinja"
    with open(base_file, 'r') as f:
        b_content = f.read()
    
    # SVG for today
    b_content = re.sub(r'<a class="nav-tab(.*?)href="/explore/today".*?>\s*<svg.*?</svg>\s*</a>', r'<a class="nav-tab\1href="/explore/today">[Today]</a>', b_content, flags=re.DOTALL)
    
    # SVG for trending
    b_content = re.sub(r'<a class="nav-tab(.*?)href="/explore/trending".*?>\s*<svg.*?</svg>\s*</a>', r'<a class="nav-tab\1href="/explore/trending">[Trending]</a>', b_content, flags=re.DOTALL)
    
    with open(base_file, 'w') as f:
        f.write(b_content)
        
    # Fix footer_interaction_buttons.jinja SVGs
    footer_file = "/root/hyperblur/src/templates/post/components/footer_interaction_buttons.jinja"
    with open(footer_file, 'r') as f:
        f_content = f.read()
        
    f_content = re.sub(r'<svg.*?</svg>', '<span>[Share]</span>', f_content, count=1, flags=re.DOTALL)
    f_content = re.sub(r'<svg.*?</svg>', '<span>[Tumblr]</span>', f_content, count=1, flags=re.DOTALL)
    
    with open(footer_file, 'w') as f:
        f_content = f_content.replace('<span>[Link]</span>', '')  # clean up any broken replacements from before
        f.write(f_content)

fix_css()
fix_jinja()
print("Fixed CSS to pure black and removed multiline SVGs.")
