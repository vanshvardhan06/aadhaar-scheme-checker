document.addEventListener("DOMContentLoaded", function() {
    // Simulate a loading process
    setTimeout(function() {
        document.body.classList.add('loaded');
    }, 500); // Adjust the delay to simulate loading time

    // Add smooth scrolling on click for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault();

            const targetId = link.getAttribute("href").slice(1);
            const targetElement = document.getElementById(targetId);

            targetElement.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        });
    });
});
