import os
import re

# 1. Update base.js to handle the select changes and the media filter
js_content = """const noJSElements = document.querySelectorAll(".no-js");
for (let element of noJSElements) {
    element.classList.remove("no-js");
}

document.addEventListener("DOMContentLoaded", function() {
    const navSelects = document.querySelectorAll("select.nav-select");
    navSelects.forEach(select => {
        select.addEventListener("change", function() {
            if (this.value) {
                window.location.href = this.value;
            }
        });
    });

    const mediaFilter = document.getElementById("media-filter");
    if (mediaFilter) {
        function applyMediaFilter() {
            const filter = mediaFilter.value;
            if (filter === "media-only") {
                document.body.classList.add("media-only-mode");
            } else {
                document.body.classList.remove("media-only-mode");
            }
            localStorage.setItem("mediaFilterPreference", filter);
        }
        
        mediaFilter.addEventListener("change", applyMediaFilter);
        
        const savedFilter = localStorage.getItem("mediaFilterPreference");
        if (savedFilter) {
            mediaFilter.value = savedFilter;
            applyMediaFilter();
        }
    }
});
"""
with open("/root/hyperblur/assets/js/base.js", 'w') as f:
    f.write(js_content)

# 2. Fix base_blog.jinja by removing inline script and onchange
base_blog_path = "/root/hyperblur/src/templates/blog/base_blog.jinja"
with open(base_blog_path, 'r') as f:
    blog_content = f.read()

# Remove onchange
blog_content = blog_content.replace('onchange="applyMediaFilter()"', 'class="nav-select"')

# Remove inline script
blog_content = re.sub(r'<script>.*?</script>', '', blog_content, flags=re.DOTALL)

with open(base_blog_path, 'w') as f:
    f.write(blog_content)
    
# 3. Replace onchange in all other dropdowns
templates = [
    "/root/hyperblur/src/templates/search.jinja",
    "/root/hyperblur/src/templates/tagged.jinja",
    "/root/hyperblur/src/templates/post/notes/viewer/reblogs.jinja",
    "/root/hyperblur/src/templates/post/notes/viewer/replies.jinja"
]

for file in templates:
    with open(file, 'r') as f:
        content = f.read()
    
    content = content.replace('<select onchange="window.location.href=this.value">', '<select class="nav-select">')
    
    with open(file, 'w') as f:
        f.write(content)

print("Fixed JS for CSP and replaced inline handlers across templates.")
