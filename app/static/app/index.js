document.addEventListener("DOMContentLoaded", function () {
    // Selecting everything that depends on a radio option choice 
    const dependentElements = document.querySelectorAll("[data-toggle-group]");

    dependentElements.forEach(element => {
        const groupID = element.getAttribute("data-toggle-group");
        const triggerValue = element.getAttribute("data-trigger-value");
        const radioContainer = document.getElementById(groupID);

        if (radioContainer) {
            function handleToggle(selectedValue) {
                const isTriggerMatch = (selectedValue === triggerValue);
                // since this toggle function can contain both text area and div with options, 
                // so were are checking for each entry
                if (element.tagName === "DIV") {
                    if (isTriggerMatch) {
                        // this makes the div visible
                        element.style.display = "flex"; 
                    } else {
                        element.style.display = "none"; 
                        // resets the value of the radio button
                        const childRadios = element.querySelectorAll('input[type="radio"]');
                        childRadios.forEach(radio => radio.checked = false);
                    }
                } else {
                    // this code block is for textarea
                    if (isTriggerMatch) {
                        element.removeAttribute("disabled");
                        element.style.opacity = "1";
                        element.style.backgroundColor = "#fafbfe";
                    } else {
                        element.setAttribute("disabled", "disabled");
                        element.value = ""; 
                        element.style.opacity = "0.5";
                        element.style.backgroundColor = "#e2e8f0";
                    }
                }
            }

            // it listens for any selection changes inside the target pill group
            radioContainer.addEventListener("change", function (event) {
                if (event.target.matches('input[type="radio"]')) {
                    handleToggle(event.target.value);
                }
            });

            // run initial check right away to apply starting state on fresh load
            const activeRadio = radioContainer.querySelector('input[type="radio"]:checked');
            const initialValue = activeRadio ? activeRadio.value : null;
            handleToggle(initialValue);
            
            // Apply safe CSS transition rules for smoother shifting
            element.style.transition = "all 0.2s ease";
        }
    });
});