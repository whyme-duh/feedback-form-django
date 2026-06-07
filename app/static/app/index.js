document.addEventListener("DOMContentLoaded", function () {
    // Find all textareas that depend on a radio option choice
    const dependentTextareas = document.querySelectorAll("[data-toggle-group]");

    dependentTextareas.forEach(textarea => {
        const groupID = textarea.getAttribute("data-toggle-group");
        const triggerValue = textarea.getAttribute("data-trigger-value");
        const radioContainer = document.getElementById(groupID);

        if (radioContainer) {
            // Listen for any selection changes inside the target pill group
            radioContainer.addEventListener("change", function (event) {
                if (event.target.matches('input[type="radio"]')) {
                    const selectedValue = event.target.value;

                    if (selectedValue === triggerValue) {
                        // Enable and switch style color back to standard focus mode
                        textarea.removeAttribute("disabled");
                        textarea.style.opacity = "1";
                        textarea.style.backgroundColor = "#fafbfe";
                    } else {
                        // Disable, dim it down, and clear out old text data
                        textarea.setAttribute("disabled", "disabled");
                        textarea.value = ""; 
                        textarea.style.opacity = "0.5";
                        textarea.style.backgroundColor = "#e2e8f0";
                    }
                }
            });

            // Run an initialization block to apply styling instantly on fresh load
            textarea.style.opacity = "0.5";
            textarea.style.backgroundColor = "#e2e8f0";
            textarea.style.transition = "all 0.2s ease";
        }
    });
});