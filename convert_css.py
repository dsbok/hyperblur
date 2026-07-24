import os
import re

css_dir = "/root/hyperblur/assets/css"

# Properties to completely remove
remove_patterns = [
    r'border-radius:\s*[^;]+;',
    r'box-shadow:\s*[^;]+;',
    r'transition:\s*[^;]+;',
    r'transform:\s*[^;]+;',
    r'backdrop-filter:\s*[^;]+;',
    r'background:\s*linear-gradient[^;]+;',
]

# We will completely overwrite base.css variables to be ultra minimalist black & white.
# And we'll change the font to basic system sans-serif.

def strip_bloat(content):
    for pat in remove_patterns:
        content = re.sub(pat, '', content)
    # Also fix some borders to be just solid 1px black
    content = re.sub(r'border:\s*1px solid [^;]+;', 'border: 1px solid #000;', content)
    content = re.sub(r'border-bottom:\s*[^;]+;', 'border-bottom: 1px solid #000;', content)
    content = re.sub(r'border-top:\s*[^;]+;', 'border-top: 1px solid #000;', content)
    return content

for file in os.listdir(css_dir):
    if file.endswith(".css"):
        filepath = os.path.join(css_dir, file)
        with open(filepath, 'r') as f:
            content = f.read()
        
        content = strip_bloat(content)

        if file == 'base.css':
            # Rewrite body variables block completely
            var_block = """
body {
    --color-background: #ffffff;
    --color-top-level-card-bg: #ffffff;
    --color-text: #000000;
    --color-text-secondary: #333333;

    --color-nav-bar-icon: #000000;
    --color-nav-bar-icon-hover: #0000EE;
    --color-nav-bar-selected-tab-highlight: #000000;
    --color-search-icon-fill: #000000;
    --color-search-bar-bg: #ffffff;
    --color-logo: #000000;

    --color-footer-text: #333333;

    --color-community-label-text: #000000;
    --color-community-label-button-text: #000000;
    --color-community-label-button-bg: #eeeeee;
    --color-community-label-button-highlight: #0000EE;
    --color-community-label-button-hover: #dddddd;
    --color-community-label-gradient-1: #ffffff;
    --color-community-label-gradient-2: #ffffff;

    --color-post-blog-name: #0000EE;
    --color-reblog-attribution: #333333;
    --color-post-link-block-subtitle: #333333;
    --color-post-header-date-separator: #000000;

    --color-ask-header: #000000;
    --color-ask-bg: #f8f8f8;

    --color-post-img-alt-text-widget-bg: #eeeeee;
    --color-post-img-alt-text-widget-text: #000000;

    --color-poll-text-color: #000000;
    --color-poll-winner-bg: #cccccc;
    --color-poll-proportion-bar-bg: #eeeeee;
    --color-poll-choice-bg: #ffffff;

    --color-post-reveal-truncated-content-button: #0000EE;
    --color-post-reveal-truncated-content-button-hover: #0000EE;

    --color-post-footer: #333333;
    --color-post-footer-post-interaction: #333333;
    --color-post-tag-bg: #eeeeee;
    --color-post-tag-hover: #dddddd;

    --color-trail-post-separator: #000000;

    --color-post-notes-viewer-nav-bar-bg: #ffffff;
    --color-post-notes-viewer-nav-bar-item: #000000;
    --color-read-more-text: #0000EE;

    --color-audio-controls-bg: #eeeeee;
    --color-audio-play-button-bg: #ffffff;
    --color-audio-play-button-icon-fill: #000000;

    --color-text-link: #0000EE;
    --color-text-link-hover: #0000EE;
    --color-text-hashtag: #0000EE;
    --color-text-hashtag-hover: #0000EE;

    --color-reblog-note-separator: #000000;

    --color-primary-button-bg: #ffffff;
    --color-primary-button-hover: #eeeeee;
    --color-primary-button-text: #000000;

    --color-secondary-button-bg: #ffffff;
    --color-secondary-button-hover: #eeeeee;
    --color-button-secondary-text: #000000;

    --color-tertiary-button-color: #000000;

    --color-dropdown-menu-bg: #ffffff;
    --color-dropdown-action-select: #ffffff;
    --color-dropdown-action-hover: #eeeeee;
    --color-control-bar-action-text: #000000;
    --color-dropdown-menu-item-selected: #eeeeee;
    --color-dropdown-menu-item-hover: #eeeeee;

    --color-blog-header-blog-name: #000000;

    --tumblr-signpost-bg: #ffffff;
    --tumblr-signpost-border: #000000;

    --color-alert-show-error-details: #333333;
    --color-alert-show-error-details-hover: #0000EE;
}
"""
            # Replace the body { ... } variables block
            content = re.sub(r'body\s*{[^}]+}', var_block, content, count=1)
            
            # Replace font
            content = re.sub(r'font-family:\s*[^;]+;', 'font-family: Arial, sans-serif;', content)
            
            # Make sure links look standard
            content = re.sub(r'color:\s*#3399ff;', 'color: #0000EE;', content)
            content = re.sub(r'color:\s*#66b2ff;', 'color: #0000EE;', content)
            
            # Fix gaps and paddings to be slightly tighter for frugal feel
            content = re.sub(r'gap:\s*15px;', 'gap: 8px;', content)
            
            # Replace background colors of elements to pure white where it was dark grey
            content = content.replace('background: #282828;', 'background: #ffffff; border: 1px solid #000;')
            content = content.replace('background: #141414;', 'background: #f4f4f4;')
            content = content.replace('background: #333333;', 'background: #eeeeee;')
            content = content.replace('background: #444444;', 'background: #cccccc;')
            content = content.replace('background: #0066cc;', 'background: #ffffff; color: #000000; border: 1px solid #000000;')
            content = content.replace('color: #ffffff;', 'color: #000000;')

        elif file == 'post.css':
            content = content.replace('background: #333333;', 'background: #eeeeee;')
            content = content.replace('background: #444444;', 'background: #dddddd;')
            content = content.replace('background: #141414;', 'background: #f4f4f4;')
            content = content.replace('background: #282828;', 'background: #ffffff; border: 1px solid #000;')
            content = content.replace('background: #0066cc;', 'background: #ffffff; color: #000000; border: 1px solid #000000;')
            content = content.replace('color: #ffffff;', 'color: #000000;')
            content = content.replace('color: #3399ff;', 'color: #0000EE;')
            content = content.replace('color: #66b2ff;', 'color: #0000EE;')
        
        with open(filepath, 'w') as f:
            f.write(content)

print("CSS transformed to brutalist minimalist.")
