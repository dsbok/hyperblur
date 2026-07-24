const noJSElements = document.querySelectorAll(".no-js");
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
