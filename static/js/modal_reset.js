document.addEventListener('DOMContentLoaded', function () {
    const modals = document.querySelectorAll('.modal'); // Handle all modals (media and map)

    modals.forEach(modal => {
        modal.addEventListener('hidden.bs.modal', function () {
            setTimeout(() => {
                const modalTriggerButtons = document.querySelectorAll('[data-bs-toggle="modal"]');
                
                modalTriggerButtons.forEach(button => {
                    button.classList.remove('active');  // Reset active state
                    button.blur();                      // Ensure button loses focus
                });
            }, 50);  // Small delay ensures Bootstrap fully processes modal closure
        });
    });
});
